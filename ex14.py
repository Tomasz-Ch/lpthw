from sys import argv

script, user_name = argv
prompt = '> '

print(f"Cześć {user_name}, jestem skryptem {script}.")
print("Chciałbym Ci zadać kilka pytań.")
print(f"Lubisz mnie, {user_name}?")
likes = input(prompt)

print(f"Gdzie mieszkasz?, {user_name}?")
lives = input(prompt)

print("Jaki masz komputer?")
computer = input(prompt)

print(f"""
OK, gdy zapytałem, czy mnie lubisz, odpowiedziałeś {likes}. Mieszkasz w {lives}. Nie jestem pewien, gdzie to jest.
I masz koputer {computer}. Fajnie.
""")
