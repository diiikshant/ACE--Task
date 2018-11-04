dataBase = {}
i = 'y'
mathMax = 0
sciMax = 0
hisMax = 0
engMax = 0
while i == "y":
    Name = input("Enter name of the student: ")
    Math = float(input("Enter marks obtained in Mathematics: "))
    Science = float(input("Enter marks obtained in Science: "))
    English = float(input("Enter marks obtained in English: "))
    History = float(input("Enter marks obtained in History: "))
    dataBase[Name] = {'Math': Math, 'Science': Science, 'English': English, 'History': History, "Percentage":
        (Math + Science + English + History) / 4}
    print("Percentage obtained: " + str(dataBase[Name]["Percentage"]) + "%")
    i = input("Create another entry? (y/n)")
for Name in dataBase:
    if (dataBase[Name]["Math"] > mathMax):
        mathMax = dataBase[Name]['Math']
        topperMath = Name
    if (dataBase[Name]["Science"] > sciMax):
        sciMax = dataBase[Name]['Science']
        topperScience = Name
    if (dataBase[Name]["History"] > hisMax):
        hisMax = dataBase[Name]['History']
        topperHistory = Name
    if (dataBase[Name]["English"] > engMax):
        engMax = dataBase[Name]['English']
        topperEnglish = Name
print("Top scorer in Mathematics: " + str(topperMath))
print("Top scorer in Science: : " + str(topperScience))
print("Top scorer in History: " + str(topperHistory))
print("Top scorer in English: " + str(topperEnglish))