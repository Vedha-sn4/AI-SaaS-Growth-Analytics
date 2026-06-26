import os
import pandas as pd

os.makedirs("data/processed", exist_ok=True)

# -----------------------------
# LOAD DATA
# -----------------------------

tickets = pd.read_csv(
    "data/raw/support_tickets.csv"
)

# -----------------------------
# ISSUE CATEGORIZATION
# -----------------------------

def categorize_ticket(text):

    text = str(text).lower()

    if "billing" in text:
        return "Billing Issue"

    elif "login" in text:
        return "Login Problem"

    elif "integration" in text:
        return "Integration Issue"

    elif "crash" in text:
        return "Performance Issue"

    elif "export" in text:
        return "Export Issue"

    elif "report" in text:
        return "Reporting Issue"

    else:
        return "General Inquiry"

# -----------------------------
# SENTIMENT ANALYSIS
# -----------------------------

negative_keywords = [
    "crash",
    "slow",
    "failed",
    "problem",
    "incorrect",
    "error"
]

positive_keywords = [
    "good",
    "great",
    "excellent",
    "thank",
    "resolved"
]

def sentiment(text):

    text = str(text).lower()

    if any(word in text for word in negative_keywords):
        return "Negative"

    elif any(word in text for word in positive_keywords):
        return "Positive"

    return "Neutral"

# -----------------------------
# PRIORITY
# -----------------------------

def priority(text):

    text = str(text).lower()

    if (
        "crash" in text
        or "failed" in text
        or "login" in text
    ):
        return "High"

    elif (
        "billing" in text
        or "integration" in text
    ):
        return "Medium"

    return "Low"

# -----------------------------
# APPLY NLP LOGIC
# -----------------------------

tickets["category"] = (
    tickets["ticket_text"]
    .apply(categorize_ticket)
)

tickets["sentiment"] = (
    tickets["ticket_text"]
    .apply(sentiment)
)

tickets["priority"] = (
    tickets["ticket_text"]
    .apply(priority)
)

# -----------------------------
# EXPORT
# -----------------------------

tickets.to_csv(
    "data/processed/support_ticket_analysis.csv",
    index=False
)

# -----------------------------
# SUMMARY
# -----------------------------

print("NLP Analysis Completed")

print("\nCategory Counts:")
print(
    tickets["category"]
    .value_counts()
)

print("\nSentiment Counts:")
print(
    tickets["sentiment"]
    .value_counts()
)

print("\nPriority Counts:")
print(
    tickets["priority"]
    .value_counts()
)

print(
    "\nSaved: data/processed/support_ticket_analysis.csv"
)