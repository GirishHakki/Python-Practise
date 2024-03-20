import os

choice = input("Shutdown your computer? ( y or n ) : ")
if choice == "y" or choice == "y":
    os.system("shutdown /l")
else:
    print("Exiting the program")