def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"Masz {cheese_count} kawałków sera!")
    print(f"Masz {boxes_of_crackers} paczek krakersów.")
    print("Stary, to wystarczy, aby zrobić imprezę!")
    print("Zorganizuj sobie koc.\n")



print("Możemy po prostu bezpośrednio podać funkcję i liczby:")
cheese_and_crackers(20, 30)


print("Albo możemy użyć zmienych ze skryptu:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("Możemy również wykonać wewnątrz operacje arytmetyczne:")
cheese_and_crackers(10 + 20, 5 + 6)


print("I możemy połączyć te dwie rzeczy, czyli zmienne i operacje arytmetyczne:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
