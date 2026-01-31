# House Price Prediction

## Repository Outline
```
1. description.md - Penjelasan gambaran umum project
2. training_notebook.ipynb - Notebook for build model
3. inference_notebook.ipynb - Notebook for inferencing/predicting new data
4. house-price-v2.csv - Dataset for training model
5. deployment - Folder consists of script for deployment
6. dataset_description.png - Description of dataset columns
```

## Problem Background
Purchasing a residential property represents a significant milestone for many individuals. However, navigating the complexities of the real estate market within a specific budget can be an overwhelming endeavor. Property values are influenced by a diverse array of characteristics and variables, and assessing these factors objectively often proves challenging due to inherent cognitive biases. This project is driven by the need to provide a systematic framework that assists prospective buyers in evaluating their options through data-driven insights.

## Project Output
The primary goal of this project is to develop a predictive model that estimates property prices based on their specific attributes. By providing accurate price projections, this model enables homebuyers to align their financial expectations with market realities, facilitating more informed and confident purchasing decisions.

## Data
![alt text](dataset_description.png)

## Method
This model implement XGBoost algoritm which is the most reliable model than compared models, Random Forest, XGBoost, Linear Regression (Ridge), Linear Regression (Ridge), Linear Regression (Lasso), Linear Regression (Polynomial).

## Stacks
Language    : Python
Tools       : Visual Studio Code, Streamlit, HuggingFace

## Reference
HuggingFace Deployment https://huggingface.co/spaces/RifqiAs/House_Price_Prediction