def find_num():
    num = input('you want to find numbers under: ')
    return int(num)

def user_input(number):
    user_in = input(f'What numbers would you like to check if they are under {number}:')
    lst = user_in.split(' ')
    return lst

def search(list, thresh):
    temp_lst = []
    for item in list:
        item = int(item)
        if item < thresh:
            temp_lst.append(item)
        else:
            pass
    return temp_lst

def main():
    max_thresh = find_num()
    main_lst = user_input(max_thresh)
    return_lst = search(main_lst, max_thresh)
    print(return_lst)

main()