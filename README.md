Since your app is a Capstone project, the README needs to be both a technical guide for developers and a professional showcase for recruiters.

Here is a structured, "GitHub-ready" README for your repository.

Modeling the Success of Nonviolent Resistance Campaigns
A data science capstone project exploring the drivers of successful nonviolent resistance. This project features an interactive R Shiny dashboard that interfaces with Python to provide real-time predictive modeling and SHAP (SHapley Additive exPlanations) interpretability.

🚀 Overview
This application allows users to simulate the conditions of a resistance campaign and predict its likelihood of success. By leveraging a Random Forest model, the app provides:

Predictive Success Probability: Instant feedback on campaign outcomes based on historical patterns.

SHAP Interpretability: Dynamic dependence plots to visualize how specific features (e.g., class diversity, participation levels) influence the model's decision.

📂 Project Structure
Plaintext
Capstone-Project/
├── Data/
│   └── ui_data.csv             # Processed dataset for the UI
├── models/
│   ├── rf_shap_tuned.pkl       # Trained Random Forest model
│   └── shap_values_class1.pkl  # Pre-computed SHAP values
├── app/
│   ├── app.R                   # R Shiny frontend logic
│   └── ui_code.py              # Python backend for SHAP & predictions
├── README.md                   # Project documentation
└── .Rproj                      # R Project file (Entry point)
🛠️ Installation & Setup
1. Prerequisites
Ensure you have the following installed:

R (4.0+) and RStudio

Python (3.9+) with Anaconda or Miniconda

2. Environment Setup
Create a conda environment to handle the Python dependencies:

Bash
conda create -n capstone_env python=3.12
conda activate capstone_env
pip install pandas shap matplotlib joblib
3. R Dependencies
Open RStudio and install the necessary R packages:

R
install.packages(c("shiny", "reticulate", "shinythemes", "ggplot2"))
🖥️ Running the App
Open the .Rproj file in RStudio.

Open app/app.R.

Ensure the use_python() path in app.R points to your capstone_env location.

Click Run App.

📊 Methodology
Model: Random Forest Classifier, tuned for recall to identify key success drivers.

Explainability: We utilize SHAP dependence plots to illustrate the non-linear relationships between variables, such as the interaction between Relative Participation and Class Diversity.

Integration: The app uses the reticulate library to pass data seamlessly between R (for UI reactivity) and Python (for ML computation).

👤 Author
Ethan Shiu

GitHub: @ethanshiu

Capstone Project - 2026