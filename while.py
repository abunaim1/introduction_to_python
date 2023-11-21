
# While loop
# num = 20
# while(num>=10):
#     if num%2 is not 0:
#         print('Odd: ', num)
#     else:
#         print('Even: ', num)
#     num -= 1

# Continue statement
# num = 20
# while(num>=10):
#     num -= 1
#     if num%2 != 0:
#         if num == 15:
#             continue
#         print('Odd: ', num)
#     else:
#         print('Even: ', num)


# Break Statement
num = 20
while(num>=10):
    if num%2 != 0:
        if num == 11:
            break
        print('Odd: ', num)
    else:
        print('Even: ', num)
    num -= 1