# This will return the names in lower case
name1=input("Enter the name1:").lower()
name2=input("Enter the name2:").lower()
#To replace whitespace between names
name1 = name1.replace(" ","")
name2 = name2.replace(" ","")
print(name1)
print(name2)
#To find out the common character we need to compare each character in name1
with each character in name2 so for that I have use for loops
for i in name1:
    for j in name2:
        if i==j:
            #Replace will replace all the occurence of the given character that is why I have mention
            the count here that means it replace only one occurence of that given character
            name1 = name1.replace(i,"",1)
            name2 = name2.replace(i,"",1)
            #if i=j than we need to replace the name and we need to go to the begining of the first for loop
            than only name1 will get update
            break
count= len(name1+name2)
print(count)

#we need to find out the relationship between these two name using this count value
if count>0:
    list1= ["Friends","Lovers","Affectionate","Marriage","Enemies","Siblings"]
    while len(list1)>1:
        #which character we want to delete from the list
        c=count%len(list1)
        #This is because here our index starts from 0
        s_index=c-1
        #for deleting we will use slicing operationa and than we concatenate
        if s_index>=0: 
              left =list1[:s_index]
              right =list1[s_index+1:]
              #concatenate sublist to list1
              list1=left+right
        else:
              #-1 is because index starts from 0
              list1=list1[:len(list1)-1]
    # Here printing list[0] because after deletion only one element is left and that is at indx 0.          
    print("relationship is:",list1[0])
else:
    # Here if the count<0 it is because none character match so ask for different name.
    print("Enter different name")

