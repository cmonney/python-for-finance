# Ask for a sentence
# Print the length of the sentence
# Ask for a file name (.txt)
# Write the sentence to the file
# Run the program from your command line

sentence = input("Please enter a sentence: ")

print("\nYou entered a sentence of length ", len(sentence))

filename = input("Please enter a filename: ")
# filename = '{0}.txt'.format(filename)
filename = f"{filename}.txt"
with open(filename, "w") as f:
    f.write(sentence)
    f.close()
