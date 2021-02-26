import py_compile
while True:
    try:
        file = input("path to the file to compile: ")
        py_compile.compile(f"{file}")
        print(f"File has been compiled to {file}")
    except Exception as e:
        print("Check the path , if it is correct because it occured a problem ")

        
