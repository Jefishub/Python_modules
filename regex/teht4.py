import re

str = 'The date is 22/10/2018'
str1 = 'The date is 3/1/2019'
lst = re.findall('[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}', str)
lst1 = re.findall('[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}', str1)
print(lst)
print(lst1)

pattern = r'[iI]t'
string = "It was the best of times, it was the worst of times."
matches = re.findall(pattern,string)
for match in matches:
    print(match)

    """
\w : sequence of word-like characters [a-zA-Z0–9_] that are not space
\d: Any numeric digit[0–9]
\s: whitespace characters(space,newline,tab)
\D: match characters that are NOT numeric digits
\W: match characters that are NOT words,digit or underscore
\S: match characters that are NOT spaces,tab or newline
    """

# Matches the email.
my_email = 'markus.korhonen@gmail.com'
my_name = 'Markus_Korhonen'
match1=re.findall(r'([\w0-9-._]+@[\w0-9-.]+[\w0-9]{2,3})',my_email)
match2=re.findall(r'([\w0-9-._]+@[\w0-9-.]+[\w0-9]{2,3})',my_name)
print(match1)
print(match2)