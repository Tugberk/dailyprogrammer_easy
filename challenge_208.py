#challenge 208
#culling numbers


nums = raw_input('>enter as 5-6-7\n')
print nums
nums = nums.split('-')
print nums


#this here gives us the unique elements in a given list
new_list = list(set(nums))
print sorted(new_list)
