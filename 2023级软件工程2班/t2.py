# # # # str1,str2 = input().split(',') # hello,l
# # # # print(str1)
# # # # print(str2)
# # # # # ['h', 'e', 'l', 'l', 'o']
# # # # # ['l']
# # # # str1_list = list(str1)
# # # # # str2_list = list(str2)
# # # # print(str1_list)
# # # # # print(str2_list)
# # # # count = 0
# # # # for i in range(len(str1)):
# # # #     if str1_list[i] == str2:
# # # #         count += 1
# # # # print(count)


# # # # str1,str2 = input().split(',') # hello,l
# # # # count = str1.count(str2)
# # # # print(count)

# # # # str1,str2 = input().split(',')
# # # # str1_list = list(str1)
# # # # str2_list = list(str2)
# # # # count = 0
# # # # for i in range(len(str1)):
# # # #     if str1_list[i] == str2_list[1]:
# # # #         count += 1
# # # # print(count)



# # # # numbers = input().split(',')
# # # # nums = sorted(list(map(int,numbers)))
# # # # print(nums)

# # # # n = len(nums)
# # # # for i in range(n-1):
# # # #     min_index = nums[i]   
# # # #     for j in range(i+1,n):
# # # #         if nums[j] > min_index:
# # # #             min_index = nums[j]
# # # #     nums[i],nums[min_index] = nums[min_index],nums[i]
# # # # print(nums[min_index])
    


# # # # my_tuple = ("apple","banana","cherry")
# # # # print(my_tuple[1])


# # # # year=2024
# # # # if(year%4==0 and year %100!=0(year % 400==0)):
# # # # print("是闰年")
# # # # else:
# # # # print("不是闰年")

# # # '''
# # # x * 0.2 + y * 0.2 + z * 0.6 = 100
# # # 10 + 10
# # # 16 + 35*0.2 + ?*0.6 = 60   ---> 47   54  61-62
# # # x*100% = 60
# # # '''


# # # # n=17
# # # # is prime=Ture
# # # # for i in range(2,n):
# # # # if n % i==0
# # # # is_prime=False
# # # # break
# # # # if is_prime:
# # # # print("是质数")
# # # # else:
# # # # print("不是质数")



# # # # my_dict={"a":[1,2,3],"b":[4,5],"c":[6]}
# # # # list j,i,q
# # # # a[i]=[1,2,3]
# # # # b[j]=[4,5]
# # # # c[q]=[6]
# # # # result=a[i]+b[j]+c[q]
# # # # print("result")


# # # def merge_sort(arr)
# # #     if len(arr)<=1:
# # #         return arr[0]
# # #     mid=len(arr)
# # #     left=merge_sort(arr[:mid])
# # #     right=merge_sort(arr[mid:])
# # #     return merge(left,right):
# # #     result=[] 
# # #     i=j=0
# # #     while i<len(left) and j<len(right):
# # #     if left[i]<right[j]:
# # #         result.append(left[i])
# # #         i+=1
# # #     else:
# # #         result.append(right[:j])
# # #         j+1
# # #         result.extend(left[i:])
# # #         input_str=input()
# # #         arr=list(map(int,input_str.split(',')))
# # #         sorted_arr=merge_sort(arr)
# # #         print('').join(map(str,sorted_arr))

# # # x = list(map(int,input().split(',')))
# # # y = list(map(int,input().split(',')))
# # # print(x+y)


# # # set_A = {12, 22, 33, 1, 25}
# # # list_A = list(set_A)
# # # for element in list_A:
# # #     print(element)


# # # set_A = {1, 2, 3, 4} 
# # # set_B = {3, 4, 5, 6}
# # # set1=set_A|set_B
# # # print(set1)

# # # ZeroDivisionError: integer modulo by zero
# # # num = 17
# # # is_prime = True
# # # for i in range(2,num):
# # #     if num%i == 0 :
# # #         is_prime = False
# # #         break

# # # if is_prime:
# # #     print("是质数")
# # # else:
# # #     print("不是质数")


# # # my_dict = {"a": [1, 2, 3], "b": [4, 5], "c": [6]}

# # # n = len(my_dict)

# # # for i in range(0,len.my_dict):
# # #     n=value.my_dict
# # #     for j in range(0,len.my_dict):
# # #     n=new_dict
# # # print(new_dict)



# # num = int(input("enter a 正整数"))
# # # for i in range (num):
# # #     if num % i = 0 :
# # #         if i != 1 :
# # #             if i != num :
# # #                 print("不是素数")
# # #                 break

# # # else :
# # #     print("是素数")


# # arr=list(int,input.split(',')))
# # a=int(input("请输入一组整数，英文逗号分隔："))


# # for i in range(0,len.arr):
# #     arr[i]=arr[len.arr-i]
# #     if i>len.arr-i:
# #         break
# # print(arr)



# # all=0
# # i = 1
# # while i<=100:
# #     all=all+i
# #     i += 1
# # print(all)



# my_list=[1,3,5,7,9]
# for i in my_list:
#     per value of i

# for i in range(len(my_list)):
#     i ==== 0 1 2 3 ...
#     per index of mylist


# for i in range(my_list):
#     my_list[i]=my_list[i] * 2
# print(my_list)


# n=int(input("输入一个正整数n:"))
# all=0
# for i in range(1,n+1):
#     all=all+i
# print(all)

'''
3 4 
1,4,7,11 
2,5,8,12 
3,6,9,16 
5

[(1, 2, 5), (3, 5, 6)]
'''
area = [(1,4,7,11),(2,5,8,12),(3,6,9,16)] # 邻接矩阵[[1, 2, 3], [4, 5, 6], [7, 8, 9]] [(1, 3), (2, 5)]
areas = {0:(1,4,7,11),1:(2,5,8,12),2:(3,6,9,16)} # 邻接表

area = []
ord = list(map(int,input().split(" ")))
n = ord[0]
m = ord[1]
for i in range(n):
    per_line = tuple(map(int,input().split(",")))
    area.append(per_line)
print(area)
