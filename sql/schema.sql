CREATE DATABASE user_behavior_analysis;
USE user_behavior_analysis;

CREATE TABLE user_events (
    event_time DATETIME,
    event_type VARCHAR(20),
    product_id BIGINT,
    category_id BIGINT,
    category_code VARCHAR(255),
    brand VARCHAR(255),
    price DECIMAL(10,2),
    user_id BIGINT,
    user_session VARCHAR(100)
);
