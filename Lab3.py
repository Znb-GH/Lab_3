# Lab 3 - 

# Q1: Numbers divisible by 7 and 5 between 1500 and 2700
print("Q1: Numbers divisible by 7 and 5 (1500-2700)")
ans1 = []
for x in range(1500, 2701):
    if x % 7 == 0 and x % 5 == 0:
        ans1.append(x)
print(ans1)
print()

# Q2: Temperature Conversion
print("Q2: Temperature Conversion")
temp_c = 60
temp_f = (temp_c * 9/5) + 32
print(f"{temp_c}C is {temp_f}F")

temp_f2 = 45
temp_c2 = (temp_f2 - 32) * 5/9
print(f"{temp_f2}F is {temp_c2}C")
print()

# Q3: Guess a number between 1 and 9
print("Q3: Guess the Number Game")
import random
target = random.randint(1, 9)
while True:
    g = int(input("Guess a number (1-9): "))
    if g == target:
        print("Well guessed!")
        break
    else:
        print("Try again.")
print()

# Q4: Star pyramid pattern
print("Q4: Star Pattern")
rows = 5
for r in range(1, rows + 1):
    print("* " * r)
for r in range(rows - 1, 0, -1):
    print("* " * r)
print()

# Q5: Reverse a word
print("Q5: Reverse a Word")
inp_word = input("Enter a word: ")
rev_word = inp_word[::-1]
print("Reversed:", rev_word)
print()

# Q6: Count even and odd numbers
print("Q6: Count Even and Odd")
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
c_even = 0
c_odd = 0
for v in nums:
    if v % 2 == 0:
        c_even += 1
    else:
        c_odd += 1
print("Even:", c_even)
print("Odd:", c_odd)
print()

# Q7: Print items and their types
print("Q7: Items and Types")
my_list = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": "V", "section": "A"}]
for obj in my_list:
    print(obj, "->", type(obj))
print()

# Q8: Print 0 to 6 except 3 and 6
print("Q8: Numbers Except 3 and 6")
for k in range(0, 7):
    if k == 3 or k == 6:
        continue
    print(k, end=" ")
print("\n")

# Q9: Fibonacci series 0 to 50
print("Q9: Fibonacci (0-50)")
f1, f2 = 0, 1
while f1 <= 50:
    print(f1, end=" ")
    f1, f2 = f2, f1 + f2
print("\n")

# Q9b: FizzBuzz 1 to 50
print("Q9b: FizzBuzz")
for p in range(1, 51):
    if p % 3 == 0 and p % 5 == 0:
        print("FizzBuzz")
    elif p % 3 == 0:
        print("Fizz")
    elif p % 5 == 0:
        print("Buzz")
    else:
        print(p)
print()

# Q10: 2D array where value = i*j
print("Q10: 2D Array i*j")
r1 = 3
c1 = 4
mat = []
for i in range(r1):
    temp_row = []
    for j in range(c1):
        temp_row.append(i*j)
    mat.append(temp_row)
print(mat)
print()

# Q11: Lines to lower case
print("Q11: Lower Case Lines")
all_lines = []
while True:
    txt = input("Enter a line (blank to stop): ")
    if txt == "":
        break
    all_lines.append(txt.lower())
for txt in all_lines:
    print(txt)
print()

# Q12: Binary numbers divisible by 5
print("Q12: Binary Divisible by 5")
data = "0100,0011,1010,1001,1100,1001"
bin_list = data.split(",")
out_list = []
for b in bin_list:
    dec = int(b, 2)
    if dec % 5 == 0:
        out_list.append(b)
print(",".join(out_list))
print()

# Q13: Count digits and letters
print("Q13: Count Digits and Letters")
msg = "Python 3.2"
count_alpha = 0
count_num = 0
for ch in msg:
    if ch.isalpha():
        count_alpha += 1
    elif ch.isdigit():
        count_num += 1
print("Letters", count_alpha)
print("Digits", count_num)
print()

# Q14: Password Validation
print("Q14: Password Validation")
import re

def check_pass(pwd):
    if not (6 <= len(pwd) <= 16):
        return False
    if not re.search("[a-z]", pwd):
        return False
    if not re.search("[A-Z]", pwd):
        return False
    if not re.search("[0-9]", pwd):
        return False
    if not re.search("[$#@]", pwd):
        return False
    return True

pwd_test = "Pass@123"
if check_pass(pwd_test):
    print(pwd_test, "is valid")
else:
    print(pwd_test, "is NOT valid")# Lab 3 - Python Programs (Updated Version)

# Q1: Numbers divisible by 7 and 5 between 1500 and 2700
print("Q1: Numbers divisible by 7 and 5 (1500-2700)")
ans1 = []
for x in range(1500, 2701):
    if x % 7 == 0 and x % 5 == 0:
        ans1.append(x)
print(ans1)
print()

# Q2: Temperature Conversion
print("Q2: Temperature Conversion")
temp_c = 60
temp_f = (temp_c * 9/5) + 32
print(f"{temp_c}C is {temp_f}F")

temp_f2 = 45
temp_c2 = (temp_f2 - 32) * 5/9
print(f"{temp_f2}F is {temp_c2}C")
print()

# Q3: Guess a number between 1 and 9
print("Q3: Guess the Number Game")
import random
target = random.randint(1, 9)
while True:
    g = int(input("Guess a number (1-9): "))
    if g == target:
        print("Well guessed!")
        break
    else:
        print("Try again.")
print()

# Q4: Star pyramid pattern
print("Q4: Star Pattern")
rows = 5
for r in range(1, rows + 1):
    print("* " * r)
for r in range(rows - 1, 0, -1):
    print("* " * r)
print()

# Q5: Reverse a word
print("Q5: Reverse a Word")
inp_word = input("Enter a word: ")
rev_word = inp_word[::-1]
print("Reversed:", rev_word)
print()

# Q6: Count even and odd numbers
print("Q6: Count Even and Odd")
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
c_even = 0
c_odd = 0
for v in nums:
    if v % 2 == 0:
        c_even += 1
    else:
        c_odd += 1
print("Even:", c_even)
print("Odd:", c_odd)
print()

# Q7: Print items and their types
print("Q7: Items and Types")
my_list = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": "V", "section": "A"}]
for obj in my_list:
    print(obj, "->", type(obj))
print()

# Q8: Print 0 to 6 except 3 and 6
print("Q8: Numbers Except 3 and 6")
for k in range(0, 7):
    if k == 3 or k == 6:
        continue
    print(k, end=" ")
print("\n")

# Q9: Fibonacci series 0 to 50
print("Q9: Fibonacci (0-50)")
f1, f2 = 0, 1
while f1 <= 50:
    print(f1, end=" ")
    f1, f2 = f2, f1 + f2
print("\n")

# Q9b: FizzBuzz 1 to 50
print("Q9b: FizzBuzz")
for p in range(1, 51):
    if p % 3 == 0 and p % 5 == 0:
        print("FizzBuzz")
    elif p % 3 == 0:
        print("Fizz")
    elif p % 5 == 0:
        print("Buzz")
    else:
        print(p)
print()

# Q10: 2D array where value = i*j
print("Q10: 2D Array i*j")
r1 = 3
c1 = 4
mat = []
for i in range(r1):
    temp_row = []
    for j in range(c1):
        temp_row.append(i*j)
    mat.append(temp_row)
print(mat)
print()

# Q11: Lines to lower case
print("Q11: Lower Case Lines")
all_lines = []
while True:
    txt = input("Enter a line (blank to stop): ")
    if txt == "":
        break
    all_lines.append(txt.lower())
for txt in all_lines:
    print(txt)
print()

# Q12: Binary numbers divisible by 5
print("Q12: Binary Divisible by 5")
data = "0100,0011,1010,1001,1100,1001"
bin_list = data.split(",")
out_list = []
for b in bin_list:
    dec = int(b, 2)
    if dec % 5 == 0:
        out_list.append(b)
print(",".join(out_list))
print()

# Q13: Count digits and letters
print("Q13: Count Digits and Letters")
msg = "Python 3.2"
count_alpha = 0
count_num = 0
for ch in msg:
    if ch.isalpha():
        count_alpha += 1
    elif ch.isdigit():
        count_num += 1
print("Letters", count_alpha)
print("Digits", count_num)
print()

# Q14: Password Validation
print("Q14: Password Validation")
import re

def check_pass(pwd):
    if not (6 <= len(pwd) <= 16):
        return False
    if not re.search("[a-z]", pwd):
        return False
    if not re.search("[A-Z]", pwd):
        return False
    if not re.search("[0-9]", pwd):
        return False
    if not re.search("[$#@]", pwd):
        return False
    return True

pwd_test = "Pass@123"
if check_pass(pwd_test):
    print(pwd_test, "is valid")
else:
    print(pwd_test, "is NOT valid")
