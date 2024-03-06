import pyfiglet
name=input("Enter your name: ")
print("====================")
print("Banner2-D")
print("Doom")
print("Digital")
print("Diamond")
print("Epic")

font_style = input("Choose the font style from above: ")
font=pyfiglet.figlet_format(f"{name}",f"{font_style}")
print(font)