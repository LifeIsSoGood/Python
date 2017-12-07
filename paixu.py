arr1=[1,3,5,7,9,11]
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

fn(arr1, arr2)
print(arr3)
