from time import sleep
list = [0,0,0,0,0,0,0,0,0,0]
def test_for():
    for i in range(1, 10000):
        list.append(i)
        if len(list) > 10:
            list.pop(0)
        else:
            pass
        sleep(3)
        str_list0 = str(list[0])
        str_list1 = str(list[1])
        str_list2 = str(list[2])
        str_list3 = str(list[3])
        str_list4 = str(list[4])
        str_list5 = str(list[5])
        str_list6 = str(list[6])
        str_list7 = str(list[7])
        str_list8 = str(list[8])
        str_list9 = str(list[9])
        st_full = str_list0 + '\n' + str_list1 + '\n' + str_list2 + '\n' + str_list3 + '\n' + \
                  str_list4 + '\n' + str_list5 + '\n' + str_list6 + '\n' + str_list7 + '\n' + \
                  str_list8 + '\n' + str_list9
        print st_full
        f = open('dump.txt', 'w')
        f.write(st_full)
        f.close()
test_for()