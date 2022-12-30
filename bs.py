arr = [1, 2, 9, 10, 15, 21, 45, 100, 150]
key = 15
left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right)//2
    if arr[mid] == key:
        break
    elif arr[mid] < key:
        left = mid
    else:
        right = mid

print(mid)