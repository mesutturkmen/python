country=input()
start=input()
end=input()
with open("covid_data.txt","r") as file:
    data=file.read().strip().split("\n")
    #print(data)
    new_data=[]
    
    for i in range(len(data)):
        if i !=0:
            new_data.append(data[i].split("\t"))
    confirm=0
    recovered=0
    death= 0
    count=0
    
    for i in new_data:
        #print(int("".join(i[0].split("-"))))
        if i[1] ==country and int("".join(i[0].split("-"))) >= int("".join(start.split("-"))) and int("".join(i[0].split("-"))) <= int("".join(end.split("-"))):
            confirm += int(i[3])
            recovered +=int(i[4])
            death += int(i[5])
            count +=1
    count_oct=0
    confirm_oct=0
    recovered_oct=0
    death_oct=0
    for i in new_data:
        #print(int("".join(i[0].split("-"))))
        if i[1] ==country and int("".join(i[0].split("-"))) >= 20201001 and int("".join(i[0].split("-"))) <= 20201031:
            confirm_oct += int(i[3])
            recovered_oct +=int(i[4])
            death_oct += int(i[5])
            count_oct +=1
    print(f'{confirm/count:.2f}   {recovered/count:.2f}   {death/count:.2f}')
    print(f'{confirm_oct/count_oct:.2f}   {recovered_oct/count_oct:.2f}   {death_oct/count_oct:.2f}')