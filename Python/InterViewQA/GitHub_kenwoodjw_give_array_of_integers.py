class Solution(object):
    func_call_count = 0

    def __init__(self):
        self.func_call_count = self.func_call_count + 1

    def two_sum(self, nums, target):
        # target_num
        for num in nums:
            target_num = target - num
            try:
                target_index = nums.index(target_num)
            except ValueError:
                target_index = None
            num_index = nums.index(num)
        return [num_index, target_index]


if __name__ == '__main__':
    my_solution = Solution()
    two_sum_list_index = my_solution.two_sum(nums=[2, 7, 11, 15], target=18)
