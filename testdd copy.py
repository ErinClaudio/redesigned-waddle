from math import *  ##this is a module##

'''
vari_name = " erin"
char_age = 23

tom = "this" +vari_name + "is here" +str(char_age)+ "."
print (tom)


vari_name = " tom"
char_age = 35

tom = "this is now" +vari_name + " is here" + str(char_age)+  " ."
print (tom.replace("now","later"))

print ("erin\nclaudio")

my_num=(23232,13455,3452452,23452345)
print (max(my_num))

my_num=43.7
print(sqrt(my_num))


name = input("what is the weather going to be today? good or bad: ")
feelings = input("what is your mood going to be today? good or bad: ")

print( "hello " + name + "!,  well that sounds " + feelings+ ".")


num_1 = input(" hello user1 please pick a whole number 1 - 100, thank you:")
num_2 = input(" hello user2 please pick a whole number 1 - 100, thank you:")
result = float(num_1) + float(num_2)

print(result)


color = input(" please pick a color:")
plural_noun = input(" please pick a plural noun:")
celebrity = input (" please pick a celebrity:")


print("roses are " +color)
print(plural_noun + "      are blue")
print("I love " +celebrity+ ".")


teams = ["bulls","bulls", "lakers", "hornets","pistons","blazers"]
numbers =[2,3,4,6,3,5,7,4,3,2,]
teams.sort()


coordinates = (4,5)


is_male = True

is_tall = False


if is_male and is_tall: 
    print("fuck ya tall person")
elif is_male and not(is_tall):
    print("you a short dude slut")
else:
    print("fuck no hoe")


def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(34,57,68))


num1 = int(input("please enter a whole number 1 - 100:"))
num2 = int(input("please enter a whole number 1 - 100:"))
operator = input("please enter a operator; +,-, *, /")


if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print("you did something incorrect ")



monthConversions ={
    "jan": "January", "Feb":"Februaury", "Mar":"March", "apr":"april", "may":"may"
}

print (monthConversions.get("Jan", "not a valid key"))


i = 1 

while i <= 10:
    print(i)
    i += 1

print ("done")


secert_word= "time"
guess= "  "
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != secert_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("please take a guess as to what the secert word is :    ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guess , too bad")
else:
    print ("holy shit you did it")


friends = ["hohaf" , "ajdfljasdf","hhihi"]

for f in range(5):
    print(f)



number_list = [
[1,2,3],
[4,5,6],
[7,8,9]
]

for ran in number_list:
    for ran2 in ran:
        print(ran2)

'''

def translator(phrase):
    result = " "
    for vowel in phrase:
        if vowel.lower() in "aeiou":
            if vowel.isupper() in "aeiou":
                result = result + "G"
            else:
                result = result + "g"
            
        else:
            result = result + vowel
    return result
 
print(translator(input("please enter a word:  ")))







'''

print(2**5)


def raise_to_power(base_num, pow_num):
    result = 1
    for exo in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,2))
'''







