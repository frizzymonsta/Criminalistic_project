import re

with open('test.csv', encoding='utf-8') as input:
    lines = input.readlines()

output = []

n = 0
couple = ""

for line in lines:
    n = n + 1
    couple = couple + line

    if n >= 4:
        n = 0

        lastname = couple.split(',')[0]
        if lastname [0] == '"':
            lastname = lastname[1:]
        search = re.search("[\.](1|2)\d\d\d([\.])", couple)

        year = search.group(0)
        year = year[1:5]

        output.append(str(year) + ", " + str(lastname)+"\r")
        print(couple)
        couple = ""

        with open('output.csv', 'w', encoding='utf-8') as file:
            file.writelines(output)
