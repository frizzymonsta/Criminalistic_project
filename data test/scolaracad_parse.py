import re

with open('test.csv', encoding='windows-1251') as input:
    lines = input.readlines()

output = []

for line in lines:
    lastname = line.split('.')[0]

    year = re.search("[^\d\-](1|2)\d\d\d(?:[\. ])", line).group(0)
    year = year[1:5]

    output.append(str(year) + ", " + str(lastname) + "." + "\r")

with open('output.csv', 'w', encoding='windows-1251') as file:
    file.writelines(output)

