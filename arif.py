from sys import argv

script , filename = argv

txt = open(filename)
data = txt.read()

word_count = len(data.split())
char_count = len(data) 
sentence_count = data.count('.') + data.count('!') + data.count('?') 


print(f"Word count is: {word_count}")
print(f"Character count is: {char_count}")
print(f"sentence count is: {sentence_count}")

arif= 4.71 * (char_count/word_count) + 0.5 * (word_count/sentence_count) - 21.43
print(f"Arif value is: {arif}" )

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