
list = [2,4,5]

# list compherension example:
new_list = [item for item in list if item % 2 == 0]

# multiplied nums
doubled_list = [num * 2 for num in range(1,5)]
print(doubled_list)

# squared nums
squared_list = [num ** 2 for num in list]
print(squared_list)