def insertionSort(arr):
    n = len(arr)

    if n <= 1:
        return
                                                      #احمد وجيه هلال الالفى 
                                                      #سيكشن5
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        print(f"Key selected: {key}")

        
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            print(f"Moved {arr[i]} to position {i + 1}: {arr}")
            i -= 1

     
        arr[i + 1] = key
        print(f"Inserted key {key} at position {i + 1}: {arr}\n")


arr = [6, 3, 4, 1, 2, 5]
print(f"Original array: {arr}\n")
insertionSort(arr)
print(f"Sorted array: {arr}")
     