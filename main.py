#hw3_5

number1 = 20
number2 = 30

print(number1 + number2)
print(number1 * number2)
print(number1 - number2)
print(number1 / number2)

#hw3_6

list_ = list(range(1, 11))

for i in range(20, 26):
    list_.append(i)

print(list_[0], list_[3], list_[5], list_[2], list_[11])

print(list_[1:5])
print(list_[4:9])
print(list_[3:])
print(list_[:4])
print(list_[1:10:2])
print(list_[:])
print(list_[::2])

#hw3_7

set1 = {1, 2, 3}
set2 = {2, 3, 5}

print(set1 & set2)
print(set1 | set2)
print(set1 - set2)
print(set2 - set1)
print(set1 ^ set2)
