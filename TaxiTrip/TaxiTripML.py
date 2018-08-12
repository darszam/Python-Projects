import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Imputer
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

# Reading Data
data = pd.read_csv('train.csv')
data_test = pd.read_csv('test.csv')
print('Loading Data Completed')
y = data.trip_duration
cols_to_use = ['vendor_id','passenger_count','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude']
X = data[cols_to_use]
train_X, test_X, train_y, test_y = train_test_split(X,y)

print('Spliting data completed')
my_pipeline = make_pipeline(Imputer(), GradientBoostingRegressor(n_estimators=1000, learning_rate=0.05))
my_pipeline.fit(train_X, train_y)
print("Fitting completed")
#predictions = my_pipeline.predict(test_X)
#print("Predicting test data completed")

#from sklearn.metrics import mean_absolute_error
#error = mean_absolute_error(test_y,predictions)
#print("MAE:%d"%error)

predicted_trips = my_pipeline.predict(data_test[cols_to_use])
submission = pd.DataFrame({'Id': data_test.id, 'trip_duration': predicted_trips})
submission.to_csv('submissiontaxi.csv', index=False)