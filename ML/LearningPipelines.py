import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Read Data
data = pd.read_csv('melb_data.csv')
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]
y = data.Price
train_X, test_X, train_y, test_y = train_test_split(X, y)

from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Imputer

my_pipeline = make_pipeline(Imputer(), RandomForestRegressor())
my_pipeline.fit(train_X, train_y)
predictions = my_pipeline.predict(test_X)

# Alternative code instead of 3 lines above:
# my_imputer = Imputer()
# my_model = RandomForestRegressor()
# imputed_train_X = my_imputer.fit_transform(train_X)
# imputed_test_X = my_imputer.transform(test_X)
# my_model.fit(imputed_train_X, train_y)
# predictions = my_model.predict(imputed_test_X)
error = mean_absolute_error(test_y, predictions)
print("MAE:%d"%error)
from sklearn.model_selection import cross_val_score
scores = cross_val_score(my_pipeline, X, y, scoring='neg_mean_absolute_error')
print(scores)
print('Mean Absolute Error %2f' %(-1 * scores.mean()))