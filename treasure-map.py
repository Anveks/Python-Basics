
map = [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

print(f"{map[0]}\n{map[1]}\n{map[2]}")

coordinates = []
row = int(input('Where will you put the treasure? Type the row: \n'))
place = int(input('Type the place: \n'))

coordinates.extend([row, place])

map[coordinates[0] - 1][coordinates[1] - 1] = '❌'

# coordinates = input('Where do you want to put the treasure? \n')
# horizontal = int(coordinates[0])
# vertical = int(coordinates[1])

print(f"{map[0]}\n{map[1]}\n{map[2]}")

