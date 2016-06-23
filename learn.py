

#10 - Slicing

example = [0,1,2,3,4,5,6,7,8,9]

example[4:8]
example[-5:-1]
example[-5:]
example[:]
example[1:8:2]
example[10:0:-2]
example[::-2]

#11 - Editing Sequences

[7,4,5]+[4,6,5]
'bucky' + 'roberts'
'bucky'*10
21*10
[21]*10

name = 'roastbeef'
'z' in name
'r' in name

family = ['mom', 'dad', 'bro']
'sis' in family
'mom' in family

# 12 - More List Functions

numbers = [8,1,4,17,28,165,7]
len(numbers)
max(numbers)
min(numbers)

list('bucky')

numbers
numbers[3] = 77
numbers
del numbers[3]

# 13 - Slicing Lists

example = list('easyhoss')
example

example[4:]= list('baby')
example

example[4:]= list('racecars')
example

example = [7,8,9]
example

example[1:1] = [3,3,3]
example

example[1:5] = []
example

# 14 - Intro to Methods

face = [21,18,30]
face
face.append
face

apples = ['i', 'love', 'apples', 'apples', 'now']
apples

apples.count('apples')
apples.count('bow')

one = [1,2,3]
one

two = [4,5,6]

two

one.extend(two)

# 15 - More Method

say = ['hey', 'now', 'brown', 'cow']
say
say.index('brown')
say.insert(2,'hoss')
say
say.pop(1)
say
say.remove('brown')
say
say.reverse()
say

#16 - Sort and Tuples

new = [32, 54, 22, 7, 98, 1]
new
new.sort()
new

sorted('Easyhoss')

41, 42, 32, 54
bucky = (32, 43, 43, 54)
bucky
bucky[2]

#15 - String n Stuff

bucky = "Hey there %s, hows your %s"
varb = ('betty', 'foot')
print bucky % varb
varc = ('tuna','fin')
print bucky % varc

example = "Hey now bessie nice chops"
example
example.find('bessie')
example.find('chops')

seperator = 'hoss'

# 18 - Cool String Methods

sequence = ['Hey', 'there', 'bessie','hoss']
sequence
glue = 'hoss'
glue.join(sequence)

randstr="I wish i had NO sausage"
randstr
randstr.lower()

truth = "I love old women"
truth
truth.replace('women', 'men')

# 19 - Dictionary

book = ('Dad':'Bob', 'Mom':'Lisa', 'Bro':'Joe')
book
book('Dad')
ages = ('Dad':'42', 'Mom':'87')
ages
ages('Dad')
book.clear()
book
tuna=ages.copy()
tuna
tuna.has_key('Mom')
tuna.has_key('Apples')

# 20 - If Statement

tuna="fish"
if tuna=="fish":
    print 'this is a fish alright'
    

if tuna=="bass":
    print 'this is a bass alright'

# 21 - else and elif

tuna="fish"
if tuna=="bass":
    print 'this is a bass alright'
else:
    print 'I dont know what this is'

tuna="fish"
if tuna=="bass":
    print 'this is a bass alright'
elif tuna=='salmon':
    print 'I hope I dont get poison'
elif tuna=='fish':
    print 'I know it is fish'
else:
    print 'I dont know what this is'

# 22 - Nesting Statements

thing = "animal"
animal = "cat"

if thing == "animal":
    if animal == "cat":
        print 'this is a cat'
    else:
        print "Idk what animal this is"
else:
    print "idk what this is"

    if thing == "animal":
    if animal == "dog":
        print 'this is a dog'
    else:
        print "Idk what animal this is"
else:
    print "idk what this is"

# 23 - Comparison Operators

9 < 7
9<= 9
9!=3

one = [21, 22, 23]
two = [21, 22, 23]
one == two
one is two
one is one

three = four = [2, 3, 4]
three is four

pizza = "pizzahut"
'p' in pizza
'z' in pizza

# 24 - And and Or

"dog" < "cat"
example  = 5
if example > 3 and example < 10:
    print 'num is between 3 and 10'
    
if example > 3 and example < 4:
    print 'num is between 3 and 4'

if example > 3 or example < 4:
    print 'this works'

# 25 - For and While Loops
    
raw_input("Press<enter>")

