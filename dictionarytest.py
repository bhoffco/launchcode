my_dictionary = {'cat': 'kitty', 'dog': 'fritz', 'bird': 'ruby'}

print(my_dictionary['cat'])


del my_dictionary['bird']

print(my_dictionary)

my_dictionary['dog'] = 'rover'

print(my_dictionary)

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for i in inventory.keys():
    print(i[0] + i[1])


for i in inventory.keys():
    let = ""
    let = let + i[:3]
    print(let)
    print(inventory[i])

keys = list(inventory.keys())
print(keys)
print(inventory[i])


def adds_numbers(num):

    a = num + 5
    b = num + 10
    return (a, b)


print(adds_numbers(10))

matrix = [[0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 3, 0]]

print(matrix)
