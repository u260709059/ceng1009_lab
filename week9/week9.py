# # # # # def isOdd(num):
# # # # #     if num % 2 == 0:
# # # # #         return False
# # # # #     else:
# # # # #         return True
# # # # #
# # # # # n = int(input("Enter a number: "))
# # # # # print(isOdd(n))
# # # #
# # # # def isleapYear(year):
# # # #     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
# # # #         return True
# # # #     else:
# # # #         return False
# # # #
# # # # print(isleapYear(2000))
# # # # print(isleapYear(2001))
# # #
# # # def triangular(x):
# # #     for i in range(1,x+1):
# # #         n = i*(i+1)/2
# # #         print(int(i)," ",int(n))
# # #
# # # triangular(int(input("Enter a number: ")))
# #
# # def isprime(n):
# #     if n < 2:
# #         return False
# #     for i in range(2, n):
# #         if n % i == 0:
# #             return False
# #     return True
# #
# # print(isprime(5))
# # print(isprime(10))
#
# def reverse(s):
#     result = ""
#     for char in s:
#         result = char + result
#     return result
# print(reverse("hello"))
# print(reverse("world"))
#
# def reverse_slice(s):
#     return s[::-1]
# print(reverse_slice("hello world"))
#
# def remove_all_occurrences(sub, s):
#     return s.replace(sub, "")
# print(remove_all_occurrences("ll", "hello world"))
#
# def substitute(message, key):
#     alphabet = "abcçdefghıijklmnoöprsştuüvyz"
#     result = ""
#     for char in message:
#         index = alphabet.find(char.lower())
#         if index == -1:
#             result == result + char
#         elif char.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key = "qwertyuıopğüasdfghjklşizxcvbn"
# print(substitute("Hello, World!", key))
#
# def remove_duplicates(s):
#     result = ""
#     for ch in s:
#         if ch.lower() not in result.lower():
#             result = result + ch
#     return result
#
# print(remove_duplicates("abcdabcdefgffgeaabABCD"))