import pandas as pd

data = pd.read_csv('sample_data/california_housing_train.csv')

filtered_data = data[data['population'] <= 500]
mean_value = filtered_data['median_house_value'].mean()

print("Средняя стоимость дома, где кол-во людей от 0 до 500:", mean_value)

min_population = data['population'].min()
sub_table = data[data['population'] == min_population]
max_households = sub_table['households'].max()

print("Максимальное количество households в зоне минимального значения population:", max_households)