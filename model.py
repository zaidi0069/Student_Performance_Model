import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score\





# Read the dataset
data = pd.read_csv('Student_Performance.csv')

# Convert 'Yes' and 'No' to 1 and 0 in the 'Extracurricular Activities' column
data['Extracurricular Activities'] = data['Extracurricular Activities'].map({'Yes': 1, 'No': 0})

print(data)
# Separate features (x) and target variable (y)
y = data['Performance Index']
x = data.drop('Performance Index', axis=1)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=50)

# Instantiate the Linear Regression model
linear_reg = LinearRegression()

# Train the Linear Regression model on the training data
linear_reg.fit(x_train, y_train)
#save the model

pickle.dump(linear_reg, open("model.pkl", "wb"))




# # Make predictions using the trained linear regression model

# y_pred = linear_reg.predict(x_test)

# # Display the predictions
# print(y_pred)





# mse = mean_squared_error(y_test, y_pred) 

# r2 = r2_score(y_test, y_pred) 


# r2



# # Create a scatter plot comparing actual vs. predicted values
# plt.figure(figsize=(8, 6))
# plt.scatter(y_test, y_pred, color='blue', alpha=0.5)  # Scatter plot of actual vs. predicted
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')  # Diagonal line
# plt.title('Actual vs. Predicted')
# plt.xlabel('Actual')
# plt.ylabel('Predicted')
# plt.show()


