# # for i in range(3):
# #     print(i)  # 0, 1, 2

# text = "hello world"
# reverse = ""
# for char in text:
#     reverse = char + reverse
# print(reverse)
# def print_multiplication_table(n):
#     if n <= 0:
#         print("Please enter a positive integer.")
#         return
#     for i in range(1, 11):
#         print(f"{n} x {i} = {n * i}")
# a = int(input("enter your no.: "))
# if a<100:
#     if a>= 90:
#         print("a")
#     elif a>= 80:
#         print("b")
#     elif a>=70:
#         print("c")
#     elif a>50:
#         print("d")
#     else:
#         print("e")
# else:
#     print("enter no. between 1 to 100")

# a, b, c = map(int, input("enter your three no.").split())
# if a>b:
#     max=a
# else:
#     max=b
# if max>c:
#     print(max)
# else:
#     print(c)

# a = int(input("enter your no.: "))
# if a%400==0:
#     if a%100!=0:
#         print("yes")
#     else:
#         print("no")
# elif a%4==0:
#     print("yes")
# else:
#     print("no")
# a = int(input("enter your no here: "))
# if a<= 100:
#     if a%15==0:
#         print("fizzbuzz")
#     elif a%3==0:
#         print("fizz")
#     elif a%5==0:
#         print("buzz")
#     else:
#         print("this is never divide by 3 and 5")
# else:
#     print("enter no. between 1 to  100")

# a =int(input("enter your no. "))
# result ="even" if a%2==0 else "odd"
# print(result)

# a = int(input("enter your no. "))
# c = 0
# while a!=0:
#     max=a%10
#     c +=max
#     a=a//10
# print(c)

# a = int(input("enter your no. "))
# c=0
# for i in  range(1, a+1):
#     if a%i==0:
#         c+=1

# if c == 2:
#     print("yes")
# else:
#     print("no")

# a = int(input("enter your no. "))
# c =1
# for i in range(1, a+1):
#     c *= i
# print(c)
    
# a = str(input("enter your sentence here: "))
# c = a.split()
# t = []
# for i in c:
#     f = ""
#     for char in i:
#         f = char + f
#     t.append(f)
# result = " ".join(t)
# print(result)

# text=str(input("enter your word: "))
# print(text[::-1])

# ret = ""
# for i in text:
#   ret = i +ret
# print(ret)
  
# text = str(input("enter your word here: "))
# for i in range(len(text)):
#   if text[i] in text[:i]:
#     print(text[i])
#     break


# texp = input("enter your word ")
# text = list(texp)
# b =len(text) -1
# c = 0 
# while c<b:
#     text[c], text[b]=text[b], text[c]
#     c+= 1
#     b -=1
# bet = "".join(text)
# print(bet)

  
   
# for i in range(1, 11):
#   for j in range(1, 11):
#     print(f"{i}x{j}={i*j}")


# a = [1, 2, 3, 4]
# b = [4, 5, 6, 7]
# for i in range(len(a)):
#   for j in range(len(b)):
#     if a[i] == b[j]:
#       print(a[i])

# a = [1, 2, 3, 4]
# b = [1, 3, 5, 4]
# for c, d in zip(a, b):
#   if c == d:
#     print(c)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# c = [g*g for g in a if g%2==0]
# print(c)

# a = [1, 2, 34, 65, 67,78, 54, 34]
# list =[]
# for i in a:
#   if i%2==0:
#     list.append(i*i)
# print(list)

# a = ["apple", "banana", "cheery", "grapes", "sandal", "peach", "mango"]
# ret = {}
# for word in a:
#   ret[word]= len(word)
# print(ret)

# a = str(input("enter your sentence: "))
# c = a.split()
# ret = {}
# vowels = "aeiou"
# for pet in c:
#   for char in pet:
#     if char.lower() in vowels:
#       ret[pet] = char
# print(ret)

# a = "Hello welcome to the world of Python"
# c = {char for char in a.lower() if char in "aeiou"}
# print(c)

# a = ["apple", "banana", "cherry"]
# c = {word: len(word) for word in a}
# print(c)

# p = int(input("enter your no. "))
# a, b = 0, 1
# for i in range(p):
#     print(a, end=" ")
#     a, b = b, a + b

# p=int(input("enter your no. "))
# a, b =0, 1
# for i in range(p):
#     a = a+i
#     b= a+b
#     print(b)


# p = int(input("enter your no. "))
# a = 0
# b = 1
# for i in range(p):
#     c = 
#     print(c)
    


  

# import itertools
# lst = [1, 2, 3]
# comb = list(itertools.combinations(lst, 2))
# print(comb)

# from itertools import cycle
# lst = ["a", "b", "c"]
# cyc = cycle(lst)
# for i in range(10):
#     print(next(cyc))


# from itertools import cycle
# a = [1, 56, 34, 56, "apple", "banana"]
# c = cycle(a)
# for i in range(90):
#     print(next(c))

# a = {"apple", "banana", "cherry", "peach", "mango"}
# c = {"Jerry", "papaya", "peach", "banana", "orange"}
# print(a.difference(c))

# import numpy as np

# arr = np.array([1, 2, 3, 4])
# print(arr)        # Output: [1 2 3 4]
# print(arr * 2)    # Output: [2 4 6 8] (element-wise operation)

# matrix = np.array([[1, 2], [3, 4]])
# print(matrix)
# # Output:
# # [[1 2]
# #  [3 4]]

# print(matrix.shape)  # (2, 2) – 2 rows, 2 columns

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(a + b)  # Output: [5 7 9]

# Fixed size list (simulate static array)
# static_arr = [0] * 5  # Size is 5, all values initialized to 0

# # Assigning values
# static_arr[0] = 10
# static_arr[1] = 20

# print(static_arr)  # Output: [10, 20, 0, 0, 0]

# # Trying to add more elements manually
# try:
#     static_arr[5] = 60  # IndexError: list assignment index out of range
# except IndexError as e:
#     print("Error:", e)

# import numpy as np
# print(np._version_)

# # Packing
# point = (10, 20)

# # Unpacking
# x, y = point
# print(f"x = {x}, y = {y}")


# a = input("enter your no. ")
# sum =0
# for i in a:
#     sum += int(i)
# print(sum)
# print(i)


# num = input("Enter a number: ")
# sum_of_digits = 0

# for digit in num:
#     sum_of_digits += int(digit)

# print("Sum of digits:", sum_of_digits)

# arr = [1, 2, 3, 2, 1]

# left = 0
# right = len(arr) - 1
# is_palindrome = True

# while left < right:
#     if arr[left] != arr[right]:
#         is_palindrome = False
#         break
#     left += 1
#     right -= 1

# print("Palindrome:", is_palindrome)  # Output: True

# arr = [2, 45, 12, 2, 67, 6]
# t = len(arr)
# for i in range(t):  (t-i-1 ka matab hota h reverse no means 5, 4, 3, 2, 1)
#     for j in range(0, t-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j], arr[j+1]=arr[j+1], arr[j]
# print(arr) 

# arr = [23, 45, 6, 13, 89, 4, 34]
# for i in range(len(arr)):
#     t = i
#     for j in range(i+1, len(arr)):
#         if arr[j]< arr[t]:
#             t = j
#     arr[i], arr[t]=arr[t], arr[i]
# print(arr)


# arr = [23, 4, 5, 27, 87, 12, 90]
# for i in range(1, len(arr)):
#     k = arr[i]
#     j = i-1
#     while j>=0 and arr[j]>k:
#         arr[j+1] = arr[j]
#         j-=1
#     arr[j+1] = k
# print(arr)

# def ch(arr):
#     if len(arr)>1:
#         bik = len(arr)//2
#         sep = arr[:bik]
#         sap= arr[bik:]
#         ch(sep)
#         ch(sap)
#         i=j=k=0
#         while i<len(sep) and j<len(sap):
#             if sep[i] < sap[j]:
#                 arr[k] = sep[i]
#                 i+=1
#             else: 
#                 arr[k] = sap[j]
#                 j+=1
#             k+=1
#         while i< len(sep):
#             arr[k]= sep[i]
#             i+=1
#             k+=1
#         while j<len(sap):
#             arr[k]=sap[j]
#             j+=1
#             k+=1
#     return arr
# print(ch([23, 45, 6, 21, 78, 4, 19]))


# def pie(arr):
#     if len(arr)<=1:
#         return arr
#     p = arr[0]
#     left = [x for x in arr[1:] if x < p]
#     right = [x for x in arr[1:] if x>=p]

#     return pie(left)+ [p] + pie(right)
# print(pie([34, 2, 89, 5, 67, 45, 23]))


# def p(a):
#     if len(a)<=1:
#         return a
#     c = a[0]
#     d = [x for x in a[1:] if x<c]
#     e = [x for x in a[1:] if x>=c]
#     return p(d) + [c] + p(e)
# print(p([12, 23, 45, 97, 1, 34, 19]))

# arr = [23, 45, 26, 98, 18, 46, 90]
# t = 46
# for i in range(len(arr)):
#     if arr[i] == t:
#      print(i)
#     else:
#         print("not")

# def fact(arr, c):
#     low = 0 
#     high = len(arr) -1
#     while low<= high:
#         mid = (low+high)//2
#         if arr[mid] == c:
#             return mid
#         elif c< arr[mid]:
#             high = mid -1
#         else:
#             low = mid+1
#     return -1
# print(fact([12, 24, 35, 46, 78, 79], 78))


# arr = [12, 34, 56, 78, 79]
# t = 79
# low =0
# high = len(arr)-1
# while low<=high:
#     mid =(low+high)//2
#     if arr[mid] == t:
#         print(mid)
#         break
#     elif t<arr[mid]:
#         high = mid -1
#     else: 
#         low = mid +1
# else:
#    print(-1)

# a = [[1, 2, 3,], [4, 5, 6], [7, 

# r, c = 15, 15
# m = []
# for i in range(1, r):
#     r = []
#     for j in range(1, c):
#         r.append(i*j)
#         m.append(r)
# print(m)

# r, c= 2, 2
# m = []
# for i in range(r):
#     r = list(map(int, input("enter your array ").split()))
#     m.append(r)
#     for r in m:
#         print(r)

# m = [[1, 2, 3, 4],[34, 45, 56, 32], [23, 87, 98, 76]]
# for r in m:
#     for i in r:
#         print(i, end=" ")
#     print()

# m = [[2, 3, 4], [34, 12, 90], [34, 67, 8]]
# for r in m:
#     for i in r:
#         print(i, end=" ")
#     print()

# for i in range(len(m)):
#     for j in range(len(m[i])):
#         print(f"m[{i}][{j}] = {m[i][j]}")

# r, c = 3, 4
# m = [[(i*j)**2 for i in range(c)] for j in range(r)]
# print(m)

# a = [[1, 2], [3, 4]]
# b = [[5, 6], [8, 9]]
# for i in a:
#     for j in i:
#         print(j, end=" ")
#     print()
# p = []
# for i in range(len(a)):
#     c = []
#     for j in range(len(a[0])):
#         c.append(a[i][j] + b[i][j])
#     p.append(c)
# print("matrix sum is ")
# for r in p:
#     print(r)

# a = [1, 34, 5,78, 1, 34, 34]
# def s(a):
#   b = set(a)
#   c = list(b)
#   print(c)
# s([1, 23, 67, 1, 23])

# def count_frequency(lst):
#     freq = {}
#     for item in lst:
#         if item in freq:
#             freq[item] += 1
#         else:
#             freq[item] = 1
#     return freq
# print(count_frequency([1, 2, 3, 4, 3, 1, 2, 3, 4, 1, 1]))



# for i in range(1, n + 1):
#     r = " "*(n-i)
#     for j in range(1, i+1):
#         r += str(j) + " "
#     print(r)


# e=[
#     {
#         "id":1,
#         "name":'payal Dhiman',
#         "age":20,
#         "email":"payaldhiman24@navgurukul.org",
#         "role":"frontend developer",
#         "department":"ENgineer",
#     }

# ]
# nid=2
# def s():
#     print("employee application")
#     print("1. add e, 2. view e, 3. update e, 4. delete e, 5. exit")
# def c():
#     global nid
#     print("add e")
#     name=input("enter your name: ").strip()
#     age=int(input("enter your age: "))
#     email=input("enter your email: ").strip()
#     role=input("enter your role: ").strip()
#     department=input("enter your department: ").strip()
#     e.append({
#         "id":nid,
#         "name":name,
#         "age":age,
#         "email":email,
#         "role":role,
#         "department":department,
#     })
#     nid+=1
#     print("e added successfully")
#     print(f"employee id: {nid}")
# def r():
#     print("view e")
#     if not e:
#         print("no e found")
#         return
#     for i in e:
#         print(f"id: {i['id']}, name: {i['name']}, age: {i['age']}, email: {i['email']}, role: {i['role']}, department: {i['department']}")
# def u():
#     print("update e")
#     id=int(input("enter your id: "))
#     f=False
#     for i in e:
#         if i['id']==id:
#             name=input("enter your name: ").strip()
#             age=int(input("enter your age: "))
#             email=input("enter your email: ").strip()
#             role=input("enter your role: ").strip()
#             department=input("enter your department: ").strip()
#             if name:
#                i['name']=name
#             if age:
#                 i['age']=age
#             if email:
#                 i['email']=email
#             if role:
#                 i['role']=role
#             if department:
#                 i['department']=department
#             print("e updated successfully")
#             break
#         if not f:
#             print("mental peace you forget something")
#             return
#     print("e not found")
# def d():
#     print("delete e")
#     id=int(input("enter your id: "))
#     for i in range(len(e)):
#         if e[i]['id']==id:
#             e.remove(e[i])
#             print("e deleted successfully")
#             return
#     print("e not found")
# while True:
#     s()
#     ch=int(input("enter your choice: "))
#     if ch==1:
#         c()
#     elif ch==2:
#         r()
#     elif ch==3:
#         u()
#     elif ch==4:
#         d()
#     elif ch==5:
#         print("exit")
#         break
#     else:
#         print("invalid no. you try don't you find what written in starting")


# # a=[[1, 2, 4], [3, 4, 5]]
# # print(a[0][1])

def re(a):
    if a==0:
        return -1
    elif a==1:
       return 1
    else:
        return re(a-1)+re(a-2)
print(re(10))