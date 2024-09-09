def sort_array(arr):
    small=0
    medium=0
    large=len(arr) - 1

    while medium <= large:
        if arr[medium]==0:
            arr[small]=arr[medium]
            arr[medium]=arr[small]
            small += 1
            medium += 1
        elif arr[medium] == 1:
            medium += 1
        elif arr[medium] == 2:
            arr[medium]=arr[large]
            arr[large]=arr[medium]
            large -= 1

    return arr

print(sort_array([0, 1, 2, 1, 0, 2, 1, 0]))  
print(sort_array([2, 2, 2, 2]))              
print(sort_array([0, 0, 0, 0]))              
print(sort_array([1, 1, 1, 1]))              
print(sort_array([2, 0, 1]))                 
print(sort_array([]))                        
