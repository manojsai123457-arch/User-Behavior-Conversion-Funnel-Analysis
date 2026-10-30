
USE user_behavior_analysis;
select * from user_events;
SELECT COUNT(*) FROM user_events;

SELECT event_type, COUNT(*) AS total_events
FROM user_events
GROUP BY event_type;

SELECT COUNT(DISTINCT user_id) AS unique_users
FROM user_events;

SELECT ROUND(SUM(price), 2) AS total_revenue
FROM user_events
WHERE event_type = 'purchase';

SELECT
    ROUND(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS view_pct,
    ROUND(SUM(CASE WHEN event_type = 'cart' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS cart_pct,
    ROUND(SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS purchase_pct
FROM user_events;

SELECT
    ROUND(SUM(CASE WHEN event_type = 'cart' THEN 1 ELSE 0 END) * 100.0 /
          SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 2) AS view_to_cart_rate,
    ROUND(SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 100.0 /
          SUM(CASE WHEN event_type = 'cart' THEN 1 ELSE 0 END), 2) AS cart_to_purchase_rate
FROM user_events;

SELECT
    category_code,
    COUNT(*) AS total_events
FROM user_events
GROUP BY category_code
ORDER BY total_events DESC
LIMIT 10;

SELECT
    brand,
    COUNT(*) AS total_events
FROM user_events
WHERE brand <> 'Unknown'
GROUP BY brand
ORDER BY total_events DESC
LIMIT 10;

SELECT
    COUNT(DISTINCT user_session) AS total_sessions,
    SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) AS view_events,
    SUM(CASE WHEN event_type = 'cart' THEN 1 ELSE 0 END) AS cart_events,
    SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchase_events
FROM user_events;

WITH session_events AS (
    SELECT
        user_session,
        MAX(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) AS has_view,
        MAX(CASE WHEN event_type = 'cart' THEN 1 ELSE 0 END) AS has_cart,
        MAX(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS has_purchase
    FROM user_events
    GROUP BY user_session
)
SELECT
    COUNT(*) AS total_sessions,
    SUM(has_view) AS sessions_with_view,
    SUM(has_cart) AS sessions_with_cart,
    SUM(has_purchase) AS sessions_with_purchase
FROM session_events;

WITH session_order AS (
    SELECT
        user_session,
        MIN(CASE WHEN event_type = 'view' THEN event_time END) AS first_view_time,
        MIN(CASE WHEN event_type = 'cart' THEN event_time END) AS first_cart_time,
        MIN(CASE WHEN event_type = 'purchase' THEN event_time END) AS first_purchase_time
    FROM user_events
    GROUP BY user_session
)
SELECT
    COUNT(*) AS total_sessions,
    SUM(CASE WHEN first_view_time IS NOT NULL THEN 1 ELSE 0 END) AS sessions_with_view,
    SUM(CASE WHEN first_cart_time IS NOT NULL AND first_cart_time > first_view_time THEN 1 ELSE 0 END) AS sessions_view_to_cart,
    SUM(CASE WHEN first_purchase_time IS NOT NULL AND first_purchase_time > first_cart_time THEN 1 ELSE 0 END) AS sessions_cart_to_purchase
FROM session_order;

SELECT category_code, COUNT(*) AS total_events
FROM user_events
GROUP BY category_code
ORDER BY total_events DESC
LIMIT 10;

SELECT brand, COUNT(*) AS total_events
FROM user_events
WHERE brand <> 'Unknown'
GROUP BY brand
ORDER BY total_events DESC
LIMIT 10;

SELECT category_code, ROUND(SUM(price), 2) AS revenue
FROM user_events
WHERE event_type = 'purchase'
GROUP BY category_code
ORDER BY revenue DESC
LIMIT 10;

SELECT brand, ROUND(SUM(price), 2) AS revenue
FROM user_events
WHERE event_type = 'purchase' AND brand <> 'Unknown'
GROUP BY brand
ORDER BY revenue DESC
LIMIT 10;

SELECT category_code, COUNT(DISTINCT user_id) AS unique_users
FROM user_events
GROUP BY category_code
ORDER BY unique_users DESC
LIMIT 10;

SELECT product_id, COUNT(*) AS total_events
FROM user_events
GROUP BY product_id
ORDER BY total_events DESC
LIMIT 10;

SELECT event_type, ROUND(AVG(price), 2) AS avg_price
FROM user_events
GROUP BY event_type;