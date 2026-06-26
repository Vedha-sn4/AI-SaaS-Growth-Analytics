import os
import pandas as pd

os.makedirs("data/processed", exist_ok=True)

# -----------------------------
# LOAD FILES
# -----------------------------

churn = pd.read_csv(
    "data/processed/churn_predictions.csv"
)

segments = pd.read_csv(
    "data/processed/customer_segments.csv"
)

# -----------------------------
# MERGE DATA
# -----------------------------

df = churn.merge(
    segments[
        [
            "user_id",
            "segment"
        ]
    ],
    on="user_id",
    how="left"
)

# -----------------------------
# RECOMMENDATION ENGINE
# -----------------------------

def get_recommendation(row):

    risk = row["risk_level"]
    segment = row["segment"]
    revenue = row["monthly_revenue"]

    # High Risk Customers

    if risk == "High":

        if revenue >= 5000:
            return "Assign Account Manager"

        return "Offer 20% Discount"

    # Medium Risk Customers

    elif risk == "Medium":

        if segment == "At-Risk Users":
            return "Provide Product Training"

        return "Email Engagement Campaign"

    # Low Risk Customers

    else:

        if segment == "Power Users":
            return "Upsell Enterprise Plan"

        return "No Action Needed"

# -----------------------------
# APPLY RECOMMENDATIONS
# -----------------------------

df["recommendation"] = df.apply(
    get_recommendation,
    axis=1
)

# -----------------------------
# SAVE OUTPUT
# -----------------------------

output = df[
    [
        "user_id",
        "plan_type",
        "monthly_revenue",
        "churn_probability",
        "risk_level",
        "segment",
        "recommendation"
    ]
]

output.to_csv(
    "data/processed/customer_recommendations.csv",
    index=False
)

# -----------------------------
# SUMMARY
# -----------------------------

print("\nRecommendations Generated\n")

print(
    output["recommendation"]
    .value_counts()
)

print(
    "\nSaved: data/processed/customer_recommendations.csv"
)