import pandas as pd

main_file_path = 'train.csv'
data = pd.read_csv(main_file_path)

print('Csv loaded')

print()


house_price = data.SalePrice
print(house_price.head())

print ()

lot_area_and_year_built = data[['LotArea','YearBuilt']]
print(lot_area_and_year_built.describe())

# Creating learn model
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
y = data.SalePrice

predictors = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr','TotRmsAbvGrd']

X = data[predictors]

my_model = DecisionTreeRegressor()
my_model.fit(X,y)
print("Making predictions for these houses")
print(X.head())
print("Predictions:")
print(my_model.predict(X.head()))

print(mean_absolute_error(y,my_model.predict(X)))

train_X, val_X, train_y, val_y = train_test_split(X,y,random_state=0)
my_model.fit(train_X, train_y)

val_predictions = my_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))

def get_mae(max_leaf_nodes, predictors_train, predictors_val, targ_train, targ_val):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(predictors_train, targ_train)
    preds_val = model.predict(predictors_val)
    mae = mean_absolute_error(targ_val, preds_val)
    return(mae)

for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))

print()
# Random Forest
from sklearn.ensemble import RandomForestRegressor

forest_model = RandomForestRegressor()
forest_model.fit(train_X, train_y)
iowa_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y,iowa_preds))

# Predicting price houses from test csv
test = pd.read_csv('test.csv')
test_X = test[predictors]
predicted_prices = forest_model.predict(test_X)
print(predicted_prices)
print()
submission = pd.DataFrame({'Id': test.Id, 'SalePrice': predicted_prices})
submission.to_csv('submission.csv', index=False)