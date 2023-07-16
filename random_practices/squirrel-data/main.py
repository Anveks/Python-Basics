import pandas

squirrel_data = pandas.read_csv('./random_practices/squirrel-data/squirrel_data.csv')
print(squirrel_data.columns) # we get all the column names just in case

# filter the color lists and get their lengths:
gray_total = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
cinnamon_total = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
black_total = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])

# creating a new dictionary:
color_dict = {
  'squirrel_colors': ['gray', 'cinnamon', 'black'],
  'total': [gray_total, cinnamon_total, black_total]
}

# saving it
color_data = pandas.DataFrame(color_dict)
color_data.to_csv('color_data.csv')

