-- Created Table
CREATE TABLE customers (
    customerID VARCHAR(50),
    gender VARCHAR(20),
    SeniorCitizen INT,
    Partner VARCHAR(10),
    Dependents VARCHAR(10),
    tenure INT,
    PhoneService VARCHAR(10),
    MultipleLines VARCHAR(50),
    InternetService VARCHAR(50),
    OnlineSecurity VARCHAR(20),
    OnlineBackup VARCHAR(20),
    DeviceProtection VARCHAR(20),
    TechSupport VARCHAR(20),
    StreamingTV VARCHAR(20),
    StreamingMovies VARCHAR(20),
    Contract VARCHAR(50),
    PaperlessBilling VARCHAR(10),
    PaymentMethod VARCHAR(100),
    MonthlyCharges NUMERIC(10,2),
    TotalCharges VARCHAR(50),
    Churn VARCHAR(10)
);

SELECT * FROM customers;

SELECT COUNT(*) FROM customers;


-- check the null value
SELECT COUNT(*)
FROM customers
WHERE TotalCharges IS NULL
   OR TRIM(TotalCharges) = '';

-- check the unique_customers
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT customerID) AS unique_customers
FROM customers;

--let us do   Excel findings validate from SQL 
SELECT
    Churn,
    COUNT(*) AS customers
FROM customers
GROUP BY Churn;

SELECT
    Contract,
    Churn,
    COUNT(*) AS customers
FROM customers
GROUP BY Contract, Churn
ORDER BY Contract, Churn;


--find the  11 rows 
SELECT
    customerID,
    tenure,
    MonthlyCharges,
    TotalCharges
FROM customers
WHERE TRIM(TotalCharges) = '';

--First Data Cleaning Query
UPDATE customers
SET TotalCharges = '0'
WHERE TRIM(TotalCharges) = '';

--Verify
SELECT COUNT(*)
FROM customers
WHERE TRIM(TotalCharges) = '';
