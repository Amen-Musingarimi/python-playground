farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)

for animal in farm_animals:
    print(animal)

more_animals = {'sheep', 'goat', 'horse', 'cow', 'hen'}

if farm_animals == more_animals:
    print('The sets are equal')
else:
    print('The sets are different')
