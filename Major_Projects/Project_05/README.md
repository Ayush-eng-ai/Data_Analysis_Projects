# 🎯 Project 05: AI-Powered Customer Churn Analysis

## 📊 Project Overview

This is a comprehensive **Customer Churn Analysis** project using **Telco Customer Churn Dataset**. The project demonstrates end-to-end data analysis workflow combining **Python (Pandas)**, **SQL**, and **Tableau** to identify key factors driving customer churn and provide actionable business insights.

**Dataset:** Telco Customer Churn (7,043 customers)  
**Objective:** Predict and analyze customer churn patterns to reduce customer attrition

---

## 📁 Project Structure

```
Project_05/
│
└── AI-Powered Customer Churn Analysis/
    ├── README.md (this file)
    ├── Customer_Churn_Analysis.ipynb
    ├── churn_analysis_queries.sql
    ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
    ├── AI_Powered_Customer_Churn_Analysis.twbx.twbx
    └── ~AI_Powered_Customer_Churn_Analysis.twbx__5352.twbr
```

---

## 📋 Files Description

### 1. **Customer_Churn_Analysis.ipynb** 📘
Jupyter Notebook containing the complete Python analysis pipeline.

**Key Sections:**
- **Data Loading & Exploration:** Load CSV and inspect dataset structure
- **Data Cleaning:** Handle missing values in TotalCharges column (11 null values found)
- **Exploratory Data Analysis (EDA):**
  - Average Tenure by Churn Status: 37.57 months (No) vs 17.98 months (Yes)
  - Average Monthly Charges by Churn: $61.27 (No) vs $74.44 (Yes)
  - Average Total Charges by Churn: $2,549.91 (No) vs $1,531.80 (Yes)
- **Payment Method Analysis:** Electronic check shows highest churn rate
- **Visualizations:** Bar charts for key metrics

**Technical Stack:**
- pandas, matplotlib
- Data types: 21 columns (4 numerical, 17 categorical)
- Total records: 7,043 customers

---

### 2. **churn_analysis_queries.sql** 🗄️
SQL queries for data validation and advanced analysis.

**Key Queries:**
```sql
-- Table Creation: customers table with 20 attributes
-- Data Validation: Check for null/empty values
-- Quality Checks: 11 rows found with empty TotalCharges
-- Churn Distribution: Analysis by Contract type
-- Data Cleaning: SET TotalCharges = '0' for empty values
```

**Database Operations:**
- Create customers table schema
- Validate data integrity
- Count unique customers: 7,043
- Identify data quality issues
- Clean and standardize data

---

### 3. **WA_Fn-UseC_-Telco-Customer-Churn.csv** 📊
Raw dataset with 7,043 customer records.

**Key Attributes (21 columns):**

| Category | Attributes |
|----------|-----------|
| **Demographics** | customerID, gender, SeniorCitizen, Partner, Dependents |
| **Service Usage** | tenure, PhoneService, MultipleLines, InternetService |
| **Add-on Services** | OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies |
| **Contract & Billing** | Contract, PaperlessBilling, PaymentMethod |
| **Financial** | MonthlyCharges, TotalCharges |
| **Target Variable** | Churn (Yes/No) |

**Data Quality:**
- Total Records: 7,043
- Missing Values: 11 rows in TotalCharges (empty strings)
- Tenure Range: 0-72 months
- Monthly Charges Range: $18.25 - $118.75

---

### 4. **AI_Powered_Customer_Churn_Analysis.twbx.twbx** 📈
Interactive Tableau Dashboard for visual analytics and KPI tracking.

**Dashboard Components:**

#### **KPI Cards:**
- **Churn Rate:** Percentage of customers who churned
- **Churn Customers:** Count of churned customers
- **Avg Monthly Charges:** Average monthly spending
- **Average Tenure by Churn:** Comparison of customer retention period

#### **Visualizations:**
1. **Churn Rate Trend** - Overall churn percentage metric
2. **Average Tenure by Churn** - Bar chart comparison
3. **Avg Monthly Charges** - KPI card showing average charges
4. **Contract vs Churn** - Stacked bar chart showing churn by contract type
5. **Internet Service vs Churn** - Distribution across service types
6. **Churn Customers** - Count of churned customers

**Interactive Features:**
- Filter by multiple dimensions
- Drill-down capabilities
- Cross-sheet filtering
- Real-time data updates

---

## 🔍 Key Findings & Insights

### Churn Analysis Results:

| Metric | No Churn | Churned | Finding |
|--------|----------|---------|---------|
| **Avg Tenure** | 37.57 months | 17.98 months | Churned customers leave ~2x faster ⚠️ |
| **Avg Monthly Charges** | $61.27 | $74.44 | Higher charges correlate with churn ⚠️ |
| **Avg Total Charges** | $2,549.91 | $1,531.80 | Lower lifetime value for churned customers |
| **Payment Method** | Bank Transfer/Credit Card | Electronic Check | Electronic check: 45% churn rate (highest) ⚠️ |

### Key Risk Factors:
1. **Electronic Check Payment:** Highest churn rate (45%)
2. **High Monthly Charges:** Customers paying $74.44+ are more likely to churn
3. **Short Tenure:** New customers (< 18 months) are at higher risk
4. **Month-to-Month Contracts:** More flexible but higher churn risk
5. **Fiber Optic Internet:** Higher churn rate than DSL

---

## 🛠️ Technologies & Tools Used

| Tool | Purpose | Usage |
|------|---------|-------|
| **Python** | Data Analysis & EDA | Cleaning, transformation, analysis |
| **Pandas** | Data Manipulation | Loading, filtering, grouping data |
| **Matplotlib** | Visualization | Charts and visualizations |
| **SQL** | Data Validation | Query, validate, and clean data |
| **Tableau** | Interactive Dashboard | Visual analytics and KPIs |
| **Jupyter Notebook** | Code Documentation | Interactive analysis environment |

---

## 📊 Data Quality & Cleaning

### Issues Identified:
1. **Missing Values:** 11 rows with empty TotalCharges (string format)
2. **Data Type Issues:** TotalCharges stored as string instead of numeric
3. **Inconsistencies:** Standardized missing values to 0

### Cleaning Steps:
```python
# Convert TotalCharges to numeric (coerce errors to NaN)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Fill missing values with 0
df['TotalCharges'] = df['TotalCharges'].fillna(0)

# Result: All 7,043 rows now have valid data
```

---

## 💡 Business Recommendations

### High Priority Actions:
1. **Improve Payment Methods:**
   - Encourage automatic payments (bank transfer/credit card)
   - Reduce incentives for electronic check method
   - Target: Reduce electronic check usage by 50%

2. **Price Optimization:**
   - Review pricing for customers paying > $74/month
   - Introduce loyalty discounts for long-term customers
   - Target: Reduce monthly charges churn by 30%

3. **Contract Strategy:**
   - Promote long-term contracts (1-2 years)
   - Offer incentives for contract commitment
   - Target: Increase 2-year contract adoption by 25%

4. **Early Intervention:**
   - Monitor new customers (< 6 months tenure)
   - Implement onboarding and support programs
   - Target: Reduce first-year churn by 20%

5. **Service Quality:**
   - Review Fiber Optic internet service quality
   - Improve tech support for high-risk segments
   - Add complementary services (security, backup)

---

## 📈 Success Metrics

- **Overall Churn Rate:** Track monthly churn percentage
- **Payment Method Distribution:** Monitor shift from electronic check
- **Average Tenure:** Increase for churned segment
- **Customer Lifetime Value:** Improve through retention
- **Contract Adoption:** Increase long-term contract penetration

---

## 🚀 How to Use This Project

### View the Analysis:
1. **Interactive Dashboard:**
   - Open `AI_Powered_Customer_Churn_Analysis.twbx.twbx` in Tableau Desktop
   - Explore KPIs and drill-down visualizations

2. **Python Notebook:**
   - Open `Customer_Churn_Analysis.ipynb` in Jupyter
   - Run cells sequentially for step-by-step analysis

3. **SQL Queries:**
   - Execute `churn_analysis_queries.sql` in your database
   - Validate findings using database queries

### Reproduce the Analysis:
```bash
# Load the CSV
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Clean data
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(0, inplace=True)

# Analyze churn patterns
df.groupby('Churn').agg({
    'tenure': 'mean',
    'MonthlyCharges': 'mean',
    'TotalCharges': 'mean'
})
```

---

## 📊 Dataset Statistics

| Statistic | Value |
|-----------|-------|
| **Total Records** | 7,043 |
| **Total Columns** | 21 |
| **Churn Rate** | ~26.5% |
| **Tenure (Average)** | 32.37 months |
| **Monthly Charges (Avg)** | $64.76 |
| **Total Charges (Avg)** | $2,279.73 |
| **Data Quality Issues Found** | 11 rows (0.16%) |

---

## 🎓 Learning Outcomes

This project demonstrates:

✅ **Data Cleaning & Preprocessing** - Handle missing/invalid data  
✅ **Exploratory Data Analysis (EDA)** - Identify patterns and trends  
✅ **Statistical Analysis** - Compare segments and metrics  
✅ **SQL Querying** - Database validation and analysis  
✅ **Data Visualization** - Create meaningful dashboards  
✅ **Business Intelligence** - Convert data to actionable insights  
✅ **Python Data Science** - Use pandas for data manipulation  
✅ **Tableau Dashboard Development** - Interactive analytics  

---

## 🔗 Project Links

- **GitHub:** [Data_Analysis_Projects](https://github.com/Ayush-eng-ai/Data_Analysis_Projects)
- **Dataset Source:** Telco Customer Churn (Public Dataset)

---

## 📝 Project Metadata

| Field | Value |
|-------|-------|
| **Project Name** | AI-Powered Customer Churn Analysis |
| **Project Type** | End-to-End Data Analysis |
| **Skills Demonstrated** | Python, SQL, Tableau, EDA |
| **Dataset Size** | 7,043 records × 21 columns |
| **Analysis Date** | 2026 |
| **Status** | ✅ Complete |

---

## 👨‍💻 Author

**Created by:** Ayush  
**Repository:** [Data_Analysis_Projects](https://github.com/Ayush-eng-ai/Data_Analysis_Projects)  
**Last Updated:** June 2026

---

**Note:** This project serves as a complete example of how to approach a real-world customer churn problem using modern data analysis tools and techniques. The insights derived can be directly applied to business strategy and customer retention initiatives.

---

**Happy Analyzing! 📊✨**
