Student_1 = {
    "Name":"Mohammad Zohaib", 
    "Father Name":"Mohammad Shahid", 
    "Address":"Surjani Town K.D.A Flat"
    }

print(Student_1["Name"])

#adding or changing an element in dictionaries
Student_1["Roll no"] = "D-18-EE-41"

print(Student_1)

#Print each value
for each_value in Student_1.values():
    print(each_value)

#Print each keys
for each_key in Student_1.keys():
    print(each_key)

#Print each keys and values

for each_key, each_value in Student_1.items():
    print("Student "+ each_key + " is " + each_value) 