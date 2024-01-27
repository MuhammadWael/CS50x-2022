x = input("Text:")
s = 0
l = 0
w = 1
for i in x:
    if i == '.' or i == '?' or i == '!':
        s += 1
    if i == ' ':
        w += 1
    else:
        l += 1

grade = int(0.0588*(l/w*100)-0.296*(s/w*100)-15.8)
if grade < 1:
    print("Before Grade 1")
elif grade > 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")