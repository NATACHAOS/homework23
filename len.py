def findLen(str):
   # ''''''найти длину строки''''''
    counter = 0
    for i in str:
        counter += 1
    return counter


str = "apple"
print('Длина строки', "'", str,"'", 'равна', findLen(str))
