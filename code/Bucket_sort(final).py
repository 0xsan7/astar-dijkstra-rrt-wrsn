import random

def my_insertion_sort(arr):
    ops = 0
    # if it's empty or just 1 item, no need to sort
    if len(arr) <= 1:
        return ops
    
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1y
        ops = ops + 1 # picking the key
        
        while j >= 0:
            ops = ops + 1 # comparing
            if arr[j] > temp:
                arr[j + 1] = arr[j]
                ops = ops + 1 # shifting
                j = j - 1
            else:
                break
                
        arr[j + 1] = temp
        ops = ops + 1 
        
    return ops

def doBucketSort(input_list, num_of_buckets):
    total_ops = 0
    
    # making empty buckets
    my_buckets = []
    for i in range(num_of_buckets):
        my_buckets.append([])
        
    # putting numbers into the buckets
    for i in range(len(input_list)):
        val = input_list[i]
        
        # math for bucket index
        index = int((val - 1) * num_of_buckets / 1000)
        
        # just in case it goes out of bounds
        if index >= num_of_buckets:
            index = num_of_buckets - 1
            
        my_buckets[index].append(val)
        total_ops = total_ops + 1

    print("\n--- Bucket Elements (" + str(num_of_buckets) + " buckets) ---")
    
    for i in range(num_of_buckets):
        if len(my_buckets[i]) > 0:
            # sort it
            ops_done = my_insertion_sort(my_buckets[i])
            total_ops = total_ops + ops_done
            
            print("Bucket " + str(i) + ": " + str(my_buckets[i]))

    # merge everything back together
    final_list = []
    for i in range(len(my_buckets)):
        for j in range(len(my_buckets[i])):
            final_list.append(my_buckets[i][j])
            total_ops = total_ops + 1

    print("\n--- Sorted List (" + str(num_of_buckets) + " buckets) ---")
    print(final_list)
    print("\nTotal operations took: " + str(total_ops))
    print("-----------------------------------------------------")

# generate 100 random numbers using a basic loop
random_list = []
for x in range(100):
    random_list.append(random.randint(1, 1000))

print("=== Original List ===")
print(random_list)
print("-----------------------------------------------------")

# test with 10 buckets
doBucketSort(random_list, 10)

# test with 100 buckets
doBucketSort(random_list, 100)