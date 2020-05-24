# description
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#  
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


class TwoSum(object):
    def __init__(self, list_var=[2, 7, 12, 112, 15], target=19):
        self.list_var = list_var
        self.target = target

    def solution(self):  # my Solution
        for i in range(len(self.list_var)):
            last_res = self.target - self.list_var[i]
            if last_res in self.list_var:
                target_index = self.list_var.index(last_res)
                aim_target = i
                return [aim_target, target_index]

    def solution1(self):
        dct = {}
        for ind, item in enumerate(self.list_var):
            target_num = self.target - item
            if target_num in dct:
                print(dct)
                return [dct.get(target_num), ind]
            dct[item] = ind


if __name__ == '__main__':
    answer = TwoSum()
    result_20524 = answer.solution()
    result_20524_1 = answer.solution1()
