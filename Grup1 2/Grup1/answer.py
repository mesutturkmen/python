


def sort():
    dict={}
    list1=[]
    with open('input1_icerik') as file:
        liste=file.read().strip().split('\n')
    print(set(liste))
    for i in set(liste):
        dict.update({i:liste.count(i)})
    print(dict)
    sorted_dict={key:value for key,value in sorted(dict.items())}
    print(sorted(dict))
    max_vote=max(sorted_dict.values())
    for i,j in dict.items():
        if j == max_vote:
            list1.append(i)
    print(list1)
    list1.sort()
    print(list1[0])
    print(max_vote)
print(sort())
