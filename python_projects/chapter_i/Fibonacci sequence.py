def length():
    length = input('How many digits of the sequence would you like: ')
    return int(length)

def sequence(length):
    lst = [0,1,1]
    count = 0
    while count < length:
        first_num = lst[-1] + lst[-2]
        lst.append(first_num)
        count += 1
        pass
    return lst[0:length]

def main():
    end = length()
    numbers = sequence(end)
    print(numbers)
    pass

main()