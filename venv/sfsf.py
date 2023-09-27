# arr = [-4, 3, -9, 0, 4, 1]

# def plusMinus(arr):
#     # Write your code here
#     total = len(arr)
#     positive = sum(1 for n in arr if n > 0)
#     negative = sum(1 for n in arr if n < 0)
#     zero = total - positive - negative

#     print(f"{positive / total:.4f}")
#     print(f"{negative / total:.4f}")
#     print(f"{zero / total:.4f}")
        
# plusMinus(arr)

# if __name__ == '__main__':
#     def restoreString(s: str, indices: list[int]) -> str:
#         n = len(s)
#         shuffled = [""] * n  
#         print(shuffled)
        
#         for i in range(n):
#             shuffled[indices[i]] = s[i]  
        
#         return "".join(shuffled)

# print(restoreString('codeleet', indices=[4,5,6,7,0,2,1,3]))

# def value(nums: list[int], target):

#     # for i in lista:
#     #     indice = i
#     #     for c in range(i + 1, len(lista)):
#     #         if lista[indice] + lista[c] == target:
#     #             a = lista.index(lista[indice])
#     #             b = lista.index(lista[c])

#     # return a, b
#     lista_indices = []
#     for i in nums:
#         indice = i
#         for c in range(indice + 1, len(nums)):
#             if nums[indice] + nums[c] == target:
#                 a = nums.index(nums[indice])
#                 b = nums.index(nums[c])
#                 lista_indices.append(a)
#                 lista_indices.append(b)


#                 return lista_indices
                    

# print(value([2,7,11,15], 9))

print([0] * 26, ord('a'))



# def fn(i):
#     if i > 3:
#         return

#     print(i)
#     fn(i + 1)
#     print(f"End of call where i = {i}")

# fn(1)

# def polindromo(strs: str) -> bool:
#     left, right  = 0, len(strs) - 1

#     while left < right:
#         if strs[left] != strs[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# def check_for_target(nums, target):
#     left = 0
#     right = len(nums) - 1

#     while left < right:
#         # curr is the current sum
#         curr = nums[left] + nums[right]
#         if curr == target:
#             return True
#         if curr > target:
#             right -= 1
#         else:
#             left += 1
    
#     return False

# nums = [1, 2, 4, 6, 8, 9, 14, 15]

# print(check_for_target(nums=nums, target=13))

def reverseString(s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        new_string = []
        
        while left < right:
            new_string.append(s[right])
            right -= 1
            
            
        return new_string


print(reverseString(['h','e','l','l','o']))