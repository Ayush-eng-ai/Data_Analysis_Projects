# Central Limit Theorem (CLT) Simulation using Height-Weight Dataset

## 📌 Project Overview

This project was completed as part of my college Extra Activity for Statistics and Probability.

The objective of this project was to demonstrate and verify the **Central Limit Theorem (CLT)** using the Height data from the Weight-Height dataset.

The project involved:
- Population analysis
- Random sampling
- Sampling distributions
- Histograms
- Comparison of sample means and sums
- Verification of CLT for different sample sizes

This simulation study helped in understanding how sampling distributions behave as sample size increases.

---

## 🎯 Objective

The main objective of this project was to:
- Understand the Central Limit Theorem
- Perform simulation using real-world height data
- Compare population statistics with sampling statistics
- Observe how sample means become normally distributed
- Validate CLT for both:
  - Sample Means
  - Sample Sums

---

## 📚 What is Central Limit Theorem (CLT)?

The Central Limit Theorem states that:

> For a population with finite mean and finite standard deviation, the distribution of sample means approaches a normal distribution as the sample size increases.

### Case I: Sample Mean

```math
(\bar{X}-\mu)/(\sigma/\sqrt{n}) \rightarrow N(0,1)
\
<!--

``` Case II: Sample Sum

(Y−nμ)/(σ squrt(n))→N(0,1)

where:

μ = Population Mean
σ = Population Standard Deviation
n = Sample Size


📂 Dataset Information
Dataset Used

Weight-Height Dataset

Variables Present
    Gender
    Height
    Weight
Variable Selected for CLT

    Height

The Height column was used to perform all statistical simulations and sampling analysis.

📊 Population Statistics

The following population statistics were calculated:

    Population Mean
    Population Standard Deviation

A histogram of the population data was also plotted to visualize the original distribution.

🎲 Sampling Process

Multiple sample sizes were selected:

n = 5, 10, 30, 50, 100

For each sample size:

    100 random samples were generated
    Sample means were calculated
    Sample sums were calculated
    Histograms were plotted


📈 CLT Analysis for Sample Means

For each sample size:

    Distribution of sample means was analyzed
    Mean of sample means was computed
    Standard deviation of sample means was computed

Observations
As sample size increased, the sampling distribution became more normal
Sample means moved closer to the population mean
Variability reduced for larger sample sizes
📉 CLT Analysis for Sample Sums

The CLT procedure was repeated for:

                Y = X1​ + X2 + X3 + ... + Xn
	​

Observations
    Distribution of sums also approached normality
    Larger sample sizes produced smoother distributions
    Standardized sums followed the CLT behavior


📊 Histogram Analysis

Histograms were used to visualize:

Population distribution
Distribution of sample means
Distribution of sample sums
Key Insight

As the sample size increased:

Histograms became more bell-shaped
Distribution approached a normal distribution

This visually verified the Central Limit Theorem.

📈 Final Comparison

Comparisons were made between:

Population Mean vs Sample Mean
Population Standard Deviation vs Sample Standard Deviation
Different sample sizes

The results confirmed:

Sample mean approaches population mean
Standard deviation decreases as sample size increases
🛠 Tools & Technologies Used
Python
Google Colab
NumPy
Pandas
Matplotlib
Excel
Statistical Simulation


📂 Project Files
Central_Limit_Theorem_Simulation/
│
├── README.md
├── Weight-Height.xlsx
├── clt_simulation.ipynb
├── Analysis_Report.docx
├── Activity_Question.docx
└── screenshots/


📚 What I Learned

Through this project, I learned:

Practical implementation of Central Limit Theorem
Random sampling techniques
Sampling distributions
Difference between population and sample statistics
Importance of sample size
Statistical visualization using histograms
Simulation-based probability analysis


✅ Conclusion

This project successfully demonstrated the Central Limit Theorem using Height data from the Weight-Height dataset.

The simulation showed that:

Sampling distributions become approximately normal as sample size increases
Sample means converge toward the population mean
Variability decreases with larger sample sizes

The project improved my understanding of probability theory, statistical simulations, and sampling distributions.

👨‍💻 Author

Ayush Rajput
Aspiring Data Analyst & Data Science Learner -->