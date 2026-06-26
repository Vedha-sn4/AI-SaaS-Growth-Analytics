import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("data/processed", exist_ok=True)

users = pd.read_csv("data/raw/users.csv")
subs = pd.read_csv("data/raw/subscriptions.csv")
payments = pd.read_csv("data/raw/payments.csv")
usage = pd.read_csv("data/raw/feature_usage.csv")
tickets = pd.read_csv("data/raw/support_tickets.csv")

print("\n===== DATA SHAPES =====")
print("Users:", users.shape)
print("Subscriptions:", subs.shape)
print("Payments:", payments.shape)
print("Usage:", usage.shape)
print("Tickets:", tickets.shape)

# -----------------------------
# Revenue by Plan
# -----------------------------
revenue = (
    subs.groupby("plan_type")["monthly_revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
revenue.plot(kind="bar")
plt.title("Revenue by Plan")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("data/processed/revenue_by_plan.png")
plt.close()

# -----------------------------
# Users by Industry
# -----------------------------
industry = users["industry"].value_counts()

plt.figure(figsize=(8, 5))
industry.plot(kind="bar")
plt.title("Users by Industry")
plt.tight_layout()
plt.savefig("data/processed/users_by_industry.png")
plt.close()

# -----------------------------
# Churn Distribution
# -----------------------------
churn = subs["is_churned"].value_counts()

plt.figure(figsize=(6, 4))
churn.plot(kind="bar")
plt.title("Churn Distribution")
plt.tight_layout()
plt.savefig("data/processed/churn_distribution.png")
plt.close()

# -----------------------------
# Feature Usage
# -----------------------------
feature_usage = (
    usage.groupby("feature_name")["usage_count"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
feature_usage.plot(kind="bar")
plt.title("Feature Usage")
plt.tight_layout()
plt.savefig("data/processed/feature_usage.png")
plt.close()

# -----------------------------
# Payment Status
# -----------------------------
payment_status = payments["payment_status"].value_counts()

plt.figure(figsize=(6, 4))
payment_status.plot(kind="bar")
plt.title("Payment Status")
plt.tight_layout()
plt.savefig("data/processed/payment_status.png")
plt.close()

print("\nEDA completed successfully.")
print("Charts saved in data/processed/")