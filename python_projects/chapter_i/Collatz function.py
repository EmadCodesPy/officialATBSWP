def collatz(num):
    if num % 2 == 0:
        print(num // 2)
        return num//2
    else:
        print(3*num+1)
        return 3*num+1

def mainFunc():
    try:
        num = int(input('Enter a number: '))
        while num != 1:
            num = collatz(num)
    except ValueError:
        print('You must enter an integer')

#this is new and for testing git
mainFunc()