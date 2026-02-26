#  J.P. Morgan Chase & Co. - Quantitative Research Simulation

This folder contains my technical implementation for the **Quantitative Researcher** job simulation at J.P. Morgan Chase. The project focuses on credit risk modeling using statistical approaches and algorithmic optimization.

##  Project Objective
The primary goal of this project was to understand how mathematical fundamentals (Calculus and Statistics) serve as the backbone for precise data analysis in global investment banking. This experience is a crucial part of building my foundational skills for future research in **NeuroAI**.

## File Structure
- **`JPMorgan_Task4_Ferry.py`**: Main Python script featuring Logistic Regression modeling, Expected Loss calculations, and data visualization.
- **`JPMC_Task 4_Example Answer.docx`**: JPMC’s reference solution utilizing **Dynamic Programming** and **Maximum Likelihood Estimation**. I performed a comparative study of these methods to understand stochastic optimization.
- **`Task 3 and 4_Loan_Data.csv`**: The dataset containing borrower profiles (FICO Scores, Income, Debt, etc.).
- **`JPMC_Certificate.pdf`**: Official certificate of completion.

## 🛠️ Technical & Mathematical Implementation

### 1. Credit Risk Modeling (Logistic Regression)
I developed a binary classification model to predict the *Probability of Default* (PD).
- **Accuracy:** 99.7% on the test set.
- **Concept:** Implemented the **Sigmoid function** to map financial inputs into a probability space $[0, 1]$.
- **Risk Drivers:** Identified that `credit_lines_outstanding` has the strongest positive correlation with default risk.

### 2. Algorithmic Optimization (FICO Bucketing)
By analyzing the provided *Example Answer*, I explored the optimization of FICO score segmentation.
- **Methodology:** Comparative study on using **Dynamic Programming** to maximize the **Log-Likelihood** (Bernoulli Distribution).
- **Goal:** Finding optimal cut-off points that minimize intra-group variance and maximize inter-group risk differentiation.

### 3. Risk Metrics Calculation
Estimated potential financial losses using the *Expected Loss* (EL) framework:
$$EL = PD \times LGD \times EAD$$
*Where PD = Prob. of Default, LGD = Loss Given Default (60%), and EAD = Exposure at Default.*

---
*Completed on January 20, 2026, as part of an academic portfolio*
