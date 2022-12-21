#8
print("Р В·Р В°Р Т‘Р В°Р Р…Р С‘Р Вµ 8")
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
a=[]
for i in string:
     if i.isalpha():
         a.append(i.lower())
print(set(a))

#9
print("Р В·Р В°Р Т‘Р В°Р Р…Р С‘Р Вµ 9")
string_numbers = [c for c in range(1, 11)]
print(list(map(lambda num: num**2, string_numbers)))

#10 
print("Р В·Р В°Р Т‘Р В°Р Р…Р С‘Р Вµ 10")

coords = [(1, 3), (2, 3), (5, 3),(0,-2)]
answer = []
for i in coords:
    x = i[0]
    y = i[1]
    if y == 5 * x - 2:
        answer.append((i, (y**2 + x**2)**0.5))
print(answer)

#11
print("Р В·Р В°Р Т‘Р В°Р Р…Р С‘Р Вµ 11")
numbers = [c for c in range(2, 28)]
even_lists = []
for i in numbers:
    if i % 2 == 0:
       even_lists.append(i)

print(list(map(lambda num: num**2, even_lists)))


#12
print("Р В·Р В°Р Т‘Р В°Р Р…Р С‘Р Вµ 12")
cor = [(1, 3), (2, 3), (5, 3), (0, -2)]
max_coords=max(cor)
print(max_coords)

#13
print("Р В·Р В°Р Т‘Р В°Р Р…Р С‘Р Вµ 13")
nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]
plus_numbers=[x+y for x, y in zip(nums_first, nums_second)]
minus_numbers=[x-y for x, y in zip(nums_first, nums_second)]
result_numbers=(list(zip(plus_numbers, minus_numbers)))
    
print(result_numbers)

#14
print("Р В·Р В°Р Т‘Р В°Р Р…Р С‘Р Вµ 14")




#15

print("Р В·Р В°Р Т‘Р В°Р Р…Р С‘Р Вµ 15")
input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""

out = []
mapped = {}
for i in input_str.split("\n"):
    line = i.split(",")
    mapped[line[0]] = line[1:]

for name, grade, subject, year in zip(mapped["name"], mapped["grade"], mapped["subject"], mapped["year"]):
    out.append({"name": name, "grade": grade, "subject": subject, "year": year})

print(out)

#16

print("Р В·Р В°Р Т‘Р В°Р Р…Р С‘Р Вµ 16")

a = [[11.9, 12.2, 12.9],
    [15.3, 15.1, 15.1], 
    [16.3, 16.5, 16.5],
    [17.7, 17.5, 18.1]]
result = [61.2, 61.3, 62.6]   


l = list(zip(*a))
res = []
for i in l:
    res.append(sum(i))
print(res)

#14
print("Р·Р°РґР°РЅРёРµ 14")
just_numbers= ['43141', '32441', '431', '4154', '43121']

slay_numbers=[]
for i in (list(map(lambda num: num**2, just_numbers))):
    if i % 2 == 0:
       slay_numbers.append(i)

print(slay_numbers)
        