DROP TABLE IF EXISTS feature_usage;
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS support_tickets;
DROP TABLE IF EXISTS subscriptions;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    signup_date DATE,
    country VARCHAR(100),
    industry VARCHAR(100),
    company_size VARCHAR(50)
);

CREATE TABLE subscriptions (
    subscription_id INT PRIMARY KEY,
    user_id INT,
    plan_type VARCHAR(50),
    monthly_revenue NUMERIC(10,2),
    subscription_start DATE,
    is_churned INT
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    user_id INT,
    payment_date DATE,
    amount NUMERIC(10,2),
    payment_status VARCHAR(20)
);

CREATE TABLE feature_usage (
    usage_id INT PRIMARY KEY,
    user_id INT,
    feature_name VARCHAR(100),
    usage_count INT,
    usage_date DATE
);

CREATE TABLE support_tickets (
    ticket_id INT PRIMARY KEY,
    user_id INT,
    ticket_text TEXT,
    created_date DATE,
    resolved_date DATE
);