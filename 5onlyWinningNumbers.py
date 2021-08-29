import re


f = open("allText.txt", "r");
Lines = f.readlines();
f.close();
regex = "([\d]+(-)[\d]+(-)[\d]+(-)[\d]+(-)[\d]+(-)[\d]+(\s)(/)(\s)[\d]+)";

only_numbers = [];

for line in Lines:
    r = re.search(regex, line)
    if r!=None:
        print(r);
        only_numbers.append(r[1]);

print(len(only_numbers));

f = open("only_numbers.txt", "w");
for l in only_numbers:
    f.write(l);
    f.write("\n");
    print("+");
f.close();
