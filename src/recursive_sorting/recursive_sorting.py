# TO-DO: complete the helper function below to merge 2 sorted arrays
# use merge inside of merge_sort
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # print('arrA', arrA)
    # print('arrB', arrB)
    merged_arr = [0] * elements
    # TO-DO
    c = i = j = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged_arr[c] = arrA[i]
            i += 1
            # print('arrA is less than arrB', merged_arr)
        else:
            merged_arr[c] = arrB[j]
            j += 1
            # print('arrB is less than arrA', merged_arr)
        c += 1
    while i < len(arrA):
        merged_arr[c] = arrA[i]
        # print('merged_arr', merged_arr)
        i += 1
        c += 1
    while j < len(arrB):
        merged_arr[c] = arrB[j]
        # print('merged_arr', merged_arr)
        j += 1
        c += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    # base case: if the array length is 1 or 0 then there is no
    # need to divide and sort the array, we can just return it.
    if len(arr) <= 1:
        # print(arr)
        return arr
    
    # Find the middle of the array and sub arrays
    middle = len(arr) // 2

    # assign both the left and right side of the arrays into there own
    # seperate arrays by slicing them according to where the middle is.
    right = merge_sort(arr[:middle])
    left = merge_sort(arr[middle:])

    # recursively call merge_sort to continue to divide the halfs until they're
    # arrays of singe integers, then use merge to sort and merge the arrays
    
    return merge(left, right)

# new_array = [1, 7, 3, 9, 8, 4, 2, 5, 0, 6]
# merge_sort(new_array)

# [1, 7, 3, 9, 8, 4, 2, 5, 0, 6]
# [1, 7, 3, 9, 8] [4, 2, 5, 0, 6]
# [1, 7] [3, 9, 8] [4, 2] [5, 0, 6]
# [1] [7] [3, 9, 8] [4] [2] [5, 0, 6]
# [1] [7] [3] [9] [8] [4] [2] [5] [0] [6]
# [1, 7] [3, 9] [4, 8] [2, 5] [0, 6]
# [1, 3, 7, 9] [2, 4, 5, 8] [0, 6]

# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
