import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

os.makedirs("data/processed", exist_ok=True)

# --------------------------------
# LOAD DATA
# --------------------------------

subs = pd.read_csv(
    "data/raw/subscriptions.csv"
)

usage = pd.read_csv(
    "data/raw/feature_usage.csv"
)

tickets = pd.read_csv(
    "data/raw/support_tickets.csv"
)

# --------------------------------
# FEATURE ENGINEERING
# --------------------------------

usage_summary = (
    usage.groupby("user_id")["usage_count"]
    .sum()
    .reset_index()
)

usage_summary.rename(
    columns={
        "usage_count": "total_usage"
    },
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

df["total_usage"] = (
    df["total_usage"]
    .fillna(0)
)

df["ticket_count"] = (
    df["ticket_count"]
    .fillna(0)
)

# --------------------------------
# FEATURES FOR CLUSTERING
# --------------------------------

X = df[
    [
        "monthly_revenue",
        "total_usage",
        "ticket_count"
    ]
]

# --------------------------------
# SCALE DATA
# --------------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# --------------------------------
# KMEANS
# --------------------------------

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["cluster"] = (
    kmeans.fit_predict(X_scaled)
)

# --------------------------------
# CLUSTER LABELS
# --------------------------------

cluster_stats = (
    df.groupby("cluster")
    ["monthly_revenue"]
    .mean()
    .sort_values()
)

cluster_order = (
    cluster_stats.index.tolist()
)

cluster_mapping = {
    cluster_order[0]: "At-Risk Users",
    cluster_order[1]: "Normal Users",
    cluster_order[2]: "Power Users"
}

df["segment"] = (
    df["cluster"]
    .map(cluster_mapping)
)

# --------------------------------
# EXPORT
# --------------------------------

output = df[
    [
        "user_id",
        "plan_type",
        "monthly_revenue",
        "total_usage",
        "ticket_count",
        "segment"
    ]
]

output.to_csv(
    "data/processed/customer_segments.csv",
    index=False
)

# --------------------------------
# SUMMARY
# --------------------------------

print("\nCustomer Segmentation Complete\n")

print(
    output["segment"]
    .value_counts()
)

print(
    "\nSaved: data/processed/customer_segments.csv"
)