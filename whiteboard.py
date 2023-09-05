# Return the "centered" average of an array of ints, 
# which we'll say is the mean average of the values, 
# except ignoring the largest and smallest values in the array. 
# If there are multiple copies of the smallest value, remove all copies
# and likewise for the largest value. 
# return the smallest whole number integer average
# You may assume that the array is length 3 or more.

# Input
nums1=[1, 2, 3, 4, 100]
# Outputs:
3

# Input
nums2=[1, 1, 5, 5, 10, 8, 7]
# Outputs:
6

# Input
nums3=[-10, -4, -2, -4, -2, 0]
# Outputs:
-3


def solution(arr): #o(n)
    highest_val = arr[0] #o(1)
    lowest_val = arr[0] #o(1)
    for num in arr: #o(n)
        if num > highest_val:
            highest_val = num #o(1)
        if num < lowest_val:
            lowest_val = num #o(1)

    mean = 0 #o(1)
    mean_count = 0 #o(1)
    for num in arr: #o(n)
        if num != highest_val and num != lowest_val:
            mean+=num #o(1)
            mean_count += 1 #o(1)
    
    return mean//mean_count #o(1)