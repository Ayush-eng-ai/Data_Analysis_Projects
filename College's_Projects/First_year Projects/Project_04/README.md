# Distribution Fitting Analysis using Student Graduation Dataset

## 📌 Project Overview

This project was completed as part of my college Extra Activity based on Probability Distribution and Statistical Modeling.

The objective of this project was to:
- Analyze a student graduation dataset
- Approximate the data using a probability distribution
- Compare theoretical and experimental distributions
- Understand how Binomial Distribution models real-world events

The dataset contains information about the number of years students took to graduate.

---

## 🎯 Objective

The main objective of this project was to:
- Fit a probability distribution to real-world educational data
- Calculate probabilities from the dataset
- Model the data using Binomial Distribution
- Compare theoretical probabilities with experimental probabilities
- Visualize the distribution behavior using graphs

---

## 📂 Dataset Information

### Dataset Name
Parental Dataset

### Total Students
1000 Students

### Variable Used
`Years to Graduate`

The dataset records the number of years students took to complete graduation.

---

## 📊 Dataset Summary

| Years to Graduate | Number of Students |
|---|---|
| 3 | 112 |
| 4 | 327 |
| 5 | 257 |
| 6 | 164 |
| 7 | 69 |
| 8 | 49 |
| 9 | 18 |
| 10 | 2 |

---

## 📈 Probability Calculation

The probability for each graduation year was calculated using:

```math
P(X=x) = Number\ of\ Students / Total\ Students





Example

For students graduating in exactly 7 years:

P(X=7)=69/1000=0.069
🎲 Binomial Distribution Modeling

A Binomial Distribution model was created using:

Success Event → Student takes exactly 7 years to graduate
Failure Event → Any other graduation duration
Parameters Used
Parameter	Value
Number of Trials (n)	10
Probability of Success (p)	0.07
Probability of Failure (q)	0.93
📉 Theoretical Distribution

The theoretical Binomial probabilities were calculated for:

K=0 to 10

where:

K = Number of students taking exactly 7 years

Theoretical probabilities decrease as the number of successes increases.

📊 Experimental Distribution

An experimental distribution was created using observed probability values from the dataset.

The comparison between:

Theoretical Distribution
Experimental Distribution

helped analyze how closely the real-world data follows the Binomial model.

📈 Graphical Analysis

Graphs were created to compare:

Theoretical Distribution
Experimental Distribution
Observations
Theoretical and experimental probabilities showed similar trends
Small differences occurred due to randomness in real-world observations
Lower probability events had larger fluctuations

The visualization helped understand:

Probability behavior
Distribution fitting
Experimental variation
📚 Statistical Concepts Used

This project involved:

Probability Distribution
Binomial Distribution
Discrete Random Variables
Experimental Probability
Theoretical Probability
Distribution Comparison
🛠 Tools & Technologies Used
Google Sheets
Google Docs
Python
Google Colab
Statistical Calculations
Probability Modeling
Graph Visualization
📂 Project Files
Distribution_Fitting_Analysis/
│
├── README.md
├── graduation_dataset.xlsx
├── distribution_analysis.ipynb
├── Analysis_Report.docx
├── Activity_Question.docx
└── screenshots/
📚 What I Learned

Through this project, I learned:

How to fit probability distributions to data
Difference between theoretical and experimental probability
Application of Binomial Distribution
Modeling real-world events using statistics
Probability visualization techniques
Interpretation of statistical graphs
✅ Conclusion

This project provided practical experience in probability distribution fitting and statistical modeling.

The analysis demonstrated that:

Real-world educational data can be approximated using probability distributions
Experimental distributions may vary slightly from theoretical models
Binomial Distribution is useful for modeling discrete events

Overall, this project improved my understanding of probability theory, distribution fitting, and statistical analysis.

👨‍💻 Author

Ayush Rajput
Aspiring Data Analyst & Data Science Learner