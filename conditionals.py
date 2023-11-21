# in, not, not in, is, is not
# || = or 
# && = and
# proper mantaining indentation
a = 7

# if-else
if a > 5:
    print("More than 5")
    print("How Much More i dont know")
else:
    print('Wrong Number')

boss = True

# use of is
if boss is True:
    print('Modhu Khaba?')
else:
    print('Mara Khaw')

coin = 'tail'

# use of and, or, ==, else-if
if boss == True and coin == 'tail':
    print('Tell er dibba niye asho')
elif boss is not True or coin != 'tail':
    print('Basor Rat')

# nested conditions, is, is not, and, or
uiu = 'bash'
faculty = False
if uiu is  'bash' and faculty is not False:
    print('Tumi jano na kichu') 
    if uiu == 'bash' or faculty is True:
        print('You are right')
        if uiu is 'bash' and faculty is True:
            print('tumi jano na meya bal')
        elif uiu is 'bash' and faculty is False:
            print('Good, Now Perfect')
else:
    print('Tumi syllabus er moddhe nai')

    