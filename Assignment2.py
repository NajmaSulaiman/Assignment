#Q1
Values = [0, 0, 0, 0, 0, 0, 0]
print(Values)
Values[0] = 10 
Values[-1] = 10
print(Values)

#Q2
list1 = [6, 3, 8, 1, 7]
list1= list1[::-1]
print(list1)

#Q3
color=["red", "yellow", "pink", "black"]
color.insert(1,"purple")
color.pop()
color.pop()
color.insert(3,"Black")
color.append("green")
print(color)
#[‘red’, ‘purple’, ‘yellow’, ’Black’, ‘green’]

#Q4
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print(fruits.count("apple"))
print(fruits.count("strawberry"))
print(fruits.index("banana"))
print(fruits.index("banana", 4))
fruits.reverse()
print(fruits)
fruits.append("grape")
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)

#Q5
input= [23, 54, 76, 12, 90]

for i in range(len(input)):
    if (i == len(input) - 1):
        print(input[i], end="")
    else:
        print(input[i], end=" | ")
    
    

#output: 23 | 54 | 76 | 12 | 90
        
#Q6
list4=[1,3,2,2,5,0,0,0,9,8]
counter=0
for i in list4:
    if(i == 0):
        counter+=1
print(counter)

#Q7
d = "a*hj"
a=list(d)
print(a)

#Q8
b= ["p", "r", "a", "c", "t", "i", "c", "e"]
for i in b:
 print(i, end="?")

#Q9
b = "Hello World"
a = list(b)
print(a)
print(len(a))
print(a[1:11])
#print(a[-2,-5,-1])
print(a[-2:-5:-1]) 
print(a[::2])
print(a[:4])
print(a[4:])

#Q10
def cal(word_list, n):
    result = []
    for word in word_list:
        if len(word) > n:
            result.append(word)
    return result

word_list = input("Enter a list of words (separated by space): ").split()
n = int(input("Enter the minimum length (n): "))


filterr = cal(word_list, n)

print("words longer than",n,":")
print(filterr)


