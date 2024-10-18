
Numbers = [3, 6, 1, 9, 2]
print(f"\n Given Numbers are:", Numbers)

Numbers.append(7)
print(f"\n The New numbers are:  ", Numbers)

Numbers.sort()
print(f"\n The arrangement of the given number in ascending order :  ", Numbers)

NumbersNew = tuple(Numbers)

print("The First Element of the sorted numbers is", NumbersNew[0], "and the Last Element is", NumbersNew[5] )
