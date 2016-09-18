from heapq import heappush, heappop, heapify, _heapify_max

heap = []
nums = [1, 55, 32, 76, 89, 12, 34]

for num in nums:
    heappush(heap, num)

while heap:
    print(heappop(heap))

heapify(nums)
print 'Min heap'
print nums

_heapify_max(nums)
print 'Max heap'
print nums
