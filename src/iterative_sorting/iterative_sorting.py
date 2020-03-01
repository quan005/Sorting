# TO-DO: Complete the selection_sort() function below 
newArray = [6,2,9,5,3,1,4,7,8]
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    # print(arr)
    return arr

selection_sort(newArray)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    
    for i in range(0, len(arr)):
        swapped = False

        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if swapped == False:
            break


    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr