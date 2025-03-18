def handle_file_error():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("file content:")
            print(content)

    except FileNotFoundError:
        print("Error: File not found. please check the filename and try again")
    except IOError:
        print("Error: unable to read the file.")