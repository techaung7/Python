#Print
print("Python Writing Exercise \nWritten By H.A.H")  # \n is New Line
print("\n")

print("Project 1")
print("\tProject 2") # \t is tab

print("Hello," , end="")  #Two Sentences to One
print("Nice to Meet You.")

print('If you don\'t know me,' , end="") # \ is user for ''
print("let me", end=" ")
print("introduce myself.")




#Variables
name = "Htet Aung"
age = 28
right = True
wrong = False
place = "Yangon"
father = "U Kyaw Ngwe"
father_age = 62
mother_age = 50
mother = "Daw Soe Than Khine"
brother = "Aung Kyaw Myat"
bro_age = 24
bro_work = "Developer"
home_no = 49.3
home_street= "Yate Thar St"
country = "Myanmar"
biz_name = "Binary Digital Solutions"

#Variable Types
print(type(name))
print(type(age))
print(type(right))

#Print Formatting 
print('My Name is %s.' %name ,end ="") 
print('I am %s years old.' %(age))

print('My father and my mother are %s and %s.' %(father,mother)) #Format 1
print('My father age is %s and My mother age is %s' %(father_age,mother_age)) #Format 1 (%s or %d)

print('My brother name is {},he\'s {} years old and he\'s a {}.'.format(brother,bro_age,bro_work)) #Format 2 ({} and .format)
print('Our home address is {0},{1},{2},{3}.'.format(home_no,home_street,place,country) )
print('Our business address is {biz_no},{biz_st},{biz_con}.'.format(biz_no=60,biz_st="Yadanarthukha St",biz_con="Yangon,Myanmar"))

print(f"My Business name is {biz_name}.") #Format 3 Using f


#String Slicing and Indexing 
alphabet = "ABCDEFGHIJ"
result1 = alphabet[:]   #Print All
result2 = alphabet[0:5] #Print 0-5
result3 = alphabet[-1] #Reverse
result4 = alphabet[1:6:2] #Print Start:End:Step
print(result1)
print(result2)
print(result3)
print(result4)

#String Operation 
surname = "Mr"
first_name = " Htet Aung"
last_name = " Hlaing"
name_result = surname+first_name+last_name
print(name_result)
length_name = len(name_result)
print(length_name)

#String Methods 
name_cap= name_result.capitalize()
print(name_cap)
name_small = name_result.casefold()
print(name_small)
name_count = name_result.count("H")
print(name_count)
name_checkup = name_result.isupper()
print(name_checkup)
name_checklow = name_small.islower()
print(name_checklow)

#Compare String Values in Unicode
alphabet1 = "a"
print(ord(alphabet1))  #Convert Unicode Value
alphabet2 = "b"        
print(ord(alphabet2))  #Convert Unicode Value
print(alphabet1 > alphabet2) #Compare
print(chr(98)) # Convert charatar values
print(id(alphabet1)) #ID no in Memory

#Checking alphabets in String 
name_of_singer= "EMINEM"
print("E" in name_of_singer) #E par lar 
print(name_of_singer.count("E")) #How many E?

#Operators 
#Operation ====> infix (Binary Operator) & prefix (Unary Operator)
#Binary Operator ======> a + b 
#Unary Operator ========> a ++

#Binary Operation
a = 7
b = 3
add_ans = a + b 
sub_ans = a - b 
multi_ans = a * b
expo = a**3
divide_ans1 = a / b 
divide_ans2  = a // b 
divide_ans3 = a % b 
print(add_ans,sub_ans,multi_ans,expo,divide_ans1,divide_ans2,divide_ans3)

#Comparison (>,<,>=,<=,==,!=,is,is not)
compare1 = a > b 
print(compare1)
compare2 = a < b 
print(compare2)
compare3 = a >= b 
print(compare3)
compare4 = a <= b 
print(compare4)
compare5 = a is b 
print(compare5)
compare6 = a is not b 
print(compare6)
compare7 = a == b 
print(compare7)
compare8 = a != b 
print(compare8)

#Statement and Expression
length = 12.5
width = 54 
area = length * width  #instruction or statement 
# len*wid is expression 
print(area)

#Assignment Operator 
e = 3                      #assgn 
print(f"Line 145 : {e}")
e += 3                     #add assgn 
print(f"Line 147 : {e}") 
e -= 1                     #substract assign 
print(f"Line 149 : {e}")
e *= 2                     #Multiplie assign
print(f"Line 151 : {e}")
e /= 2                     #divide assign 
print(f"Line 153 : {e}")
e //= 2                    #modulus assign 
print(f"Line 155 : {e}")
e %= 2
print(f"Line 157 : {e}")   #a kwin assign

#Logical Operators 
# and or not 
#Example of Driving Lecense 
is_over_18 = True
good_at_driving = True
give_Licnese = is_over_18 and good_at_driving    # and 
print(f"Give_Licnese : {give_Licnese}")
#Example of Student Cupon 
is_student = False
have_cupon = True
get_discount = is_student or have_cupon #or 
print(f"Get_discount : {get_discount}")
#Example of student
is_over_16 = False
university_student = not is_over_16
print(f"University_Student : {university_student}")

#Bitwise Operators (Base on Binary) 
# and ====> & 
# or  ====> |
# xor ====> ^
# not ====> ~
# left shift ====> >>
# right shift ====> << 

a = 9   # 1 0 0 1
b = 1   # 0 0 0 1
print(a & b) # and # 0 0 0 1 
print(a | b) # or  # 1 0 0 1 
print(a ^ b) # xor # 1 0 0 0 # matu 1 tu 0 
print(~a) # not ===> -(1 0 0 1 + 1) = -1 0 1 0
print(a >> 3) # left shift
print(b << 3) # right shift 


#Conditional Statement
is_over_18 = True
if is_over_18:
    print("You are available to get a license")


a = 7
b = 5
condition = a > b 
if condition: 
    print("A is greater than B")
else: 
    print("A is't greater than B")

light = "Red"

if light == "Green":
    print("Go")
elif light == "Yellow":
    print("Look")
elif light == "Red":
    print("Stop")
else:
    print("Error")

#_________________________________________________
price = 267
dis1,dis2,dis3,dis4 = 30,20,10,5
if price >= 300 : 
    print(f"You Get {dis1}% Discount." , end =" ")
    final_amt = price - (price * dis1/100)
elif 200 < price <= 300 :
    print(f"You get {dis2}% Discount.",end =" ")
    final_amt = price - (price * dis2/100)
elif 100 < price <= 200:
    print(f"You get {dis3}% Discount.",end =" ")
    final_amt = price - (price * dis3/100)
elif 0<price<=100:
    print(f"You get {dis4}% Discount.", end=" ")
    final_amt = price - (price * dis4/100)
elif price <= 0:
    print("Sorry,You can't get discount.",end=" ")
    final_amt = 0

print(f"Your Final Amount is {final_amt} Kyats.")
#___________________________________________________

#Conditional Expression 
number = -10
result = "Number is even" if number% 2 == 0 else "Number is odd" #<<======== 
print(result)

result = "Positive Number" if number > 0 else "Negative Number"
print(result)

#List Data Type 
student_data = ["Mg Mg",100,"Aung Aung",70,"Su Su",65,True] #<====== 
print(student_data[0])  #indexing of mg mg 
print(student_data[3])  #indexing of 70
student_data[2] = "Kyaw Kyaw" #Insert Kyaw Kyaw in Aung Aung 
print(student_data)

#List Indexing & Slicing 
student = ["Mg Mg","Ag Ag","Kyaw Kyaw","Hla Hla"]
second_student = student[1]
print(second_student)
thirdtolast_student = student[2:4]
print(thirdtolast_student)

#List Method 
student = ["Mg Mg","Ag Ag","Kyaw Kyaw","Hla Hla"]
first_student = student.pop(0)  #Pop Method
print(student)
print(first_student)
student.append("Su Su") #Append Method
print(student)
no_of_student =student.count("Su Su") #Count Method
print(no_of_student)
classA = ["Mg Mg","Ag Ag","Kyaw Kyaw","Hla Hla"]
classB = ["Min Min","Yu Yu","Thae Thae","Mya Mya"]
classA.extend(classB) #Extend Method
print(classA)
classA.sort() #####
print(classA)
marks = [3,5,1,7,4,8]
marks.sort() ######
print(marks)
marks.reverse() ######
print(marks)
newmarks = marks.copy() #######
print(newmarks)
newmarks.clear() ########
print(newmarks)

#Tuple Data Type >>>>> Write in ()
names = ("Aung Aung","Mg Mg","Su Su",1,2,3)

