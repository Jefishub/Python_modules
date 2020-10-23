import re

word_list = ["hello", "hei","heippa", "hey", "hi"]

for i in range(len(word_list)):
    if re.findall("^he", word_list[i]):
        print("The matched word is " + word_list[i])
    else:
        print("This word did not match " + word_list[i])