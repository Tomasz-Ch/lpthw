from sys import argv

script, filename = argv

print(f"Wymażemy {filename}.")
print("Jesli tego nie chcesz, wcisniej CTRL+C (^C).")
print("Jesli tego chcesz, wciśniej RETURN.")

input("?")

print("Otwieranie pliku...")
target = open(filename, 'w')

print("Wykasowywanie pliku. Do widzenia!")
target.truncate()

print("Teraz proszę Cię o wpisanie trzech linii tekstu.")

line1 = input("linia 1: ")
line2 = input("linia 2: ")
line3 = input("linia 3: ")

print("Zapisze je w pliku.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("A na koniec zamykamy plik.")
target.close()
