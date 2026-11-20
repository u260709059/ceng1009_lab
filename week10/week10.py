# # # # # # # # myList = [76, 92.3, "hello", True, 4, 76]
# # # # # # # #
# # # # # # # # myList.append("apple")
# # # # # # # # myList.append(76)
# # # # # # # # myList.insert(3, "cat")
# # # # # # # # myList.insert(0,99)
# # # # # # # # print(myList)
# # # # # # # #
# # # # # # # # print(myList.index("hello"))
# # # # # # # # print(myList.count(76))
# # # # # # # # myList.remove(76)
# # # # # # # # print(myList)
# # # # # # # # myList.pop(myList.index(True))
# # # # # # # # print(myList)
# # # # # # #
# # # # # # # def sum_of_squares(list):
# # # # # # #     sum = 0
# # # # # # #     for i in list:
# # # # # # #         sum += i**2
# # # # # # #     return sum
# # # # # # # list1 = [3, 4, 5]
# # # # # # # print(sum_of_squares(list1))
# # # # # #
# # # # # # def sum_evens(list):
# # # # # #     sum = 0
# # # # # #     for i in list:
# # # # # #         if i % 2 == 0:
# # # # # #             sum += i
# # # # # #     return sum
# # # # # # print(sum_evens([1,2,3,4,5,6]))
# # # # #
# # # # # def count_five_letter(words):
# # # # #     counter = 0
# # # # #     for word in words:
# # # # #         if len(word) == 5:
# # # # #             counter += 1
# # # # #     return counter
# # # # #
# # # # # list=["apple", "banana", "cherry", "lemon"]
# # # # # print(count_five_letter(list))
# # # #
# # # # def sum_till_even(numbers):
# # # #     sum = 0
# # # #     for number in numbers:
# # # #         if number % 2 == 0:
# # # #             return sum
# # # #             break
# # # #         sum += number
# # # #     return sum
# # # #
# # # # print(sum_till_even([1,3,5,7,8,9]))
# # #
# # # def count_until_sam(list):
# # #     counter = 0
# # #     for i in list:
# # #         counter += 1
# # #         if i == "sam":
# # #             break
# # #     return counter
# # #
# # # print(count_until_sam(["", "", "", "sam", ""]))
#
#  def replace(s, old, new):
#      pieces = s.split(old)
#      return new.join(pieces)
#
#  def test(actual, expected):
#      if actual == expected:
#          print("PASSED")
#      else:
#          print("FAIL")
#
#  test(replace("Mississippi","i","I"),"MIssIssIppI")
#  print(replace("Mississippi","i","I"))
#
#
# def max(list):
#     highest = list[0]
#     for num in list:
#         if num > highest:
#             highest = num
#     return highest
# print(max([1,2,23,14,5]))
