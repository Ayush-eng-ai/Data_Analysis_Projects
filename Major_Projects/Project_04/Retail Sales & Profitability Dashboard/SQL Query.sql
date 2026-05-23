CREATE TABLE orders (
    row_id INT,
    order_id VARCHAR(50),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    customer_id VARCHAR(50),
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    country VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    region VARCHAR(50),
    product_id VARCHAR(50),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name TEXT,
    sales NUMERIC,
    quantity INT,
    discount NUMERIC,
    profit NUMERIC
);

SELECT * FROM orders;

DROP TABLE orders; --if error relation already exists
-- then run  this command and  create second time run  and  successfully  running 


SELECT COUNT(*) FROM orders; --  for checking rows

SELECT * FROM orders
LIMIT 10;

--Null valuse check
SELECT * 
FROM orders
WHERE sales IS NULL
	OR profit IS NULL;

/* Date Range Check */
SELECT
MIN(order_date),
MAX(order_date)
FROM orders;

--Unique Regions
SELECT DISTINCT region
FROM orders;

-- Total Sales and Profit
/* 
SUM(sales)-> Saari sales add karta hai
SUM(profit)-> Saara profit add karta hai
ROUND(...,2)-> 2 decimal places tak
*/
SELECT 
ROUND(SUM(sales),2) AS total_sales,
ROUND(SUM(profit),2) AS total_profit
FROM orders;

-- Profit Margin
/*
Formula
Profit Margin % = Profit ÷ Sales × 100-> Ye batata hai:
Har ₹100 sale pe kitna profit

Example:
10% margin
Means ₹100 sale pe ₹10 profit
*/
SELECT 
ROUND((SUM(profit)/SUM(sales))*100,2) AS profit_margin
FROM orders;

-- Region-wise Performance
/*
Region-wise compare:
-- Kaun best?
-- Kaun weak?
*/


-- Category Performance
/*
Why?
Har category equal profitable nahi hoti.
High sales ≠ high profit
Ye bahut important business insight hota hai.
*/
SELECT
category,
ROUND(SUM(sales),2) AS sales,
ROUND(SUM(profit),2) AS profit
FROM orders
GROUP BY category
ORDER BY profit DESC;

-- Region Deep Analysis
/*
Ab sirf profit nahi.
Profit efficiency dekhenge.
High sales but low margin possible.
*/
SELECT
region,
ROUND(SUM(sales),2) AS sales,
ROUND(SUM(profit),2) AS profit,
ROUND((SUM(profit)/SUM(sales))*100,2) AS profit_margin
FROM orders
GROUP BY region
ORDER BY profit_margin DESC;


-- Furniture Breakdown
/* 
Furniture category weak hai.
Ab identify karenge exact culprit.
Example:
Maybe Tables losses de rahe.
*/
SELECT
sub_category,
ROUND(SUM(sales),2) AS sales,
ROUND(SUM(profit),2) AS profit
FROM orders
WHERE category = 'Furniture'
GROUP BY sub_category
ORDER BY profit ASC;


-- Discount Impact
/*
Discount badhne pe profit gir raha ya nahi.
Agar haan → clear recommendation.
*/
SELECT
discount,
ROUND(AVG(profit),2) AS avg_profit
FROM orders
GROUP BY discount
ORDER BY discount;

-- Monthly Sales Trend
/*
Power BI line chart ke liye.
	-- Trend dikhega:
	-- Growth
	-- Seasonality
	-- Peaks
*/
SELECT
DATE_TRUNC('month', order_date) AS month,
ROUND(SUM(sales),2) AS sales
FROM orders
GROUP BY month
ORDER BY month;

-- Top 10 Products
-- Dashboard me top-performing products.
SELECT
product_name,
ROUND(SUM(sales),2) AS sales
FROM orders
GROUP BY product_name
ORDER BY sales DESC-
LIMIT 10;

-- Segment Analysis
/*
Kaunsa customer segment best hai.
Usually:
		* Consumer
		* Corporate
		* Home Office
*/
SELECT
segment,
ROUND(SUM(sales),2) AS sales,
ROUND(SUM(profit),2) AS profit
FROM orders
GROUP BY segment
ORDER BY profit DESC;