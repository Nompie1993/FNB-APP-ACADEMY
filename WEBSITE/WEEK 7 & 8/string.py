#STRINGS

message = "Hello, World!"
message1 ="Bob's World! "
print(message1)
print(message)

print(message[0])  # First character
print(message[-1])  # Last character    

print(len(message))  # Length of the string
message2 = " Hello, World! " # String with leading and trailing spaces
print(message2.strip())
print(message2.lower())  # Convert to lowercase
print(message2.upper())  # Convert to uppercase
print(message2.split(','))  # Split into a list of words
print(message2.replace("World", "Universe"))  # Replace substring