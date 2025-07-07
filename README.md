# AI in Software Engineering – Week 4 Assignment

**Theme: Building Intelligent Software Solutions**

---

## Overview

This repository contains the full implementation and analysis for the Week 4 assignment titled **"AI in Software Engineering"**, developed under the Power Learn Project (PLP). The project demonstrates how AI can automate software development tasks, improve decision-making, and ensure ethical practices.

---

## Contents

- `task1_code_completion.py`: Demonstrates AI-powered code suggestion using GitHub Copilot.
- `task2_selenium_login_test.py`: Automated login testing using Selenium.
- `task3_predictive_analytics.ipynb`: Predictive analytics using Random Forest on the Breast Cancer dataset.
- `README.md`: This file.

---

## Part 1: Theoretical Analysis

### Q1: AI Code Generation Tools
Tools like GitHub Copilot reduce development time by auto-generating code based on context, improving efficiency. However, they require oversight due to occasional errors or security issues.

### Q2: Supervised vs. Unsupervised Learning for Bug Detection
- **Supervised**: Predict bugs using labeled training data.
- **Unsupervised**: Detect anomalies without labels, useful for unknown issues.

### Q3: Bias in UX Personalization
Bias in training data can lead to unfair treatment of user segments. Bias mitigation ensures inclusive and ethical AI systems.

### Case Study: AIOps in DevOps
AIOps enhances deployment pipelines by:
1. Predicting and avoiding deployment failures.
2. Automating resolution during deployments.

---

## Part 2: Practical Implementation

### Task 1: AI-Powered Code Completion
**Tool**: GitHub Copilot  
Wrote a function to sort dictionaries by key. Compared Copilot’s code with a manually written version.  
Copilot’s version was more concise, readable, and efficient.

➡️ File: `task1_code_completion.py`

### Task 2: Automated Testing with Selenium
**Tool**: Selenium IDE  
Automated a login test with valid and invalid credentials. AI-based tools improve test coverage and adaptability.

➡️ File: `task2_selenium_login_test.py`

### Task 3: Predictive Analytics for Resource Allocation
**Tool**: Scikit-learn (Random Forest)  
Used the Breast Cancer dataset to classify issue priority. Evaluated the model using accuracy and F1-score. Included visualizations.

➡️ File: `task3_predictive_analytics.ipynb`

---

## Part 3: Ethical Reflection

### Bias in AI Models
AI systems may be biased if datasets underrepresent specific groups. In this project, tools like IBM AI Fairness 360 could help detect and correct bias.

---

## Bonus Task: Innovation Challenge

**Tool Idea**: `DocSmartAI`  
Generates inline documentation and READMEs automatically using NLP.

- **Input**: Source code  
- **Output**: Markdown docs  
- **Impact**: Saves time and improves code maintainability

---

## How to Run the Code

### Requirements
```bash
pip install pandas numpy scikit-learn matplotlib seaborn selenium notebook
