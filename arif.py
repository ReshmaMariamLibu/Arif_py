from sys import argv

script , filename = argv

txt = open(filename)
data = txt.read()

# calculates word count , char count and sentence count
word_count = len(data.split()) # .split() method splits the text into words. The len() function then counts the number of words.
char_count = len(data)  # counts the total number of characters in the text
sentence_count = data.count('.') + data.count('!') + data.count('?') #

#prints the word count , character count and sentence count
print(f"Word count is: {word_count}")
print(f"Character count is: {char_count}")
print(f"sentence count is: {sentence_count}")

# calculates Arif using the formula
arif= 4.71 * (char_count/word_count) + 0.5 * (word_count/sentence_count) - 21.43
print(f"Arif value is: {arif}" )

# condition to check readability index based on reading level.
if (arif<1):
     print("kindergarden")
elif (arif<2):
    print("First grade")
elif (arif<3):
    print("second grade")
elif (arif<4):
    print("Third grade")
elif (arif<5):
    print("Fourth grade")
elif (arif<6):
    print("Fifth grade")
elif (arif<7):
    print("Sixth grade")
elif (arif<8):
    print("Seventh grade ")
elif (arif<9):
    print("Eigth grade")
elif (arif<10):
    print("Ninth grade")
elif (arif<11):
    print("Tenth grade")
elif (arif<12):
    print("Eleventh grade")
elif (arif<13):
    print("Tweleth grade")
else:
    print("college level")