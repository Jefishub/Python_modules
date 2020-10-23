import re

text_list = ["abs", "alias", "abyss", "Alias", "An abacus"]

for word in text_list:
    print(re.findall("a...s$", word))
    

second_list = ["a", "ac", "Hey Jude", "abc de ca"]

for word in second_list:
    print(re.findall("[abc]", word))

txt ="The rain in Spain 45599"

x = re.findall("[0-9]",txt)
print(x)