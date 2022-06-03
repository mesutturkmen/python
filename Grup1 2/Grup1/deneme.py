
with open('icerik') as file:
    liste = file.read().strip().split('\n')
    #liste1 =[]
    #for line in file:
        #liste1.append(line.replace("\n","").split())
    liste2 = []
    for i in liste:
        liste2.append(tuple(map(eval,i.split())))

print(liste)
print(liste2)
