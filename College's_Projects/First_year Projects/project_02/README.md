&#x09;		**# Monte Carlo Simulation using Google Colab**

---

###### 📌 Project Overview

This project was created as part of my college Extra Activity based on Probability and Statistics.

The objective of this project was to perform a **Monte Carlo Simulation** using Python in Google Colab and compare:

* Theoretical Probability
* Monte Carlo (Experimental) Probability

For this simulation, I selected the experiment of rolling a fair six-sided die multiple times and observing how experimental probabilities approach theoretical probabilities as the number of trials increases.

\---

##### 🎯 Objective of the Simulation



The main objective of this project is to understand how Monte Carlo Simulation works in probability experiments.

The project compares:

* **Theoretical Probability** → Probability calculated mathematically
* **Monte Carlo Probability** → Probability estimated using repeated simulations

By increasing the number of die rolls (10, 50, and 100 throws), we observe that the simulated probabilities become closer to the theoretical probabilities.

\---

##### 🧮 Theoretical Probability

For a fair six-sided die:

* Total possible outcomes = 6
* Favorable outcomes for each face = 1

The theoretical probability formula is:

P(Event) = Favorable Outcomes / Total Outcomes

Therefore:

* ```math
P(each face) = 1/6 = 0.167



The theoretical probabilities remain constant because they are derived mathematically.

🎲 Monte Carlo Simulation

Monte Carlo Simulation estimates probabilities through repeated random experiments.

Steps Performed
Roll a die using Python random generation
Repeat the experiment multiple times
Count occurrences of each face
Calculate experimental probabilities
Compare with theoretical probabilities
Formula Used
P(face)=Occurrencesofface/Totalthrows


📊 Simulation Results
Results for 10 Throws

The probabilities fluctuate significantly due to the small sample size.

Results for 50 Throws

The probabilities begin to stabilize and move closer to theoretical values.

Results for 100 Throws

The Monte Carlo probabilities become much closer to the theoretical probability (0.167).

This demonstrates the Law of Large Numbers, where larger sample sizes produce more accurate approximations.


📈 Key Observations

Small sample sizes create high randomness
Larger simulations reduce fluctuations
Experimental probability approaches theoretical probability over time
Monte Carlo Simulation is useful for approximating probabilities in real-world scenarios


🛠 Technologies Used
Python
Google Colab
NumPy
Random Simulation
Probability Concepts


📂 Project Files
Monte\_Carlo\_Simulation/
│
├── README.md
├── monte\_carlo\_simulation.ipynb
├── Activity\_Question.docx
├── Analysis\_Summary.docx
└── screenshots/


📚 What I Learned

Through this project, I learned:

Basics of Monte Carlo Simulation
Difference between theoretical and experimental probability
Python implementation of probability experiments
Random number generation using NumPy
Importance of sample size in simulations
Working with Google Colab notebooks

✅ Conclusion

This project helped me understand how simulations can be used to estimate probabilities practically.

The experiment clearly showed that:

Theoretical probabilities remain fixed
Experimental probabilities vary initially
Larger numbers of simulations produce more accurate results

This project improved my understanding of probability concepts and Python-based simulations.

👨‍💻 Author

Ayush Rajput
Aspiring Data Analyst \& Data Science Learner

