def good_segement(arrayofbad, l, r):
    arrayofbad.sort()
    main_list=[]
    new_list=[]
    max_len=0
    for i in arrayofbad:
        for j in range(l, r+1):
            while j != i:
                new_list.append(j)
                new_list.append(i)
            main_list.append(new_list)

    for i in main_list:
        if i.len()+1 > max_len:
            max_len = i.len+1
    print(max_len)


good_segement([5,4,2,15], 1, 10)
# answer s/b 5
#[1,1],[3,3],[6,10]