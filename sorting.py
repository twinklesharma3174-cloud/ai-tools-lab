def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop to traverse through all list elements
    for i in range(n):
        swapped = False
        
        # Inner loop for pairwise comparisons
        # Last i elements are already sorted, so we can skip them
        for j in range(0, n - i - 1):
            
            # Change > to < to sort in descending order
            if arr[j] > arr[j + 1]:
                # Swap elements in place using Python's tuple unpacking
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If no elements were swapped in the inner loop, the list is already sorted
        if not swapped:
            break
        return arr

# Example usage:
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", data)
    
    bubble_sort(data)
    print("Sorted Array:  ", data)
