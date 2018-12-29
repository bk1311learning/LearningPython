from sys import argv

script, Name1, Name2, Name3, = argv


print("The script is called:", script)
print(f"{Name1} What is your favorite drink?", end=' ')
Name1FD = input()
print(f"{Name2} What is your favorite drink?", end=' ')
Name2FD = input()
print(f"{Name3} What is your favorite drink?", end=' ')
Name3FD = input()
print(f"So {Name1} enjoys drinking {Name1FD} the most.",
f" {Name2} likes {Name2FD}. {Name3} enjoys {Name3FD}")
