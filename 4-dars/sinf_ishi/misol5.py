nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
nums1= set()
for k in nums:
    if k % 2 == 0:
        nums1.add(k)
print(nums1)