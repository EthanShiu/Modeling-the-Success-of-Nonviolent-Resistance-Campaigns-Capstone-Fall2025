#!/usr/bin/env python
# coding: utf-8

# In[81]:


import pandas as pd
import shap
import matplotlib.pyplot as plt
import joblib
import uuid
import os
from pathlib import Path  # This is the line that defines 'Path'

# 1. This is the full path to the FILE: .../app/ui_code.py
current_file = Path(__file__).resolve()

# 2. This is the folder containing the file: .../app/
# We MUST use .parent here to get the directory, not the filename
app_folder = current_file.parent

# 3. This is the project root: .../Modeling-the-Success...Capstone/
PROJECT_ROOT = app_folder.parent

print(f"DEBUG: Project Root is {PROJECT_ROOT}")

# 4. Now the path will be correct: .../Capstone/Data/ui_data.csv
df = pd.read_csv(PROJECT_ROOT / "Data" / "ui_data.csv")
model = joblib.load(PROJECT_ROOT / "models" / "rf_shap_tuned.pkl")
shap_values = joblib.load(PROJECT_ROOT / "models" / "shap_values_class1.pkl")

X = df.drop(columns=["success", "year"])

# In[84]:


# Function to predict probability
def predict_success_probability(user_input_dict):
    input_df = pd.DataFrame([user_input_dict], columns=X.columns)
    prob = model.predict_proba(input_df)[0, 1]
    return float(prob)


# In[85]:


# Function to plot SHAP dependence
# Dependence Plot function for UI
def shap_dependence_plot(main_feature, interaction_feature, shap_values, X):
    try:
        if interaction_feature == "None" or interaction_feature is None:
            interaction_feature = None

        shap.dependence_plot(
            main_feature,
            shap_values,
            X,
            interaction_index=interaction_feature,
            show=False
        )

        # FIX: Handle the case where __file__ is missing
        try:
            current_dir = Path(__file__).resolve().parent
        except NameError:
            # Fallback to current working directory if __file__ is not defined
            current_dir = Path(os.getcwd())
            # If R is running from the root, we might need to go into /app
            if (current_dir / "app").exists():
                current_dir = current_dir / "app"

        fig_name = f"shap_plot_{uuid.uuid4().hex}.png"
        fig_path = str(current_dir / fig_name)

        plt.tight_layout()
        plt.savefig(fig_path)
        plt.close()

        return fig_path
    except Exception as e:
        print("SHAP plot error:", e)
        return None




# In[100]:


# Test Prediction
sample_input = {
    'wdrwl_support': 1.250656e+00,
    'div_class': 1.034801e+00,
    'sec_defect': 7.589216e-01,
    'sdirect': 5.781821e-01,
    'div_ethnicity': 5.513224e-01,
    'camp_backlash': 4.608532e-01,
    'state_defect': 3.873066e-01,
    'camp_support': 2.261295e-01,
    'violent_flank': 2.094405e-01,
    'camp_goals': 1.306134e-01,
    'ab_internat': 6.398306e-02,
    'log_rel_part': 7.229054e-03,
    'media_outreach': 1.450923e-03,
    'total_part': 2.062547e-08,
    'camp_orgs': -3.541489e-02,
    'dom_media': -6.930089e-02,
    'camp_duration': -9.874490e-02,
    'camp_structure': -2.694264e-01,
    'fatalities_range': -2.925996e-01,
    'indiscrim': -8.209170e-01,
}

# Create DataFrame and match columns to model
sample_df = pd.DataFrame([sample_input])
sample_df = sample_df[model.feature_names_in_]

# Predict
prob = model.predict_proba(sample_df)[0, 1]
#print(f"Predicted Probability of Success: {prob:.2%}")


# In[87]:


predict_success_probability(sample_input)


# In[88]:


# Test Shap_dependence_plot
#shap_dependence_plot(main_feature="div_class", shap_values=shap_values, X=X, interaction_feature="state_defect")

