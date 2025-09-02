#!/usr/bin/env python
# coding: utf-8

# In[81]:


import pandas as pd
import shap
import matplotlib.pyplot as plt
import joblib
import uuid


# In[82]:


# Load dataset and model
df = pd.read_csv("ui_data.csv")  # this includes 'success' column if needed
model = joblib.load("rf_shap_tuned.pkl")
X = df.drop(columns=["success", "year"])


# In[83]:


# Load SHAP values (optional, only if precomputed)
shap_values = joblib.load("shap_values_class1.pkl")


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

        fig_path = f"shap_plot_{uuid.uuid4().hex}.png"
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

