nums = [1,2,3,4,5]

print(nums[0])

print(nums[1:3])

for i in range(len(nums)):
    if nums[i] == 4:
        print("We have found 4")
        break

# for i in nums:
#     if i == 4:
#         print("We have found 4")
#         break

nums.insert(0,10)

print(nums)

nums[0] = 100

print(nums)

print 'lambda test \n'
print map(lambda n: n + 1, nums)
