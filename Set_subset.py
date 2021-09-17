set1=set(input("enter set1:"))
set2=set(input("enter set2:"))
#1st way
'''print(set1.issubset(set2))#by using inbuilt function in sets ,checking elements are there in anotherset or not
print(set2.issubset(set1))#vice versa '''
#second way
set1_list=list(set1)
set2_list=list(set2)
#print(set1_list)
#print(set2_list)
flag=0
#chceking all elements are present in subset or not
if(all(i in set1_list for i in set2_list)):
    flag=1

if flag==1:
    print("set 2 is subset of set2")
else:
    print("set2 is not a subset of set1")
























