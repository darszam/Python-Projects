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