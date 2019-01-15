import re 

s = "Hi,This is Jame"

it = re.finditer(r'[A-Z]\w+',s)

for i in it:
    print(i.group()) #获取match对象对应子串

try:
    obj = re.fullmatch(r"\w+","port123")
    print(obj.group())
except AttributeError as e:
    print(e)

obj = re.match(r'Hello',"Hello,joy")
print(obj.group())


obj = re.search(r'\d+',"138-4466-5587")
print(obj.group())