import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

os.makedirs("data/processed", exist_ok=True)

# -----------------------------
# LOAD DATA
# -----------------------------

subs = pd.read_csv("data/raw/subscriptions.csv")
usage = pd.read_csv("data/raw/feature_usage.csv")
tickets = pd.read_csv("data/raw/support_tickets.csv")

# -----------------------------
# FEATURE ENGINEERING
# -----------------------------

usage_summary = (
    usage.groupby("user_id")["usage_count"]
    .sum()
    .reset_index()
)

usage_summary.rename(
    columns={"usage_count": "total_usage"},
    inplace=True
)

ticket_summary = (
    tickets.groupby("user_id")
    .size()
    .reset_index(name="ticket_count")
)

df = subs.merge(
    usage_summary,
    on="user_id",
    how="left"
)

df = df.merge(
    ticket_summary,
    on="user_id",
    how="left"
)

df["total_usage"] = df["total_usage"].fillna(0)
df["ticket_count"] = df["ticket_count"].fillna(0)

# -----------------------------
# ENCODE PLAN TYPE
# -----------------------------

plan_mapping = {
    "Starter": 0,
    "Professional": 1,
    "Enterprise": 2
}

df["plan_encoded"] = df["plan_type"].map(plan_mapping)

# -----------------------------
# FEATURES / TARGET
# -----------------------------

X = df[
    [
        "monthly_revenue",
        "plan_encoded",
        "total_usage",
        "ticket_count"
    ]
]

y = df["is_churned"]

# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# MODEL
# -----------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# EVALUATION
# -----------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nAccuracy:", round(accuracy, 4))

print(
    classification_report(
        y_test,
        predictions
    )
)

# -----------------------------
# CHURN PROBABILITY
# -----------------------------

df["churn_probability"] = (
    model.predict_proba(X)[:, 1]
)

# -----------------------------
# RISK LEVEL
# -----------------------------

def assign_risk(prob):

    if prob >= 0.80:
        return "High"

    elif prob >= 0.50:
        return "Medium"

    else:
        return "Low"

df["risk_level"] = df[
    "churn_probability"
].apply(assign_risk)

# -----------------------------
# SAVE OUTPUT
# -----------------------------

output = df[
    [
        "user_id",
        "plan_type",
        "monthly_revenue",
        "total_usage",
        "ticket_count",
        "is_churned",
        "churn_probability",
        "risk_level"
    ]
]

output.to_csv(
    "data/processed/churn_predictions.csv",
    index=False
)

# -----------------------------
# FEATURE IMPORTANCE
# -----------------------------

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

importance.to_csv(
    "data/processed/feature_importance.csv",
    index=False
)

print("\nSaved:")
print("data/processed/churn_predictions.csv")
print("data/processed/feature_importance.csv")