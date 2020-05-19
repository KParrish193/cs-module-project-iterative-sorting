# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        curr_index = i
        smallest_index = curr_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for smallest_index in range(i + 1, len(arr)):
            if arr[smallest_index] < arr[curr_index]:
                curr_index = smallest_index

        # TO-DO: swap
        # Your code here
        arr[i], arr[curr_index] = arr[curr_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    n = len(arr) 

    # Traverse through all array elements 
    for i in range(n): 

        # Last i elements are already in place 
        for j in range(0, n-i-1): 

            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return arr

    if maximum == -1:
        maximum = max(arr)

    buckets = [0 for i in range(maximum+1)]

    for x in arr:
        if x < 0:
            return "Error, negative numbers disallowed"
        buckets[x] += 1

    j = 0
    for i in range(len(buckets)):
        while buckets[i] > 0:
            arr[j] = i
            j +=1
            buckets[i] -+ 1

    return arr