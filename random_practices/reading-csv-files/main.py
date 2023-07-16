import pandas

data = pandas.read_csv('./random_practices/reading-csv-files/weather_data.csv')
temp_list = data['temp'].to_list()

avg = data['temp'].mean()
max = data['temp'].max()
day_with_max = data[data.temp == max] # filtering by a specific parameter

monday = data[data.day == 'Monday'] # filtering out the specific data

#  creating a dataframe:
data_dict = {
  'students': ['Tom', 'Arthur', 'John'],
  'scores': [50, 60, 70]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv('new_data.csv') # saving the new data as a separate file
