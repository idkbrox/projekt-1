TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30 and the Union Pacific Railroad,
which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

import re

user_info = {
    "bob" : "123", 
    "ann" : "pass123", 
    "mike" : "password123", 
    "liz" : "pass123"
}

user = input("User: ") 
password = input("Password: ")

print("----------------------------------------")
if user not in user_info:
    print("unregistered user, terminating the program..")
    exit()
if user_info[user] == password:
    print(f'''Welcome to the app, {user} 
We have {len(TEXTS)} texts to be analyzed''')

else:
    print("wrong password, terminating the program..")
    exit()

print("----------------------------------------")
number = int(input(f"Enter a number between 1 and {len(TEXTS)} to select: "))
 

if 1 > number or number > len(TEXTS):
    print("Invalid number, terminating the program..")
    exit()

selected_text = TEXTS[number-1]
words = re.split(r'[ ,.;!?\-\n]', selected_text) 

total_words = 0
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_strings = 0
sum_of_numbers = 0
histogram = {}

for word in words:
    if word:
        total_words += 1
        
        if word.isupper():
            uppercase_words += 1
        elif word[0].isupper():
            titlecase_words += 1 
        elif word.islower():
            lowercase_words += 1
        else:
            numeric_strings += 1
            sum_of_numbers += int(word)

        try:
            histogram[len(word)] += 1 
        except KeyError:
            histogram[len(word)] = 1

print(f'''----------------------------------------
There are {total_words} words in selected text
There are {titlecase_words} titlecase words in selected text
There are {uppercase_words} uppersase words in selected text
There are {lowercase_words} lowercase words in selected text
There are {numeric_strings} numeric strings in selected text
The sum of all numbers {sum_of_numbers}
----------------------------------------
LEN| OCCURRENCES |NR.
----------------------------------------''')

histogram = dict(sorted(histogram.items()))

for i in histogram:
    print(f"{i:>2}|{("*"*(histogram[i])):<20}|{histogram[i]}")
    
