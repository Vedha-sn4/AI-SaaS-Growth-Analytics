# AI-SaaS-Growth-Analytics

## Project Overview

AI-SaaS-Growth-Analytics is an end-to-end analytics project that simulates a real-world SaaS business environment. The project combines SQL, Python, Machine Learning, NLP, and Power BI to analyze customer behavior, subscription revenue, product usage, churn risk, and customer support trends.

The project demonstrates how raw business data can be transformed into actionable insights through analytics, predictive modeling, and interactive dashboards.

---

## Tech Stack

- SQL
- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Faker
- Power BI

---

## Project Architecture

```
Synthetic Data
      │
      ▼
Python Data Generation
      │
      ▼
CSV Datasets
      │
      ▼
SQL Analytics
      │
      ▼
Python Analytics
 ├── Data Cleaning & EDA
 ├── Churn Prediction
 ├── NLP Analysis
 ├── Customer Segmentation
 └── AI Recommendations
      │
      ▼
Power BI Dashboards
```

---

## Dataset

The project uses realistic synthetic SaaS datasets.

### Raw Data

- Users
- Subscriptions
- Payments
- Feature Usage
- Support Tickets

### Processed Data

- Churn Predictions
- Customer Segments
- Support Ticket Analysis
- Customer Recommendations
- Feature Importance

---

## Key Features

### SQL Analytics

- Monthly Recurring Revenue (MRR)
- Annual Recurring Revenue (ARR)
- Churn Rate
- Customer Lifetime Value (CLV)
- Cohort Analysis
- Retention Analysis
- Revenue Analytics

### Machine Learning

- Customer Churn Prediction using Random Forest
- Churn Probability
- Risk Classification
- Feature Importance Analysis

### Natural Language Processing

- Support Ticket Sentiment Analysis
- Issue Categorization
- Priority Classification

### Customer Segmentation

- K-Means Clustering
- Power Users
- Normal Users
- At-Risk Users

### AI Recommendations

Business recommendations generated based on customer behavior and churn risk.

---

## Power BI Report

The Power BI report contains five dashboard pages:

- Executive Dashboard
- Revenue Analytics
- AI Churn Intelligence
- Customer Intelligence
- Support & AI Recommendations

---

## Project Structure

```
AI-SaaS-Growth-Analytics
│
├── data
│   ├── raw
│   └── processed
│
├── scripts
│   ├── generate_data.py
│   ├── eda.py
│   ├── churn_prediction.py
│   ├── nlp_analysis.py
│   ├── customer_segmentation.py
│   └── recommendations.py
│
├── sql
│   ├── create_tables.sql
│   ├── kpi_queries.sql
│   ├── cohort_analysis.sql
│   └── retention_analysis.sql
│
├── powerbi
│   └── SaaS_Analytics.pbix
│
├── requirements.txt
└── README.md
```

---

## Skills Demonstrated

- SQL
- Python
- Data Cleaning
- Exploratory Data Analysis
- Machine Learning
- Natural Language Processing
- Customer Segmentation
- Feature Engineering
- Power BI
- Business Intelligence
- Data Visualization

---

## Future Improvements

- Connect to a live SQL database
- Deploy dashboards to Power BI Service
- Integrate an LLM-powered analytics assistant
- Automate data refresh and reporting

---

## Author

Developed as a portfolio project to demonstrate end-to-end Data Analytics, Machine Learning, and Business Intelligence using SQL, Python, and Power BI.
