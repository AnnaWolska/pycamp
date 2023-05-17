from string import ascii_lowercase
import json
from json import load, dump

letters = ascii_lowercase
# print(letters)

with open('pytania.json') as file:
    data = json.load(file)

# print(data)
# with open('pytania.json',r) as file:
name = input("O, widzę nowgo gracza, jak masz na imię?:")
print(f"{name}, odpowiedz na 4 pytania:")
points = 0
for el in data:
    # print(el['question'])

    class Question:
        question = (el['question'])
        answers = (el['answers'])
        right_answer = (el['right_answer'])


    print(Question().question)
    for letter, answer in zip(list(letters),list(Question().answers)):
        print(letter,answer)
    # print(list(zip(letters,Question().answers)))
    answer_given = input("Twoja odpowiedź to? : ")
    # print(answer_given)
    if answer_given == Question().right_answer:
        points += 1
        print(f"Brawo, zgadłeś!{name} zdobywasz {points} punktów.")
    else:
        print("Niestety, próbuj dalej.")
print(f"{name} masz {points} poprawnych odpowiedzi.")

resoults = []
# with open('results.json', 'r') as file:
#     results = load(file)
#
# with open('results.json', 'w') as file:
#     results.append({
#         'name':name,
#         'points': points
#     })

with open('results.json') as file:
    results = load(file)
    results.append({
        'name':name,
        'points': points
    })

with open('results.json', "w") as file:
    dump(resoults, file)
# try:
#     with open('results.json', 'w') as file:
#         results = load(file)
#         results.append({
#             'name':name,
#             'points': points
#         })
# except FileNotFoundError:
#     results=[]
#
# with open('results.json', 'w') as file:
#     dump(results, file)
