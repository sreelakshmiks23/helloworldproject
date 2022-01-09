def create_file():
    f = open("sample.txt", "w")
    a = input("Enter your string:")
    f.write(a)
    print("File created!")
    f.close()

def find_function(search_element):
    f = open("sample.txt", "r")
    a = f.read()
    b = a.split()
    if search_element in b:
        print("Element found!")
        print(search_element)
    else:
        print("Element not found")       
    f.close()

def replace_function(source_element, replace_element):
    f = open("sample.txt", "r+")
    ch = f.read()
    if source_element in ch:
        f.close()
        f1 = open("sample.txt", "r+")
        ch1 = f1.read()
        ch1 = ch1.replace(source_element, replace_element)
        f1.seek(0)
        f1.write(ch1)
        f1.close()
        print("Word replaced!\n")
        f2 = open("sample.txt")
        a = f2.read()
        print("New string:",a)
    else:
        print("Element not found, so string not modified")
        f.close()

print("Program to find and replace words in a user-created text file:")
while True:
    print("\n1.Create file")
    print("2.Find a given word")
    print("3.Replace a given word")
    print("4.Exit\n")
    c = int(input("Enter your choice:"))
    
    if c == 1:
        create_file()
    elif c == 2:
        search_element = input("Enter word to be searched:")
        find_function(search_element)
    elif c == 3:
        source_element = input("Enter word to be replaced:")
        replace_element = input("Enter new word:")
        replace_function(source_element, replace_element)
    elif c == 4:
        print("Program is exiting...")
        break

    
         
    
