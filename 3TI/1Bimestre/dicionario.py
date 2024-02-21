User = {
    "Name" : "Mateus",
    "LastName" : "Paulino",
    "Age" : 17,
    "Course" : "TI",
    "Endress" : "Rua Lírios do campo"
}

print(User)

for i in User:
    print(User[i])

del User["Course"]

User["LastName"] = "Lopes"

print(User)

print(User["Endress"])