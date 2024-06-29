lst=[1,2,3,4,5,6,8,10]

def oddeven(lst):

    print([num for num in lst if num%2==0])

    print([num for num in lst if num%2!=0])

oddeven(lst)
 







# =================================
# odd=[]
# even=[]

# def evenodd(lst):
#     for num in lst:
#         if num%2==0:
#             even.append(num)
#         else:
#             odd.append(num)
#     return even,odd

# even,odd=evenodd(lst)

# print("even:",even)
# print("odd:",odd)


