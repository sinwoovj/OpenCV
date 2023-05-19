import os
os.system('clear')

numbers = [11,12,13,14,15]
print(numbers)
print(numbers[2])
print(numbers[2:4])

numbers[1], numbers[3] = 22, 24
print(numbers[:])

numbers[:] = []
print(numbers[:])

numbers = [1, 2, 3, 4, 5]
alphabet = ['a', 'b', 'c']
collabo = [numbers, alphabet]
print(collabo[:])
print(collabo[0])
print(collabo[1])