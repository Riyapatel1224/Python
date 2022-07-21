from unicodedata import name


people=[
    {"name":"Harry", "house":"Gryffinder"},
    {"name":"Cho", "house":"Gryffinder"},
    {"name":"Draco", "house":"Gryffinder"}
]

people.sort(key=lambda person:person["name"])
print(people)