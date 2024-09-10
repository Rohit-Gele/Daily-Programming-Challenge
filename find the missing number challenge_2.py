def missing(arr):
    n=len(arr)+1  
    expected_sum=n*(n+1)//2
    actual_sum=sum(arr)
    missing_num=expected_sum-actual_sum
    return missing_num

print(missing([1, 2, 4, 5]))  
print(missing([2, 3, 4, 5])) 
print(missing([1, 2, 3, 4]))  
print(missing([1]))          
print(missing(list(range(1, 1000000))))  
