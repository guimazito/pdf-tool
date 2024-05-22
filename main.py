import sys
from common import merge_files, split_files

menu = "\n1. Merge Files (PS: Rename Your Files To Be In The Desired Insertion Order)\
        \n2. Split File (PS: You Must Have Only One File In The Folder split)\
        \n0. Exit\
        \nOption: "

while True:
    
    option = input(menu)

    match option:

        case "1":
            filepath = merge_files()
            print(f"\n{filepath} created!")

        case "2":
            start_page = int(input("\nStart Page: "))
            end_page = int(input("End Page: "))
            filepath = split_files(start_page, end_page)
            print(f"\n{filepath} created!")

        case "0":
            print("\nBye Bye...\n")
            sys.exit(0)

        case _:
            print("\nInvalid Option!\n")
