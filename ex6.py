types_of_people = 10
x = f"Istnieje {types_of_people} rodzajów ludzi."

binary = "binarny"
do_not = "nie znają"
y = f"Ci, którzy znają system {binary} i ci, którzy go {do_not}."

print(x)
print(y)

print(f"Powiedziałem: {x}")
print(f'Powiedziałem również "{y}"') #można stosować zamiennie cudzysłów i apostrof

hilarious = True
joke_evaluation = "Czyż to nie jest przezabawny dopwcip?! {}"

print(joke_evaluation.format(hilarious))

w = "To jest lewa strona..."
e = "łańcucha znaków z prawą stroną."

print(w+e)
