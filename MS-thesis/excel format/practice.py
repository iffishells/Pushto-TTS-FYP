
#grammer={"S":0.6, "NP":0.2, "VP":0.2, "ADJ":0.3, "NU":0.5, "N":0.6,"V":0.5, "AV":0.4, "AP":0.6,"PN":0.47,"ADV":0.7}

grammer={"S":0.6, "NP":0.2, "VP":0.2, "ADJ":0.3, "NU":0.5, "N":0.6,"V":0.5, "AV":0.4, "AP":0.6,"PN":0.47,"ADV":0.7}



with open("temp.txt", "r", encoding='utf-8') as f:
        line=f.read()
print(line)
#line=line.strip("\n")
list=line.split(" ")
print (list)
prob=1
temp=0
total=0
print ("Count of S")
temp=list.count("\ufeff(S\n")
if(temp!=0):
    prob=prob*(grammer["S"]*temp)
    total+=temp
    temp=0
print(list.count("\ufeff(S\n"))


temp=list.count("(NP")
if(temp!=0):
    print("NP Grammer = ",grammer["NP"])
    print("prob before = ", prob)
    print("temp current = ", temp)
    prob=prob*(grammer["NP"]*temp)
    total+=temp
    temp=0
print(list.count("(NP"))

print ("Count of VP")
temp=list.count("(VP")
if(temp!=0):
    prob=prob*(grammer["VP"]*temp)
    total+=temp
    temp=0
print(list.count("(VP"))

print ("Count of ADJ")
temp=list.count("(ADJ")
if(temp!=0):
    prob=prob*(grammer["ADJ"]*temp)
    total+=temp
    temp=0
print(list.count("(ADJ"))

print ("Count of NU")
temp=list.count("(NU")
if(temp!=0):
    prob=prob*(grammer["NU"]*temp)
    total+=temp
    temp=0
print(list.count("(NU"))

print ("Count of N")
temp=list.count("(N")
if(temp!=0):
    prob=prob*(grammer["N"]*temp)
    total+=temp
    temp=0
print(list.count("(N"))

print ("Count of V")
temp=list.count("(V")
if(temp!=0):
    prob=prob*(grammer["V"]*temp)
    total+=temp
    temp=0
print(list.count("(V"))

print ("Count of AV")
temp=list.count("(AV")
if(temp!=0):
    prob=prob*(grammer["AV"]*temp)
    total+=temp
    temp=0
print(list.count("(AV"))

print ("Count of AP")
temp=list.count("(AP")
if(temp!=0):
    prob=prob*(grammer["AP"]*temp)
    total+=temp
    temp=0
print(list.count("(AP"))

print ("Count of PN")
temp=list.count("(PN")
if(temp!=0):
    prob=prob*(grammer["PN"]*temp)
    total+=temp
    temp=0
print(list.count("(PN"))

print ("Count of ADV")
temp=list.count("(ADV")
if(temp!=0):
    prob=prob*(grammer["ADV"]*temp)
    total+=temp
    temp=0
print(list.count("(ADV"))

print(prob/total)
##print ("total = ",total)
##print ("prob = ",prob)
