# User Behavior & Conversion Funnel Analysis

## Project Overview

This project analyzes user clickstream behavior to understand how users move through a product funnel and where they drop off before completing a purchase. It combines SQL, Python, Pandas, Matplotlib, and Power BI to study user sessions, event patterns, category behavior, and revenue concentration.

## Business Problem

A product team wants to understand:

* How users interact with the platform
* Where users drop off in the funnel
* Which products, categories, and brands drive the most revenue
* How clickstream behavior translates into conversion

The goal is to convert raw clickstream data into actionable product insights.

## Tech Stack

* **SQL**
* **Python**
* **Pandas**
* **Matplotlib**
* **Power BI**
* **MySQL**
* **Git / GitHub**

## Dataset

The project uses a public e-commerce clickstream dataset containing:

* `event_time`
* `event_type`
* `product_id`
* `category_id`
* `category_code`
* `brand`
* `price`
* `user_id`
* `user_session`

The dataset was cleaned and sampled for analysis and imported into MySQL for SQL-based exploration.

## Project Workflow

### 1. Data Understanding

Inspected the raw dataset structure, column names, missing values, and event types.

### 2. Data Cleaning

Processed the large dataset using Python and created a clean analysis dataset.

### 3. SQL Analysis

Imported the data into MySQL and analyzed:

* event distribution
* unique users
* total revenue
* category performance
* brand performance
* product activity
* funnel behavior

### 4. Python EDA

Created summary statistics and charts for:

* event type distribution
* top categories
* top brands
* daily trend
* revenue analysis

### 5. Funnel Analysis

Built a funnel analysis to understand:

* view → cart conversion
* cart → purchase conversion
* session-level drop-off behavior

### 6. Power BI Dashboard

Built an interactive dashboard with:

* KPI cards
* funnel visual
* event distribution
* top categories
* top brands
* trend analysis

## Key Insights

* Most activity comes from **product views**
* The biggest drop-off happens between **view → cart**
* Smartphones dominate category activity and revenue
* Apple generates the highest revenue among brands
* A few products drive a large share of activity
* The dataset shows realistic clickstream behavior with strong funnel drop-off

## Folder Structure

```text
User-Behavior-Conversion-Funnel-Analysis/
├── data/
│   ├── raw/
│   └── processed/
├── images/
├── powerbi/
├── python/
├── reports/
├── sql/
├── venv/
├── README.md
└── requirements.txt
```

## How to Run

### Python

Run the Python scripts from the `python/` folder.

### MySQL

Import the cleaned analysis dataset into MySQL and run the SQL queries stored in:

```text
sql/schema.sql
sql/analysis_queries.sql
```

### Power BI

Open the dashboard file from:

```text
powerbi/User_Behavior_Conversion_Funnel_Analysis.pbix
```

## Output Files

### Python charts

Saved in:

```text
images/
```

### Funnel summary

Saved in:

```text
reports/funnel_summary.csv
```

### Power BI dashboard

Saved in:

```text
powerbi/User_Behavior_Conversion_Funnel_Analysis.pbix
```

## Dashboard Screenshots

Add the dashboard screenshots here:

* `images/dashboard_1.png`
* `images/dashboard_2.png`

## Conclusion

This project demonstrates a complete analytics workflow from raw clickstream data to SQL analysis, Python EDA, funnel analysis, and interactive dashboarding. It is suitable for Product Analyst, Data Analyst, BI Analyst, and SQL-focused interview roles.
