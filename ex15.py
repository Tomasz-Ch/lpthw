from sys import argv

script, filename = argv

txt = open(filename)

print(f"Oto Twój plik {filename}:")
print(txt.read())

print("Wpisz ponownie nazwę pliku:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
