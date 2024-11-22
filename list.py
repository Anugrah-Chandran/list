'''Author:Anugrah Chandran
Date:22-11-24
Description:Program to merge the two lists in the third list such that in the merged list, all even numbers
occur first followed by odd numbers . both the even numbers and odd numbers should be in sorted order'''
list1 = [34,25,12,2,56,7,6]
list2 = [98,67,45,34,12]
combined_list = list1 + list2
even_list = []
odd_list = []
for i in combined_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
print(even_list+odd_list)