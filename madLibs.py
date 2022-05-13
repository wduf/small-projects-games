
print("noun? (a name)")
noun1 = input()
print("adjective?")
adjective1 = input()
print("noun? (town/city name)")
noun2 = input()
print("noun? (another name)")
noun3 = input()
print("noun? (a sport)")
noun4 = input()

print()

# story:

print(f"Once upon a time, there was a young boy named {noun1}.")
if adjective1[0] == "a" or adjective1[0] == "e" or adjective1[0] == "i" or adjective1[0] == "o" or adjective1[0] == "u":
    print(f"He lived in an {adjective1} town named {noun2}")
else:
    print(f"He lived in a {adjective1} town named {noun2}")
print(f"His best friend, {noun3}, lived across the street from him and her favorite sport was {noun4}.")