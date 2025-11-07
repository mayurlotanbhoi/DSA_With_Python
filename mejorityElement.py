arr = [2,2,3,6,5,8,7,2,2,2,2,2,2,8,2]

my_map = {}

# for i in range(len(arr)):
#     if arr[i] in my_map:
#         my_map[arr[i]] = my_map[arr[i]]+1
#         if my_map[arr[i]]  >= len(arr)//2:
#             print('this is mejority element ',arr[i], my_map[arr[i]] )
#             break;
#     else:
#          my_map[arr[i]] = 1  
# 
 
candidet = arr[0]
count = 1
for i in range(1,len(arr)):
    if arr[i] == candidet:
        count = count+1
    else:
        count = count -1

    if count == 0:
        candidet = arr[i]
        count = 1  

count = 0
for i in range(len(arr)):
    if arr[i] == candidet:
        count = count+1

if count > len(arr)/2:
    print("this candiet win", candidet)
else:
    print("no noe will")    


