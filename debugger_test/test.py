message = "Hello"
def get_frequency(text, word):
    words = text.split(" ")
    count = text.count(word)
    frequency = count / len(words) * 100 # Calculate frequency percentage
    return frequency


frequency = get_frequency("Ahoj jak se máš?", "máš")
if frequency > 5:
    print("High frequency")
else:
    print("Low frequency")



print(message) # Print the message