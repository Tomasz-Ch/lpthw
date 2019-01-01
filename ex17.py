from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Kopiowanie z {from_file} do {to_file}.")

in_file = open(from_file)
indata = in_file.read()

print(f"Plik wejściowy ma {len(indata)} bajtów.")

print("Czy plik wyjściowy istnieje? {exists(to_file)}")
print("Wciśniej RETURN, aby kontynuować lub CRTL+C (^C), żeby anulować.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("W porządku. Zrobione.")

out_file.close()
in_file.close()
