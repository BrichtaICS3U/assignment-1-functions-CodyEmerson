# Assignment 1
# ICS3U
# <Cody Emery>
# March 28, 2018

###### uncomment this when you are ready to work on it
def CtoF (x):
    x = (1.8)*x+32
    return x

###### uncomment this when you are ready to work on it
def FtoC (y):
    y  = (0.55556)*(y-32)
    return y


answ = True
while answ == True:
    print('Convert to Celsius or to Fahrenheit?')
    ans = str(input())
    if ans == str('Fahrenheit') or ans == str('F'):
        temperature = int(input('Enter your temperature in Celsius: ' ))
        if temperature <= -273:
            print('Print a temperature higher than -273C')
        else:
            temperature = CtoF(temperature)
            print(round(temperature))

    elif ans == str('Celsius') or ans == str('C'):
        temperature = int(input('Enter your temperature in Fahrenheit: ' ))
        if temperature <= -459 :
            print('Print a temperature higher than -459F')
        else:
            temperature = FtoC(temperature)
            print(round(temperature))
    
