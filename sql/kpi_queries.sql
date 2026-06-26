-- MRR
SELECT
    SUM(monthly_revenue) AS mrr
FROM subscriptions
WHERE is_churned = 0;

-- ARR
SELECT
    SUM(monthly_revenue) * 12 AS arr
FROM subscriptions
WHERE is_churned = 0;

-- Churn Rate
SELECT
    ROUND(
        100.0 * SUM(is_churned) / COUNT(*),
        2
    ) AS churn_rate
FROM subscriptions;

-- Active Customers
SELECT
    COUNT(*) AS active_customers
FROM subscriptions
WHERE is_churned = 0;

-- Revenue By Plan
SELECT
    plan_type,
    COUNT(*) AS customers,
    SUM(monthly_revenue) AS revenue
FROM subscriptions
GROUP BY plan_type
ORDER BY revenue DESC;

-- Customer Lifetime Value
SELECT
    plan_type,
    ROUND(
        AVG(monthly_revenue) * 12,
        2
    ) AS estimated_clv
FROM subscriptions
GROUP BY plan_type;

-- Average Revenue Per User
SELECT
    ROUND(
        SUM(monthly_revenue) / COUNT(*),
        2
    ) AS arpu
FROM subscriptions;

-- Successful Payments
SELECT
    COUNT(*) AS successful_payments
FROM payments
WHERE payment_status = 'Success';

-- Failed Payments
SELECT
    COUNT(*) AS failed_payments
FROM payments
WHERE payment_status = 'Failed';

-- Average Ticket Resolution Time
SELECT
    ROUND(
        AVG(resolved_date - created_date),
        2
    ) AS avg_resolution_days
FROM support_tickets;