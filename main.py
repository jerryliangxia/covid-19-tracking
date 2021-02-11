# comment puts a space inbetween the segments
def name_function():
    # everything in the function is indented
    print("Hello you!")

name_function()

def whichSchool(school, not_school):
    print("I study at",school," and not ", not_school)

y = "McGill"
whichSchool(y, "Concordia")

print("Where do you go to school")

def randomFact(str):
    print(str**4)


print("What...")
fav = int(input())
randomFact(fav)

fruits = ["banana","blueberry","pomegranate"]
x = fruits[0]
y = fruits[2]

fruits.append("kiwi")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits[1]="raspbery"

numFruits = len(fruits)

student= {'firstname': 'Soraya', 'lastname': 'Delacour', 'id':'260123456'}
studFirstName = student['firstname']

student['lastname']