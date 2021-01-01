Students = [
    {
        "Student id":"41",
        "Name":"Mohammad Zohaib",
        "Father Name":"Mohammad Shahid",
        "Address":"Surjani Town K.D.A Flat"
    },
    {
        "Student id":"28",
        "Name":"Mehwish Fatima",
        "Father Name":"Ali Khan",
        "Address":"Surjani Town K.D.A Flat"
    },
    {
        "Student id":"34",
        "Name":"Mohammad Qureshi",
        "Father Name":"Fateh ur Rehman",
        "Address":"Guru Mandar"
    }
]

print("list no 2 Name: is " + Students[2]["Name"])
print("Students list contain "+ str(len(Students)) + " Dictionaries.")

#append new
New_Student = {
    "Student id":"42",
    "Name":"Anwar Ali",
    "Father Name":"Ali",
    "Address":"Sarab Goth"
}
Students.append(New_Student)
print("Students list contain "+ str(len(Students)) + " Dictionaries.")

# add an List in dictionary of list
for each_dictionary in Students:
    each_dictionary["GPA"] = ["3.8","3.3","3.5"]
    # for item in each_dictionary.items():
    #     print(item[1])
print(Students[0])

#Check for a value
if "3.8" in Students[0]["GPA"]:
    Result = "Passed"
    print(Result)

print(Students)
    