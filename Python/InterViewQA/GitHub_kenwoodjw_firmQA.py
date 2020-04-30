'''
python新式类和经典类的区别
1、python里凡是继承了object的都是新式类，
2、python里只有新式类
3
'''
import os


class Solution(object):
    run_count = 0

    def __init__(self):
        self.run_count = self.run_count + 1

    def reverstring(self, string):
        if string.startswith('-'):
            raw_string = string[1:]
            res_string = raw_string[::-1]
            return "-" + res_string
        else:
            return string[::-1]

    def get_python_file(self, path):
        files_list = []
        for root, dirs, files in os.walk(path):
            files_list.append(files)
        flated_list = [it for sublist in files_list for it in sublist]
        res = filter(lambda x: x.endswith('.py'), flated_list)
        return res

    def list_temp(self):
        list_var = list(range(1, 21))
        sum_var = sum(list_var)


if __name__ == '__main__':
    solution = Solution()
    reversed_string = solution.reverstring("120")
    reversed_string2 = solution.reverstring("-120")
    python_file = solution.get_python_file('E:\李震祥\PYGIT\Learnning\Python')
