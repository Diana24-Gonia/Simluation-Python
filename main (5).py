"""
Testing in Python
"""
#testing program in python
the_family_is_wonderful = True
if the_family_is_wonderful:
    print("i believe my family is wonderful!")
    
#using  python interpreter as a calculator and displaying through print() funtion
print("2.)whole_gasto pamalengke.\n")
print(50 + 25)
print(100 - 25)
print(35 * 100)
print(1000/20)
print(100- (200 * 300 ) + 400 *((500/600)+700))
print(100//15)
print(1**20)
print("\t# gihatag ni mama para pamalengke")
print("n")

#using the "=" to assign a value
print("kataason sa lamesa og kalaparon sa lamesa")
kataason = 30
kalaparon = 50
print(kataason/kalaparon)

#returning float value with mixed operands
print(55*25-80)
print(55+25*80)
print(1*2+3/4-5)

#interactive string and using python r to denotes raw string
print("Boy I love you\; Girl I love you too!")
player1 = "Boy First pick = chocolates \n Girl Second pick = eating the chocolates"
print(player1)
print("c: boy_name_is_kalix") # \n is treated as newline
print(r"c: girl_name_is_luna") # the r denotes raw 
print ("Boyfriend and Girlfriend")

#string literal spanning multiple lines adding \ for preventing end of line
print("6.) string literal spanning multiple lines adding \ for preventing end of line.\n")
print("""\ Usage: thingy [pick] -h read the message -H sender receive the message""")

#string contactication using + operator and repeating using * operator
print(1* "My father is a driver!" +" I am proud of him!")
print(1* "My mother works hard!" +" Shes my imspiration!")
print(1* "I am proud of myself!" +" Top student!")

#automatic contactication of two or more string literals
player = ("The first pro player!" "n The second pro player" "n The last pro player!")
print(player)
pick = ("First pick!" "nSecond pick." "nThird pick!")
print(pick)

#string indexing as immutable
print("9.) String indexing aa immutable.\n")
Diana = " ALPHABETICAL"
print(Diana [1])
print(Diana [2])
print(Diana [3])
print(Diana [4])
print(Diana [5])
print("\n")
print(Diana [6])
print(Diana [7])
print(Diana [8])
print(Diana [-9])
print(Diana [-10])
print(Diana [-11])
print(Diana [-12])
print(Diana [-4])
print("\t{>_>}\n")
#print (pinoy [9])

#string index slicing
print(Diana [0:5])
print(Diana [5:8])

#string index selected slicing 
print(Diana [:0]) # characters from the beginning to position 2 (excluded)
print(Diana [0:]) # characters from the position 4 (included) to the end
print(Diana [-3:]) # characters from the second-last (included ) to the end
print(Diana [:1] + Diana [-1:])
print(Diana [:11] + Diana [-1:])

#creating a new string data 
print("10.) Creating a new string data.\n")
Diana = "butuan city" + Diana [1] + Diana [2] + Diana [3] + Diana [4] + Diana [5] + Diana [6] + Diana [7]
print(Diana)

#using the len() built-in function
print(len(Diana))

#exploring list
grades = [93,94,98,97,96,90,91,91]
print(grades)

#indexing a list 
names = ["danica","ruffa","rachel","roged","regel"]
print(names [0])
print(names [-1])
print(names [1:2])
print(names [-4:3])

#slicing indexing of list 
numbers = [10,20,30,40,50,60,70,80,90,100]
print(numbers [3])
print(numbers [7])
print(numbers [-2])
print(numbers [-5])

#exploring the multiple nature of list
length = [50,100,200,300,400,500]

#item in one of this list is wrong
print(length)
print(1 ** 10)
print(2 ** 10)
print(3 ** 10)
print(4 ** 10)
print(5 ** 10)
print(6 ** 10)
print(7 ** 10)
print(8 ** 10)
print(9 ** 10)
print(10 **10)
length [5] = 4 ** 10
print(length)

#adding new value to the end of the list using the append() method 
total = 8 ** 10
length.append (total)
print(length)
length.append (9 ** 10)
print(length)

#assigning to slices, changing sizes, and cleaning a list 
abakada = ["ba","be","bi","bo","bu"]
print(abakada)
abakada [1:3] = ["ba","be","bi"]
print(abakada)
abakada [-2:5] = []
print(abakada)
abakada [:] = []
print(abakada)

#applying the len() built-in functiom to lists
favorite_abakada = ["Pa","Pe","Pi","Po","Pu","Ha","He","Hi","Ho","Hu"]
print(len(favorite_abakada))

#list within lists, a nested lists
friends1 = ["danica","ruffa","rachel","rogielyn","regel"]
friends2 = ["erika","abby","jeevan","Vincent","Charles"]
friends3 = ["Ariana","Zarwin","raffy","Anjun"]
print(friends1)
print(friends2)
print(friends3)
friends_nest = [friends2, friends3, friends1]

#creating a nested lists
print(friends_nest)
print(friends_nest [1])
print(friends_nest [2][1])
print(friends_nest [1])
print(friends_nest [2][4])
print(friends_nest [1])
print(friends_nest [2][3])

#single line multiple value assignment
total1, total2 = 20,15
print("\n")
print(total1)
print(total2)
print("\n")

#itering multiple assigned value
while total1 <20:
    print(total1)
    total1, total2 = total2, total1/ total2
    print("\n")
    
#using the keyword argument end in the point() function to avoid newline after the output
b2, b1 = 5,10
while b2<10:
    print(b2, end = " ")
    b2, b1= b1, b2 * b1
    
    c2, c4 = 3,5
while c2<10:
    print(c2, end = " ")
    ('c2,c4 = c2*c4')


