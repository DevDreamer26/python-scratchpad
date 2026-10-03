nums = [2,7,11,15]

target = 9

arr = []

for i in range(len(nums)):
    arr.append((nums[i], i))

arr.sort()

left = 0
right = len(arr) - 1

if not nums:
    print("No numbers available")

while left < right:

    current_sum = arr[left][0] + arr[right][0]

    if current_sum == target:
        print(arr[left][1], arr[right][1])
        break

    elif current_sum > target:
        right -= 1

    else:
        left += 1
        
if current_sum != target:
    print('Not possible ')