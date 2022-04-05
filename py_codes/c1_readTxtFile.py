# Read the provided text files

fileName = input("""
Enter a File Name:
[ clown.txt ] [ intro-short.txt ]
[ mbox-short.txt ] [ romeo.txt ] [ words.txt ]
""")

fh = open(fileName, "r")
count = 0

print("\nYour Text:\n")
for line in fh:
	print(line.strip())
	count += 1
print("\nTotal lines: {}".format(count))