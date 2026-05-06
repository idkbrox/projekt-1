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
number = input(f"Enter a number between 1 and {len(TEXTS)} to select: ")
 
x = [str(i) for i in range(1, len(TEXTS)+1)]
if number not in x:
    print("Invalid number, terminating the program..")
    exit()

selected_text = TEXTS[int(number)-1]

all_words = []
word = ""
for letter in selected_text:  
    if letter in (" ", "\n"):
        all_words.append(word)
        word = ""
    else:
        word += letter
all_words.append(word)

total_words = 0
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_strings = 0
sum_of_numbers = 0
every_word_length = []

for i in all_words:
    total_words += 1
    
    if i.isupper():
        uppercase_words += 1
    elif i[0].isupper():
        titlecase_words += 1 
    elif i.islower():
        lowercase_words += 1
    else:
        numeric_strings += 1
        sum_of_numbers += int(i)

    length_of_word = 0 
    for letter in i:
        if letter not in (",", "."):
            length_of_word += 1
    every_word_length.append(length_of_word)

final_table = " 1|"
expected_length = 1
number_of_words = 0
space = " "
while every_word_length != []:
    if expected_length == 9:
        space = ""

    if expected_length in every_word_length:
        number_of_words += 1 
        every_word_length.remove(expected_length)
    else:
        expected_length += 1
        final_table += (
            f'{"*"*number_of_words}{" "*(20-number_of_words)}'
            f'|{number_of_words}\n{space}{expected_length}|'
        )
        number_of_words = 0
final_table += (
    f'{"*"*number_of_words}{" "*(20-number_of_words)}'
    f'|{number_of_words}'
)

print(f'''----------------------------------------
There are {total_words} words in selected text
There are {titlecase_words} titlecase words in selected text
There are {uppercase_words} uppersase words in selected text
There are {lowercase_words} lowercase words in selected text
There are {numeric_strings} numeric strings in selected text
The sum of all numbers {sum_of_numbers}
----------------------------------------
LEN| OCCURRENCES |NR.
----------------------------------------
{final_table}''')
