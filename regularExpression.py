import re

text = "this is Ravi with $40 in my hand"

setCh = re.findall('[d-i]', text)
spclCh = re.findall('\d', text)
anyCh = re.findall('th..', text)
startWith = re.findall('^is', text)
endsWith = re.findall('hand$', text)
zeroOrMore = re.findall('vi*', text)

print(setCh)
print(spclCh)
print(anyCh)
print(startWith)
print(endsWith)
print(zeroOrMore)

count = 0
whiteSpace = re.findall('\s', text)
print(whiteSpace)
