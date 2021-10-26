def reverse(nums):
  #pointing to first index
  startIndex = 0
  #pointing to last index
  endIndex = len(nums)-1

  while endIndex > startIndex:
    #swap the items
    nums[startIndex], nums[endIndex] = nums[endIndex], nums[startIndex]
    startIndex = startIndex+1
    endIndex = endIndex-1

n = [1, 2, 3, 4]
reverse(n)
print(n)