# def sub_three(x):
#     print(x-3)
#     return x-3
# sub_three(10)

# def square_x(x):
#     print(x**2)
#     return x**2
# square_x(5)

# def add(a,b):
#     print(a+b)
#     return a+b

# add(2,3)
# add(3,4)
# add(4,6)

# def compare(a,b):
#     if a>b:
#         print(a)
#         return a
#     else: 
#         print(b)
#         return b
# # compare(2,3)

# def sub_from_big(a,b):
#     result= compare(a,b)
#     if result == a:
#         print(a-b)
#         return a-b
#     else:
#         print(b-a)
#         return b-a
# # sub_from_big(2,3)

# def compare(a,b):
#     if a>b:
#         print(a)
#         return a
#     elif a == b:
#         print(a)
#         return a
#     else:
#         print(b)
#         return b
# compare(2,3)

# def multiply(a,b):
#     print(a*b)
#     return a*b

# def check_ten(a,b):
#     result= multiply(a,b)
#     if result > 10:
#         # print("bigger than 10")
#         return f"bigger than 10.the result was {float(result)}"
# "bigger than" + 10
#     else:
#         # print("smaller than 10")
#         return f"smaller than 10.the result was {float(result)}"
# result1=check_ten(3,5)
# result2=check_ten(3,2)

# print(result1)
# print(result2)


# print(f"bigger than {40}.the result {check_ten(3,5)}")

# print(f"bigger than {10}.the result was {10}")

# a = 1
# while a<=10:
#     print(f"a는 10보다 작음. a는 지금 {a} 입니다.")
#     a += 1
    
# a = 5
# while a!=0:
#     print("go!")
#     a -= 1
    
# result = 8
# state = True
# while state == True:
#     if result == 0:
#         state = False
#     else:
#         # print(result)
#         result -= 1
        
# a = 1
# while a<10:
#     print(f"a는 10보다 작다. a는 {a}다.")
#     a *= 2
    
# fruits = ["apple", "banana"]
# for fruit in fruits:
#     print(fruit)    

# def multiply(a,b):
#     print(a*b)
#     return a*b

# numbers=[1,2,3,4]
# for number in numbers: 
#     print(multiply(number,3))
    
#     # result = multiply(item,3)
#     # print(result)
    
# age = 10
# name = "kim"

# if age >= 9 or name == "block":
#     print(True)
# else:
#     print(False)
    
# age = 26
# name = "park"

# if age >=9 and name == "kang":
#     print(True)
# else:
#     print(False)
    
# age = 10

# if not age >= 9:
#     print(True)
# else: 
#     print(False)
    

# fruits = ["사과", "포도", "홍시"]

# if "사과" in fruits:
#     print("사과")
# else:
#     print("없음")
    
# 판결문_목록 = ["피고인","피해자","주문","이유","법령의 적용","판단","판사"]

# print(판결문_목록[3])

# 판결문_목록 = ["피고인","피해자","주문","이유","법령의 적용","판단","판사"]
# for item in 판결문_목록:
#     print(item)
    
# 판결문_목록.append("범죄사실")
# print(판결문_목록)

# 판결문_목록 = ["피고인","피해자","주문","이유","법령의 적용","판단","판사"]
# 판결문_목록2 = [["피고인","피해자","주문","판사"],["범죄사실","법령의 적용","판단"]]
# print(판결문_목록2[1][2])

# 판결문_목록2 = [["피고인","피해자","주문","판사"],["범죄사실","법령의 적용","판단"]]
# for 판결문_1 in 판결문_목록2:
#     for item in 판결문_1:
#         print(item)
        
# case = {"meta": ["피고인","피해자","주문","판사"], "reason": ["범죄사실","법령의 적용","판단"]}
# # print(case["meta"])
# # print(case["reason"])

# case["meta"].append("검사")
# # print(case["meta"])

# for key in case.keys():
#     print(key)
#     for item in case[key]:
#         print(item)
# for val in case.values():
#     print(val)
        
# for key,val in case.items():
#     print(key,val)
    
# case["meta"].append("검사")
# print(case)

# title3 = [["피고인","피해자","주문","판사"],["범죄사실","법령의 적용","판단"]]  
# title3[0][2]
# print(title3[0][2])

# print(title3[0].index("주문"))

# ice = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
# ice['죠스바'] = 1200
# ice['월드콘'] = 1500
# ice['메로나'] = 1300
# del ice['메로나']
# print(ice)

# print(ice)
# print(ice)
# print(ice)
# print(ice['메로나'])
# print('메로나 가격:', ice['메로나'])

# inventory = {'메로나': [300,20], '비비빅': [400,3], '조스바': [250,100]}
# print(inventory)
# print(inventory['메로나'][0])
# print(inventory['메로나'][1])
# inventory['월드콘']= [500,7]
# print(inventory.keys())
# print(inventory.values())

# for keys in inventory:
#     print(keys)

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# total = 0

# for value in icecream.values():
    
#     total = total + value
    
# print(total)

# colors = ['yellow','green','blue','purple','red','pink']
# for color in colors:
#     if color == 'blue':
#         continue(뛰어넘음)
#     elif color == 'red': 
#         break
#     else:
#         print(color)
        
# fruits = ['banana','apple','orange', 'tomato']
# vegetables = ['cucumber','eggplant','lecttuce', 'tomato']

# healthy_food = fruits + vegetables
# print(healthy_food) 

def merge_string(str1,str2):
    print(str1+str2)
    return str1+str2
merge_string('apple','mango')

team_a =[10,6,8]
team_b =[8,10,9]

def average_score(team_name):
    sum = 0
    for team in team_name:
        sum = sum + team
    result = sum/len(team_name)
    print(result)
    
average_score(team_a)
average_score(team_b)

