# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Untuk menjalankan streamlit di eda
# "streamlit run eda.py"

def run():
    # Make title
    st.title("House Price Prediction")
    st.image("deployment/image.jpg")
    st.markdown("## Background")
    st.markdown("""
    Purchasing a residential property represents a significant milestone for many individuals. However, navigating the complexities of the real estate market within a specific budget can be an overwhelming endeavor.
    Property values are influenced by a diverse array of characteristics and variables, and assessing these factors objectively often proves challenging due to inherent cognitive biases. This project is driven by the need to provide a systematic framework that assists prospective buyers in evaluating their options through data-driven insights.       
    """)

    st.markdown("## Objective")
    st.markdown("""The primary goal of this project is to develop a predictive model that estimates property prices based on their specific attributes. By providing accurate price projections, this model enables homebuyers to align their financial expectations with market realities, facilitating more informed and confident purchasing decisions.
    """)

    # Data Preparation
    df_eda = pd.read_csv('deployment/house-price-v2.csv')

    # Menampilkan Visualisasi EDA
    st.markdown("## Exploratory Data Analysis")

    # # 1
    st.markdown("### Voltage Capacity Proportion")
    df_eda['voltage'] = df_eda['voltage'].astype(str).str.replace(' mah', '').astype(int)

    # Condition Setting
    conditions = [(df_eda["voltage"] >=450) & (df_eda["voltage"] <= 2200) ,
                (df_eda["voltage"] >= 3300) & (df_eda["voltage"] <= 5500),
                (df_eda["voltage"] >= 6600)]
    choices = ["Lower", "Middle", "Upper"]

    # Creating New Column
    df_eda["voltage_cat"] = np.select(conditions,
                                choices,default=False)

    # Deleting Column
    df_eda = df_eda.drop(columns=['voltage'])

    # Visualization
    voltage_counts = df_eda['voltage_cat'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.pie(voltage_counts, labels=voltage_counts.index, autopct='%1.1f%%', colors = ['#FF9999', '#66B2FF', '#99FF99'])
    plt.title('Percentage of Houses Based on Voltage Category')
    st.pyplot(fig)
    st.markdown("""Majority of houses are low voltage category (450-2200 VA) by 66%, and for medium and high voltage categories, they are 25% and 7% subsequently.
                The market is heavily saturated with low-voltage properties, reflecting a standard residential profile, whereas high-voltage luxury or specialized estates remain a selective minority within the current inventory.""")
  
    # 2
    # Building Area Filtering
    luxury_houses = df_eda[df_eda['building_area'] >= 300]

    # Luxury House Counting on Each Area
    top_luxury_area = pd.DataFrame(luxury_houses['area'].value_counts().sort_values(ascending=False).head(5))
    top_luxury_area=top_luxury_area.rename(columns={'count':'Total','area':'Area'})

    # Average Houses Price on Top 5
    top_luxury_area['Price (billion)'] = luxury_houses[luxury_houses['area'].isin(top_luxury_area.index)].groupby('area')['price'].mean().sort_values(ascending=False)/1e9
    st.markdown("""### Top 5 Areas with The Most Luxury House and The Average Houses Price on Top 5:""")
    st.dataframe(top_luxury_area)

    # Visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.bar(top_luxury_area.index, top_luxury_area['Price (billion)'], color = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#BC8F8F'])
    plt.title('Average Price at Top 5 Area')
    plt.xlabel('Area')
    plt.ylabel('Average Price (Rupiah)')
    st.pyplot(fig)
    st.markdown("""Based on the quantitative exploration presented above, it is evident that Sentul City constitutes the region with the highest concentration of luxury properties.
                However, in terms of market valuation, Kemang maintains the highest average property price, followed by Pantai Indah Kapuk, BSD, Alam Sutera, and Sentul City respectively.
                A significant insight derived from this analysis is that while Sentul City leads in the volume of luxury housing units, it offers a more competitive and lower average price point compared to the other top-tier areas.
                This suggests that Sentul City may present a higher value proposition for buyers seeking luxury characteristics at a relatively lower entry price.
                """)

if __name__=='__main__':
    run()