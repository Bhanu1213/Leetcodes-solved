s="(){}}{"
se=[]
pair={")":"(","}":"{","]":"["}
for i in s:
    if i in "([{":
        se.append(i)
    elif i in ")]}":
        s!=[]
        if se and se[-1]==pair[i]:
            se.pop()
        else:
            print(False)
            break
print(se)
print(len(se)==0)

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         mapping = {
#             ')': '(',
#             '}': '{',
#             ']': '['
#         }

#         for char in s:
#             if char in mapping:
#                 top = stack.pop() if stack else '#'
#                 if mapping[char] != top:
#                     return False
#             else:
#                 stack.append(char)

#         return not stack

        