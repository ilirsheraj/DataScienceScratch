if 1 > 2:
	message = "if only one were greater than 2"
elif 1 > 3:
	message = "elif stands for else if"
else:
	message = "when all else fails, use else (if you want to)"

print(message)

# All in one line
x = 5
parity = "even" if x % 2 == 0 else "odd"
print(parity)
print("=" * 10)
# While loop
x = 0
while x < 10:
	print(f"{x} is less than 10")
	x += 1
print("=" * 10)
# Break and continue
for x in range(10):
	if x == 3:
		continue
	if x == 5:
		break
	print(x)
