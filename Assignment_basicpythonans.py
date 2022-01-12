#1)Prepare a list having the numbers present in table of 2(till 20), using Python Builtin function. Display the list.

numlist=list(range (2,20,2))
print ("table of 2 =",numlist)


# 2)Will %s formatter print the correct value of numK variable?
numK=100
numP = 5
print("There are %s Kauravas and %d Pandavas!"%(numK,numP))
# ans = yes

'''3)Mention the Builtin function for the following -
a)Function to find length of a string
b)Function to find type of the variable
c)Function to get the details of functions/methods supported by any class.'''

a = "string"
print("length of string",len(a))
print("type of variable",type(a))
print(help(a))
print(help(print))

# 4)Mark the correct answer.
num = 34
NUM = 34
if(num == NUM):
    print("Same")
else:
    print("Case insensitive")
'''a)Print answer is "Case insensitive"
b)Print answer is "Same"
c)Cannot compare num and NUM
ans= b '''

# 5) Accept a name from the user. If the length of the name is not greater than 5 then display "Name is too short" and exit from the code . Else accept age.
# If age is greater equal than 18, display "Eligible for vaccination", else between 5 and 18 display "Your turn is next". For age below 5 print "Coming soon...".
# The program should keep ON, asking name and age as long as, name length is greater than 5.

print("Hello! what is your name :")


def namelength ():
 name = input()
 if (len(name) < 5):
    print("Name is too short,enter name with more than or equal to 5 character")
    namelength()
 else:
     pass

namelength()

print(" Hi  And how old are you?")
age = int(input())
if (age>= 18):
 print("Eligible for vaccination")
elif(age>=5 and age<18):
    print("Your turn is next")
else:
    print("Coming soon...")

#6)Consider a string "Fundamental". The program should display all letters in the string except letter 'e'.

i = 0
a = "Fundamental"
while i < len(a):
    if a[i] == 'e':
        i += 1
        continue

    print('letter:', a[i])
    i += 1

'''7) Consider the following sentence -
"Rahul Dravid is the new mentor of Indian team. He is a brilliant cricketer. He is also called as 'The wall'."
Write a program that will accept a word from the user. If the word is not present in above sentence then it will ask for another word.
Once the word is found in the sentence above the program should print "Present" and then ONLY exit.'''

print("enter a word related to Rahul Dravid: ")

def findword ():
 word= input()
 sentence = "Rahul Dravid is the new mentor of Indian team. He is a brilliant cricketer. He is also called as 'The wall'."

 if word in sentence:
    print("Present!")
 else:
  print("enter another word ")
  findword()

findword()

# another method

def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
        check()
    else:
        print("YES")


# driver code
print("enter another word related to Rahul Dravid: ")
string = "Rahul Dravid is the new mentor of Indian team. He is a brilliant cricketer. He is also called as 'The wall'."
word = input()
sub_str = word
check(string, sub_str)

'''8)somenumber = 45
somestring = "zoya"
answerme = somenumber + somestring
Will the above code print "45zoya"? Give a proper explanation of the same

ans: no string cannot be combined with integer


9)A  drawing teacher has the following colors . Red , Green , Yellow , Violet. Display the colors by printing "Original colors are :"
Later her Green color is replaced with  Blue. Make changes in data structure accordingly and print "Green replaced by Blue is :" and then the
new data structure.
'''

colors= "Red , Green , Yellow , Violet"
print("Original colors are :", colors)
colors.replace("Green","Blue")
print("Green replaced by Blue is :",colors.replace("Green","Blue"))

#10) Accept 6 numbers from the user. Write a function that returns the summation of these 6 numbers.

print("enter 6 numbers")
lst = []
for i in range(0, 6):
    ele = int(input())

    lst.append(ele)  # adding the element

print(lst)
Sum= sum(lst)
print("summation od entered 6 numbers is",Sum)

'''Write True or False
a)a=3
c= "Namaste"
Since Python is a dynamically typed language. Hence we dont need to specify the datatype of variables 'a' and 'c'.

true

b)carset1 ={"santro","mercedes","nano"}
carset2 =["santro","mercedes","nano"]
carset1.pop()
carset2.pop()
print(carset1)
print(carset2)
The outputs in every execution of the program is same for carset1 and carset2. Whether Yes/No give an explanation.

ans: no output is different 
{'mercedes', 'nano'}
['santro', 'mercedes']


11)Place  either 'list' , ' tuple' , 'set'or 'dictionary' in the blanks.
A) A developer has  many 'city names' in his record. The city names can change or get replaced based on the location. He should implement
city names as a __list.
B)A lead has a record of clients( clientID , clientproject).He wants to alter some data based on the clientID. He should implement the logic
using __dictionary
C)A developer is asked to fetch capital cities data from an API. The capitals wont change or alter. They can be stored in __tuple
D)A developer was told to remove repeated data from a list of client location names. The best data structure to represent them would be
__set.
E)A developer was told to find the common Student Names from two files. Which data structure is efficient to give her the desired results?-list-
'''
