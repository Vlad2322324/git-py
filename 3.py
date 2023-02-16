print("1 задание")
Name = "Vlad"
Surname = "Romantsov"
print(f"Hello {Name} {Surname}! You just delved into Python. Great start!")



print("\n\n2 задание")
thickness = 6
c = 'H'

for i in 1,3,5,7,9,11:
    print((c*i).center(thickness+6))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2-3) + (c*thickness).center(thickness*6-1))

for i in range(thickness-4):
    print((c*thickness*5).center(thickness*5+1))

for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2 - 3) + (c * thickness).center(thickness * 6 - 1))

for i in 11,9,7,5,3,1:
    print(((c*i).center(thickness+6)).rjust(thickness*6-3))

print("\n\n3 задание")
text = "hello world"
print(text.title())


print("\n\n4 задание")
amount = 100500.157
print('{:,.2f}'.format(amount))


print("\n\n5 задание")
height = 10
wight = height * 3
t = '0'
k = 'T'
for i in range(height//2):
    #    print((t*i).rjust(wight//2) + (t*i).ljust(wight//2))
    print((((wight//2)-i)*k)+(i*t) + (i*t)+(((wight//2)-i)*k))
for i in range(height//2,-1,-1):
    print((((wight // 2) - i) * k) + (i * t) + (i * t) + (((wight // 2) - i) * k))



print("\n\n6 задание")
value = 234230
mul=1
print(f"Число:{value}")
while value>0:
    if (value%10)!=0:
        mul*=value%10
    value//=10
print(f"Результат умножения:{mul}")


