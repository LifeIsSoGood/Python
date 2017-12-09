arr1=[1,2,3,4,5,6]
arr2=[2,3,4,6,8]
arr3=[]

def fn(arr1,arr2):
    if arr1[0] <= arr2[0]:
        arr3.append(arr1[0])
        arr1.pop(0)
        if len(arr1) >0:
            fn(arr1, arr2)
        else:
            arr3.extend(arr2)
    else:
        arr3.append(arr2[0])
        arr2.pop(0)
        if len(arr2) >0:
            fn(arr1, arr2)
        else:
            arr3.extend(arr1)
    return

def join(arr1,arr2):
    arr1.extend(arr2)
    return arr1

if(len(arr1) and len(arr2)):
    if arr1[-1] <= arr2[0]:
        join(arr3,join(arr1,arr2))

    elif arr2[-1] <= arr1[0]:
        join(arr3,join(arr2,arr1))
    else:
        fn(arr1, arr2)
else:
    join(arr3,join(arr1,arr2))

print(arr3)
