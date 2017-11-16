def main():
    userinput = input("Enter a sentence: ")
    return userinput
print(main())
#Count the number of spaces
def count_spaces():
    userinput = input("Enter a sentence: ")
    spaces=0
    for char in userinput:
        if char=="":
            spaces=spaces+1
            return(spaces)
print(count_spaces())
