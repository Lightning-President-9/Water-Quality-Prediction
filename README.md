# Water Quality Prediction

This project analyzes and predicts water quality using historical data collected from monitoring stations across Punjab, India (2000–2021). It aims to evaluate environmental health based on several key parameters and build machine learning models for predictive analytics.

## Dataset Description

**File**: [PB_All_2000_2021.csv](https://github.com/Lightning-President-9/Water-Quality-Prediction/blob/main/PB_All_2000_2021.csv)  
This dataset contains water quality measurements from various monitoring stations across Punjab, India. Parameters include:

- **NH₄ (Ammonium)** – indicator of organic pollution
- **BSK5 (BOD₅)** – biochemical oxygen demand
- **Suspended Solids** – affects water clarity and aquatic life
- **O₂ (Dissolved Oxygen)** – essential for aquatic organisms
- **NO₃ (Nitrate)**, **NO₂ (Nitrite)** – nitrogen compounds from sewage and fertilizers
- **SO₄ (Sulfate)** – found in industrial runoff
- **PO₄ (Phosphate)** – causes algal blooms
- **Cl (Chloride)** – affects water salinity

> Refer to [Parameters_WQM_RMS.pdf](https://github.com/Lightning-President-9/Water-Quality-Prediction/blob/main/Parameters_WQM_RMS.pdf) for environmental significance and accepted limits of each parameter.

## Week 1 - Data Preprocessing and Visualization

**Notebook**: [Water_Quality_Prediction.ipynb]([Water_Quality_Prediction.ipynb](https://github.com/Lightning-President-9/Water-Quality-Prediction/blob/main/Week_1/Water_Quality_Prediction.ipynb))

In this first week, we:
- Imported and explored the dataset
- Checked for missing/null values
- Converted necessary columns to datetime format
- Analyzed parameter distributions across districts
