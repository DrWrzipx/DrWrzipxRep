#Data structure: List:

list = [1, 3, 4]
fruits = ["apple", "orange", "pear"]
print(list)
print (fruits)
fruits.append("watermellon")
print (fruits)

fruits.append(list)
print(fruits)

# Data structure: Dictionary:

d = {}
d = {'alice': '817-673-345', 'bob': '345-245-785', 'mario': '384-048-283'}
print(d)
#print(mario)

cities = ['Maribor', 'Celje', 'Velenje', 'Novo Mesto', 'Ljubljana']
for city in cities:
    print (city)

print('\n')

for index in d:
    print(index, d[index])
