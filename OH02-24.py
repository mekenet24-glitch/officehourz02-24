print("hello world")

age = 25
year = 2026

# operators (+, -, *, /, //, %, **)

#
print(age+5) 

#subtracting

print(age-5)

#multiplying
print(age*3)
#dividing
print(age/4)

#remainder
print(age%4)

#power to
print(age**2)

#string 
name = "Mesganaw"
otherName = 'Abraham'

sentence = "This is a sentence"
exampleSentence = 'This is another sentence'
doYouLikeCottageCheese = "I don't like cottage cheese 42.True."

print(name)
print(otherName)
print(sentence)
print(exampleSentence)
print(doYouLikeCottageCheese) 

#Lists
MesganawsGradesInSchool = ['A', 'D', 'D-', 'C' ]
MesganawsGradesInSchool.append("B+") 
print(MesganawsGradesInSchool) 
MesganawsGradesInSchool.append("A-")
print(MesganawsGradesInSchool)

#dictionaries
student = {
    "name": "Mesganaw",
    "age": 25,
    "favoratie activity": "pepsi" ,
    "favorite color": "blue",
    "grades": ['A', 'D', 'D-', 'C']
}

student1 = {
    "name": "beth",
    "age": 40,
    "favoratie activity": "jogging" ,
    "favorite color": "white",
    "grades": ['A', 'D', 'D-', 'C']
}

print(student1)
print(student1["name"])
print(student1["age"])
print(student1["favoratie activity"])    
print(student1["favorite color"])
print(student1["grades"])


#For loop
for eachElement in range(1, 11):
    print(eachElement)

#short hand for loop
for i in range(1, 11):
    print(i)

for eachgrade in MesganawsGradesInSchool:
    print(eachgrade)

for i in MesganawsGradesInSchool:
    print(i)

# for applesCommicsBoomerang in MesganawsGradesInSchool:
#     print(applesCommicsBoomerang)

for eachElement in range(1, 21):
    if eachElement % 2 == 0:
        print(eachElement)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)    

numbers = [1, 57, 85, 32, 0]
total = 0
for num in numbers:
    total += num
print("The total is:", total)    

for i in range(5, 0, -1):
    print(i)    

names = ["Colton", "Mesganaw", "Beth"]   
for name in names: 
    if len(name) > 5:
        print(name)    

for num in numbers:
    if num % 2 == 0:
        print(num, "is even")  
    else:
        print(num, "is odd")