# def water_trapped(arr, n):
#     l = 0 
#     r = n - 1
#     l_max = r_max = water_trapped = 0
    
#     while l <= r:
#         if(arr[l] >= arr[r]):
#             if arr[r] <= r_max:
#                 water_trapped += r_max - arr[r]
#             else:
#                 r_max = arr[r]
#             r -= 1
#         if arr[l] < arr[r]:
#             if arr[l] <= l_max:
#                 water_trapped += l_max - arr[l]
#             else:
#                 l_max = arr[l]
#             l += 1

#     return water_trapped

# # Example usage
# arr = [3, 0, 0, 2, 0, 4]
# n = len(arr)
# trapped = water_trapped(arr, n)
# print(trapped)

def water_trapped(arr, n):
    l_max = [0] * n
    r_max = [0] * n
    water_trapped = 0
    
    l_max[0] = arr[0]
    for i in range(1, n):
        l_max[i] = max(l_max[i-1], arr[i])
    
    r_max[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        r_max[i] = max(r_max[i+1], arr[i])
    
    for i in range(n):
        water_trapped += min(l_max[i], r_max[i]) - arr[i]
    
    return water_trapped


# Example usage
arr = [3, 0, 0, 2, 0, 4]
n = len(arr)
result = water_trapped(arr, n)
print(result)
