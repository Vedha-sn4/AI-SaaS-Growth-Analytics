import os
from datetime import timedelta

import numpy as np
import pandas as pd
from faker import Faker
from random import randint, choice, choices

# -----------------------------
# SETUP
# -----------------------------
fake = Faker()

os.makedirs("data/raw", exist_ok=True)

NUM_USERS = 5000
NUM_USAGE = 50000
NUM_TICKETS = 10000

# -----------------------------
# USERS
# -----------------------------
industries = [
    "Technology",
    "Healthcare",
    "Finance",
    "Education",
    "Retail"
]

company_sizes = [
    "Small",
    "Medium",
    "Large"
]

users = []

for user_id in range(1, NUM_USERS + 1):

    users.append([
        user_id,
        fake.date_between(start_date="-3y", end_date="today"),
        fake.country(),
        choice(industries),
        choice(company_sizes)
    ])

users_df = pd.DataFrame(
    users,
    columns=[
        "user_id",
        "signup_date",
        "country",
        "industry",
        "company_size"
    ]
)

# -----------------------------
# SUBSCRIPTIONS
# -----------------------------
plans = {
    "Starter": 999,
    "Professional": 2999,
    "Enterprise": 9999
}

subscriptions = []

for user_id in range(1, NUM_USERS + 1):

    plan = choices(
        ["Starter", "Professional", "Enterprise"],
        weights=[60, 30, 10],
        k=1
    )[0]

    monthly_revenue = plans[plan]

    churn_probability = {
        "Starter": 0.30,
        "Professional": 0.15,
        "Enterprise": 0.05
    }

    is_churned = np.random.choice(
        [0, 1],
        p=[
            1 - churn_probability[plan],
            churn_probability[plan]
        ]
    )

    subscriptions.append([
        user_id,
        user_id,
        plan,
        monthly_revenue,
        fake.date_between(start_date="-2y", end_date="today"),
        is_churned
    ])

subscriptions_df = pd.DataFrame(
    subscriptions,
    columns=[
        "subscription_id",
        "user_id",
        "plan_type",
        "monthly_revenue",
        "subscription_start",
        "is_churned"
    ]
)

# -----------------------------
# PAYMENTS
# -----------------------------
payments = []
payment_id = 1

for _, row in subscriptions_df.iterrows():

    num_payments = randint(3, 12)

    for _ in range(num_payments):

        payments.append([
            payment_id,
            row["user_id"],
            fake.date_between(
                start_date="-1y",
                end_date="today"
            ),
            row["monthly_revenue"],
            choice([
                "Success",
                "Success",
                "Success",
                "Failed"
            ])
        ])

        payment_id += 1

payments_df = pd.DataFrame(
    payments,
    columns=[
        "payment_id",
        "user_id",
        "payment_date",
        "amount",
        "payment_status"
    ]
)

# -----------------------------
# FEATURE USAGE
# -----------------------------
features = [
    "Dashboard",
    "Reports",
    "Analytics",
    "Automation",
    "Exports",
    "Integrations"
]

usage = []

for usage_id in range(1, NUM_USAGE + 1):

    usage.append([
        usage_id,
        randint(1, NUM_USERS),
        choice(features),
        randint(1, 30),
        fake.date_between(
            start_date="-1y",
            end_date="today"
        )
    ])

usage_df = pd.DataFrame(
    usage,
    columns=[
        "usage_id",
        "user_id",
        "feature_name",
        "usage_count",
        "usage_date"
    ]
)

# -----------------------------
# SUPPORT TICKETS
# -----------------------------
ticket_texts = [
    "Dashboard loads slowly",
    "Unable to login",
    "Billing issue detected",
    "Need export functionality",
    "Analytics report incorrect",
    "Integration not working",
    "Application crashes frequently",
    "Feature request for automation",
    "Payment failed unexpectedly",
    "Data sync problem"
]

tickets = []

for ticket_id in range(1, NUM_TICKETS + 1):

    created_date = fake.date_between(
        start_date="-1y",
        end_date="today"
    )

    resolved_date = created_date + timedelta(
        days=randint(1, 10)
    )

    tickets.append([
        ticket_id,
        randint(1, NUM_USERS),
        choice(ticket_texts),
        created_date,
        resolved_date
    ])

tickets_df = pd.DataFrame(
    tickets,
    columns=[
        "ticket_id",
        "user_id",
        "ticket_text",
        "created_date",
        "resolved_date"
    ]
)

# -----------------------------
# SAVE FILES
# -----------------------------
users_df.to_csv(
    "data/raw/users.csv",
    index=False
)

subscriptions_df.to_csv(
    "data/raw/subscriptions.csv",
    index=False
)

payments_df.to_csv(
    "data/raw/payments.csv",
    index=False
)

usage_df.to_csv(
    "data/raw/feature_usage.csv",
    index=False
)

tickets_df.to_csv(
    "data/raw/support_tickets.csv",
    index=False
)

# -----------------------------
# SUMMARY
# -----------------------------
print("Dataset generation completed successfully!")
print(f"Users: {len(users_df):,}")
print(f"Subscriptions: {len(subscriptions_df):,}")
print(f"Payments: {len(payments_df):,}")
print(f"Feature Usage: {len(usage_df):,}")
print(f"Support Tickets: {len(tickets_df):,}")