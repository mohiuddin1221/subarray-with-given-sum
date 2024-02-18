def subarray(arr, target_sum):
    dict1 = {}
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum == target_sum:
            print("Subarray found from index 0 to", i)
            return  
        
        if current_sum - target_sum in dict1:
            print("subarray starts from", dict1[current_sum - target_sum] + 1, "to", i)
            return
        dict1[current_sum] = i 

arr = [1, 4, 20, 3, 10, 5]
target_sum = 33
subarray(arr, target_sum)
