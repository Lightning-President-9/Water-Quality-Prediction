import pandas as pd
import numpy as np
import joblib
import streamlit as st
import plotly.graph_objects as go

# Load model and model columns
model = joblib.load("pollution_model.pkl")
model_cols = joblib.load("model_columns.pkl")

# Define pollutants and their acceptable limits
pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']
limits = {
    'O2': 5,
    'NO3': 10,
    'NO2': 0.1,
    'SO4': 250,
    'PO4': 0.1,
    'CL': 250
}

# UI
st.title("Water Quality Prediction")
st.write("Predict key water pollutant levels based on Year and Station ID")

# Inputs
year_input = st.number_input("Enter Year", min_value=2000, max_value=2100, value=2022)
station_id = st.text_input("Enter Station ID", value='1')

# Graph type toggle
graph_type = st.radio("Choose visualization type", ["Radar Chart", "Gauge Charts", "Bullet Charts"])

# Predict and display
if st.button("Predict"):
    if not station_id.strip():
        st.warning("Please enter the Station ID.")
    else:
        # Prepare input
        input_df = pd.DataFrame({'year': [year_input], 'id': [station_id]})
        input_encoded = pd.get_dummies(input_df, columns=['id'])

        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[model_cols]

        # Make prediction
        predicted = model.predict(input_encoded)[0]
        predicted_values = dict(zip(pollutants, predicted))

        st.subheader(f"Predicted pollutant levels for Station '{station_id}' in {year_input}:")
        for p, val in predicted_values.items():
            st.write(f"**{p}**: {val:.2f} (Limit: {limits[p]})")

        # ------------------ GRAPH SELECTION ------------------

        if graph_type == "Radar Chart":
            st.subheader("Radar Chart: Predicted vs Acceptable Limits")
            fig = go.Figure()

            fig.add_trace(go.Scatterpolar(
                r=list(predicted_values.values()),
                theta=pollutants,
                fill='toself',
                name='Predicted',
                line=dict(color='red')
            ))

            fig.add_trace(go.Scatterpolar(
                r=[limits[p] for p in pollutants],
                theta=pollutants,
                fill='toself',
                name='Acceptable Limit',
                line=dict(color='green', dash='dash')
            ))

            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True)),
                showlegend=True,
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)

        elif graph_type == "Gauge Charts":
            st.subheader("Gauge Charts: Per Pollutant")
            for p in pollutants:
                actual = predicted_values[p]
                limit = limits[p]
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=actual,
                    title={'text': f"{p} Level"},
                    gauge={
                        'axis': {'range': [0, limit * 2]},
                        'bar': {'color': "red" if actual > limit else "blue"},
                        'steps': [
                            {'range': [0, limit], 'color': "lightgreen"},
                            {'range': [limit, limit * 2], 'color': "lightcoral"}
                        ],
                        'threshold': {
                            'line': {'color': "black", 'width': 4},
                            'thickness': 0.75,
                            'value': limit
                        }
                    }
                ))
                st.plotly_chart(fig, use_container_width=True)

        elif graph_type == "Bullet Charts":
            st.subheader("Bullet Charts: Predicted vs Safe Threshold")
            for p in pollutants:
                actual = predicted_values[p]
                limit = limits[p]
                fig = go.Figure()

                fig.add_trace(go.Bar(
                    x=[limit * 3],
                    y=[p],
                    marker=dict(color='lightgray'),
                    orientation='h',
                    name='Max Scale',
                    showlegend=False
                ))

                fig.add_trace(go.Bar(
                    x=[limit],
                    y=[p],
                    marker=dict(color='lightgreen'),
                    orientation='h',
                    name='Safe Limit',
                    showlegend=False
                ))

                fig.add_trace(go.Scatter(
                    x=[actual],
                    y=[p],
                    mode='markers',
                    marker=dict(color='red' if actual > limit else 'blue', size=12),
                    name='Predicted'
                ))

                fig.update_layout(
                    barmode='overlay',
                    height=120,
                    margin=dict(l=40, r=10, t=30, b=10),
                    xaxis=dict(range=[0, limit * 3]),
                    title=f"{p}: {actual:.2f} (Limit: {limit})"
                )

                st.plotly_chart(fig, use_container_width=True)