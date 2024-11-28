# car_resale_price_prediction.readme

**Overview:**

The `Ubhate_LTD.ipynb` notebook implements a resale car price prediction model designed to estimate a car's market value based on its usage and features. The model analyzes factors like distance traveled, number of previous owners, and year of purchase to understand how these influence price depreciation. Additionally, categorical features such as fuel type, transmission drive, and car segment are incorporated to capture broader trends.

The dataset consists of car resale data with containing the following attributes:
1. Car Name : The name of the car model
2. Year : The year the car was initially purchased brand new.
3. Distance: The distance the car has traveled in kilometers.
4. Owner: The number of previous owners of the car.
5. Fuel : The type of fuel the car uses (e.g., Petrol, Diesel).
6. Location: The location where the car is being registered in goverment transport body
7. Drive: The type of transmission drive car operates on.
8. Type: The segment of the car (e.g., Sedan, SUV, Hatchback)
9. Price: The resale price of the car in monetary units.

**Prerequisites**
Python 3.7 or higher.
Required libraries:
pandas
numpy
matplotlib
seaborn
sklearn
RandonforestRegressor

**Steps in the Project**

1. Data Preprocessing
Handling Missing Values:
Dropped rows with missing values in Car Name, Year and Location due to low impact.(<5%)
Created bins for distance column

2. Exploratory Data Analysis (EDA)
Boxplots to identify outliers.
Visualized key relationships between features and the target variable (Price) using Facet Grid of Scatterplot.
Catplot to give business insights

3. Feature Engineering
Encoding Categorical Features: Car Name, Fuel, Location, Drive, and Type.
Used OrdinalEncoder for ordinal variables: Year, Owner, and Distance_Binned.

4. Model Development
Split the data into training and testing sets (80% train, 20% test).
Trained the following machine learning models:
Random Forest Regressor (baseline model).

5. Evaluation
Used metrics:
Mean Absolute Error (MAE): Measures average prediction error.
R-squared (R²): Explains the variance in Price captured by the model.
Achieved:
MAE: 58,191
R²: 0.833

**This predictive tool offers valuable insights for automobile dealers, enabling them to optimize transaction rates and make data-driven decisions in the resale market.**
