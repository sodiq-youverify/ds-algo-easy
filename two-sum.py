for i in range(len(nums)):
            for x in range(len(nums)):
                if x != i:
                    if (nums[i] + nums[x] == target):
                        return [i, x]
