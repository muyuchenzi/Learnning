class QuestionAnswer(object):
    class_function_count = 0

    def __init__(self):
        self.class_function_count = self.class_function_count + 1

    def merge_list(self, list_var_1, list_var_2):
        '''
        :param list_var_1:
        :param list_var_2:
        :return: 对两个list 进行排序，并进行有序排列
        '''
        temp = []
        while len(list_var_1) > 0 and len(list_var_2) > 0:
            if list_var_1[0] < list_var_2[0]:
                temp.append(list_var_1[0])
                del list_var_1[0]
            else:
                temp.append(list_var_2[0])
                del list_var_2[0]
        while len(list_var_1) > 0:
            temp.append(list_var_1[0])
            del list_var_1[0]
        while len(list_var_2) > 0:
            temp.append(list_var_2[0])
            del list_var_2[0]
        return temp

    def list_sort_odd_even(self, list_var):
        odd_list = []
        even_list = []
        for li in list_var:
            if li % 2 == 0:
                odd_list.append(li)
            else:
                even_list.append(li)
        odd_list_sorted = sorted(odd_list, reverse=True)
        even_list_sorted = sorted(even_list, reverse=False)
        odd_list_sorted.extend(even_list_sorted)
        print(odd_list_sorted)
        return odd_list

    @staticmethod
    def count_string(string_var):
        key_list = set(string_var)
        dict_string_count = dict.fromkeys(key_list, 0)
        for li in string_var:
            dict_string_count[li] = dict_string_count[li] + 1
        return dict_string_count


if __name__ == '__main__':
    my_question = QuestionAnswer()
    merge_list_res = my_question.merge_list([1, 2, 3, 4], [0, 1, 2, 3, 4])
    sort_list_odd_even = my_question.list_sort_odd_even([2, 4, 5, 1, 3, 9, 0, 4, 8, 67])
    temp=QuestionAnswer.count_string()
