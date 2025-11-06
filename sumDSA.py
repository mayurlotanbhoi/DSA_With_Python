# 3sum
arr = [1,4,5,4,8,9,9,5,-5,6,4]
target = 5

may_set = set()

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        remain = target - (arr[i] + arr[j])
        if remain in may_set:
            print('sum found', remain, arr[i], arr[j])
        else:
            may_set.add(arr[i])      