formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("jeden", "dwa", "trzy", "cztery"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Spróbuj tutaj",
    "Wpisać własny tekst",
    "Może wiersz",
    "Albo piosenkę o lęku"
))
