# print('Now I need money')
# input()
# taka = input('Give me some moeny: ')
# print("Here is your money: ", taka)


# firstOne = input("Kodom Ali: " )
# secondOne = input("Rhat Ali: ")
# loan = f"First loan from Kodom Ali is {firstOne} and Second loan from Rahat Ali is {secondOne}"
# print(loan)

# By default the input from user will be String type so, we need to 'type conversion'

# befor type conversion
# print(type(firstOne))
# total = firstOne + secondOne
# print("Before type conversation: ", total)


# after type conversion
# money_int = int(firstOne)
# print(type(money_int))
# money2_int = int(secondOne)
# total = money_int + money2_int
# print("After type conversation: ", total)

#one line multiple input
# split -> string to list
# join -> list to string
# take = int(input())
lst = list(map(int, input().split()))
print(lst)

