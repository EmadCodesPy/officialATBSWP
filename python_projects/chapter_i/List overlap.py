def lists():
    inp1 = input('What is your first list: ')
    lst1 = inp1.split(' ')
    inp2 = input('What is your second list: ')
    lst2 = inp2.split(' ')
    return lst1,lst2

def compare(list1, list2):
    lst3 = []
    for item in list2:
        if item in list1:
            lst3.append(item)
        else:
            pass
    return lst3

def main():
    Lists,Lists2 = lists()
    end_res = compare(Lists,Lists2)
    print(end_res)

main()
