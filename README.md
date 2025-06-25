# Water Quality Prediction

This project analyzes and predicts water quality using historical data collected from monitoring stations. It aims to evaluate environmental health based on several key parameters and build machine learning models for predictive analytics.

## Dataset Description

**File**: [PB_All_2000_2021.csv](https://github.com/Lightning-President-9/Water-Quality-Prediction/blob/main/PB_All_2000_2021.csv)  
This dataset contains water quality measurements from various monitoring stations. Parameters include:

- **NH₄ (Ammonium)** – indicator of organic pollution
- **BSK5 (BOD₅)** – biochemical oxygen demand
- **Suspended Solids** – affects water clarity and aquatic life
- **O₂ (Dissolved Oxygen)** – essential for aquatic organisms
- **NO₃ (Nitrate)**, **NO₂ (Nitrite)** – nitrogen compounds from sewage and fertilizers
- **SO₄ (Sulfate)** – found in industrial runoff
- **PO₄ (Phosphate)** – causes algal blooms
- **Cl (Chloride)** – affects water salinity

> Refer to [Parameters_WQM_RMS.pdf](https://github.com/Lightning-President-9/Water-Quality-Prediction/blob/main/Parameters_WQM_RMS.pdf) for environmental significance and accepted limits of each parameter.

## Week 1 - Data Preprocessing

**Notebook**: [Water_Quality_Prediction.ipynb](https://github.com/Lightning-President-9/Water-Quality-Prediction/blob/main/Week_1/Water_Quality_Prediction.ipynb)

In this first week:
- Imported and explored the dataset
- Checked for missing/null values
- Converted necessary columns to datetime format
- Analyzed parameter distributions across districts

## Week 2 – Predicting Water Pollutants Using Machine Learning

**Notebook**: [Water_Quality_Prediction.ipynb](https://github.com/Lightning-President-9/Water-Quality-Prediction/blob/main/Week_2/Water_Quality_Prediction.ipynb)

In Week 2, we built and evaluated a machine learning model to predict multiple water quality parameters for a given year and monitoring station.

### Data Preparation
We first cleaned the dataset by dropping rows with missing values for key pollutants. The input features selected were:
- `station_id` (representing the monitoring location)
- `year` (to capture temporal trends)

The pollutants we targeted for prediction were:
- `O2` (Dissolved Oxygen)
- `NO3` (Nitrate)
- `NO2` (Nitrite)
- `SO4` (Sulfate)
- `PO4` (Phosphate)
- `CL` (Chloride)

To handle the categorical station IDs, we used one-hot encoding to convert them into numeric columns.

### Model Training
We used a `MultiOutputRegressor` wrapped around a `RandomForestRegressor`, which allowed us to train a separate regression model for each pollutant simultaneously.

We split the data into training and testing sets (80/20), trained the model, and evaluated its performance using:
- **Mean Squared Error (MSE)**
- **R² Score** (a higher score indicates better prediction accuracy)

### Sample Results

Below are the model's performance metrics (R² and MSE) on the test dataset for each pollutant:

| Pollutant | R² Score | MSE       | Interpretation |
|-----------|----------|-----------|----------------|
| **O₂**    | -0.017   | 22.22     | Poor prediction; model underperforms compared to mean |
| **NO₃**   | 0.516    | 18.15     | Moderate prediction quality |
| **NO₂**   | -78.42   | 10.61     | Very poor performance; model likely overfitting or lacks signal |
| **SO₄**   | 0.412    | 2412.14   | Decent prediction, room for improvement |
| **PO₄**   | 0.322    | 0.38      | Basic pattern captured; could be improved |
| **CL**    | 0.736    | 34882.81  | Strongest performance among all pollutants |

### Prediction
We tested the model on hypothetical input: station `22` in the year `2024`.
