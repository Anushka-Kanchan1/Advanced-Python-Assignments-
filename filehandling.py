file_name = "my_notes.txt"

with open(file_name, "w") as file:
    file.write("Hello everyone \n")
    file.write("I am Anushka .\n")

with open(file_name, "a") as file:
    file.write("This is python practice .\n")

print("--- Reading the File ---")
with open(file_name, "r") as file:
    content = file.read()
    print(content)


Output:
 --- Reading the File ---
 Hello everyone
 I am Anushka
 This is python practice .
