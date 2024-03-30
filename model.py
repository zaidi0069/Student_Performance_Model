import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('Student_Performance.csv')
data['Extracurricular Activities'] = data['Extracurricular Activities'].map({'Yes': 1, 'No': 0})

y = data['Performance Index']
x = data.drop('Performance Index', axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=50)

linear_reg = LinearRegression()
linear_reg.fit(x_train, y_train)

pickle.dump(linear_reg, open("model.pkl", "wb"))
