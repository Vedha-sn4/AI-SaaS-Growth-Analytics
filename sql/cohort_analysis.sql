WITH user_cohorts AS
(
    SELECT
        user_id,
        DATE_TRUNC('month', signup_date) AS cohort_month
    FROM users
),

monthly_activity AS
(
    SELECT
        user_id,
        DATE_TRUNC('month', usage_date) AS activity_month
    FROM feature_usage
)

SELECT
    uc.cohort_month,
    ma.activity_month,
    COUNT(DISTINCT ma.user_id) AS active_users
FROM user_cohorts uc
JOIN monthly_activity ma
    ON uc.user_id = ma.user_id
GROUP BY
    uc.cohort_month,
    ma.activity_month
ORDER BY
    uc.cohort_month,
    ma.activity_month;