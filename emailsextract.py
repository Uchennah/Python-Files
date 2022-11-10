import re

file = open('emails.txt', 'r')
file_text = file.read()

match = re.search(r'[\w.-]+@[\w\.-]+', file_text)

print(match)
