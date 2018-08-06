import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer

data = pd.read_csv('train.csv')
data.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = data.SalePrice
X = data.drop(['SalePrice'], axis=1).select_dtypes(exclude=['object'])
train_X, test_X, train_y, test_y = train_test_split(X.as_matrix(), y.as_matrix(), test_size=0.25)

my_imputer = Imputer()
train_X = my_imputer.fit_transform(train_X)
test_X = my_imputer.transform(test_X)

from sklearn.ensemble import GradientBoostingRegressor
my_new_model = GradientBoostingRegressor()
my_new_model.fit(train_X, train_y)
predictions = my_new_model.predict(test_X)


print("Mean Absolute Error:" + str(mean_absolute_error(predictions,test_y)))

my_new_model = GradientBoostingRegressor(n_estimators=1000,learning_rate=0.05)
my_new_model.fit(train_X, train_y)
predictions = my_new_model.predict(test_X)


print("Mean Absolute Error:" + str(mean_absolute_error(predictions,test_y)))

my_new_model = GradientBoostingRegressor(n_estimators=1000,learning_rate=0.1)
my_new_model.fit(train_X, train_y)
predictions = my_new_model.predict(test_X)


print("Mean Absolute Error:" + str(mean_absolute_error(predictions,test_y)))