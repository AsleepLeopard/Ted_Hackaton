array = input()
k = int(input("k: "))
limit = int(input("limit: "))
array2 = array.split(",")


for item in array2:
    array3 = []
    ktru = False
    multitru = False
    multi = 1
    total = 0
    item = int(item)
    array3.append(item)
    for item2 in array2[item: ]:
        ktru = False
        multitru = False
        multi = 1
        total = 0
        item2 = int(item2)
        array3.append(item2)
        for item3 in array3:
            multi = multi*item3
        
        if (len(array3)%2) == 0:
            for item4 in range(0, round(len(array3)/2), 2):
                total = total+array3[item4]
                total = total-array3[item4+1]
        else:
            if round(len(array3)/2)<len(array3)/2: 
                for item4 in range(0, round(len(array3)/2), 2):
                    total = total+array3[item4]
                    total = total-array3[item4+1]
            else:
                for item4 in range(0, round(len(array3)/2)-1, 2):
                    total = total+array3[item4]
                    total = total-array3[item4+1]
        print(array3)
        print(multi, total)
        if multi<limit:
            multitru = True
        
        if k == total:
            ktru = True

        if ktru == True and multitru == True:
            print(multi)
        
        else:
            print(-1)