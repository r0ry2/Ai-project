Analyze Seasonal Sales Prediction

1.  (Business Understanding):

Project Objective: The main objective is to optimize the storage process and forecast the demand for products in different seasons (winter, spring, summer, autumn). The project aims to identify the products that achieve the highest sales in each season to guide marketing strategies and seasonal offers.



2. Data Understanding:

Data Used: The data was downloaded from the e-commerce dataset available on Kaggle platform. The data contains information such as:
Invoice number
Product
Price
Quantity
Invoice date
Steps taken:
Review the data to understand the types of variables (categorical and numeric).
Check for missing or duplicate values ​​in the columns.
Analyze the distributions of data and sales based on seasons.





3. Data Preparation:
At this stage, the data was cleaned and transformed to be ready for modeling:

Data cleaning: Missing values ​​in columns with missing data were removed or replaced.
Data transformation:
Converting dates to seasons (Winter, Spring, Summer, Fall).
Calculating total sales (TotalSales) using the Quantity * UnitPrice formula.
Extracting the month and year from the invoice date.

4. Modeling:
Model Selection: The Random Forest Regressor algorithm was chosen because it is suitable for problems with numerical and categorical variables.
Data Preparation: The data was divided into Inputs (Features) and Targets (Targets).
Inputs: The variables include Month, Year, Quantity, and Season (represented numerically).
Target: Total Sales.
Model Training: The model was trained on the Training Set.

5. Evaluation
After training the model, it was evaluated using prediction accuracy metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
Metrics used:١
MAE: Reflects the absolute mean of errors between actual and predicted values.
RMSE: Reflects the root mean of squared errors.
Results:
MAE: 12.28
RMSE: 106.05
These values ​​indicate that the model can reasonably predict actual sales, as the error on average is not very high.

 The model was used to make sales forecasts for each season. Actual sales results and forecasts for each season were combined.

season
Total Sales
Expected sales
autumn
3,153,974.55
3,166,579.00
the spring
1,743,295.68
1,731,037.00
summer
1,906,648.60
1,901,971.00
winter
2,107,489.07
2,072,039.00


6. Deployment
Model Accuracy: The performance measures MAE and RMSE were used to evaluate the model. Considering the results, it can be said that the model provides reasonable accuracy in forecasting sales. Sales Comparison: The actual total sales were compared with the forecasts in different seasons. The forecasts were close to the actual sales in most cases.



