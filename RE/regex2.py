import re 

pattern = r"(?P<dog>ab)cd(ef)"

regex = re.compile(pattern)
obj = regex.search("abcdefghi",0,7)

# print(obj.group())
#属性
print(obj.pos)  #目标子串开始位置
print(obj.endpos) #目标子串结束位置
print(obj.re)  #正则表达式
print(obj.string)  #目标字符串
print(obj.lastgroup) #最后一组组名
print(obj.lastindex) #最后一组序列号
print("===================================")

print(obj.start())  #匹配内容的开始位置
print(obj.end())   #匹配内容的结束位置
print(obj.span())  #匹配内容的起止位置

print(obj.group())
print(obj.group(2))
print(obj.group('dog'))

print(obj.groupdict())
print(obj.groups())