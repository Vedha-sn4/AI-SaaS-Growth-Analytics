-- Retention By Industry

SELECT
    u.industry,
    COUNT(*) AS total_users,

    SUM(
        CASE
            WHEN s.is_churned = 0 THEN 1
            ELSE 0
        END
    ) AS retained_users,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN s.is_churned = 0 THEN 1
                ELSE 0
            END
        ) /
        COUNT(*),
        2
    ) AS retention_rate

FROM users u
JOIN subscriptions s
ON u.user_id = s.user_id

GROUP BY u.industry
ORDER BY retention_rate DESC;


-- Retention By Company Size

SELECT
    u.company_size,

    COUNT(*) AS total_users,

    SUM(
        CASE
            WHEN s.is_churned = 0 THEN 1
            ELSE 0
        END
    ) AS retained_users,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN s.is_churned = 0 THEN 1
                ELSE 0
            END
        ) /
        COUNT(*),
        2
    ) AS retention_rate

FROM users u
JOIN subscriptions s
ON u.user_id = s.user_id

GROUP BY u.company_size
ORDER BY retention_rate DESC;


-- Retention By Plan

SELECT
    plan_type,

    COUNT(*) AS customers,

    SUM(
        CASE
            WHEN is_churned = 0 THEN 1
            ELSE 0
        END
    ) AS retained_customers,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN is_churned = 0 THEN 1
                ELSE 0
            END
        ) /
        COUNT(*),
        2
    ) AS retention_rate

FROM subscriptions

GROUP BY plan_type
ORDER BY retention_rate DESC;