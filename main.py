correction = True
print("Please enter your informations to learn if you can get your own driving licence situation ")


def name_info():
    global name
    name = input('Name : ')



def gentle_info():
    global correction
    global gentle
    gentle = input('Gentle (M/F) : ')

    while correction:
        if gentle == "M" or gentle == "F":
            if gentle == "M":
                gentle = "Male"
            elif gentle == "F":
                gentle = "Female"
            correction = False
        else:
            print("Please enter M or F")
            gentle_info()




def age_info():
    global correction
    global age
    birth = int(input('Birth Year : '))
    while correction:
        if 1900 <= birth <= 2022:
            correction = False
        else:
            print("Please enter a valid year !!")
            age_info()
    age = 2022 - birth



def schoolGrades_info():
    global schoolGrades
    schoolGrades = input("School Grades \nElementary --> 1 \nIntermediate --> 2 \nHigh School --> 3 \nCollage --> 4 \n")
    global correction

    while correction:
        if schoolGrades == 1 or schoolGrades == 2 or schoolGrades == 3 or schoolGrades == 4:
            if schoolGrades == 1:
                schoolGrades = 'Elementary'
            elif schoolGrades == 2:
                schoolGrades = 'Intermediate'
            elif schoolGrades == 3:
                schoolGrades = 'High School'
            else:
                schoolGrades = 'Collage'
            correction = False
        else:
            print("Please enter a valid option !!")
            schoolGrades_info()




def general_info():
    if gentle == "Male" and age >= 18 and (schoolGrades == 3 or schoolGrades == 4):
        print(f"Hello Mr.{name} you can get a driving licence because your age is {age} and your school grades is {schoolGrades}")

    elif gentle == "Female" and age >= 18 and (schoolGrades == 3 or schoolGrades == 4):
        print(f"Hello Ms.{name} you can get a driving licence because your age is {age} and your school grades is {schoolGrades}")
    # School
    elif gentle == "Male" and (age < 18 or (schoolGrades == 1 or schoolGrades == 2)):
        print(f"Hello Ms.{name} you cannot get a driving licence because your age is {age} and your school grades is {schoolGrades}")

    elif gentle == "Female" and (age < 18 or (schoolGrades == 1 or schoolGrades == 2)):
        print(f"Hello Ms.{name} you cannot get a driving licence because your age is {age} and your school grades is {schoolGrades}")


name_info()
gentle_info()
age_info()
schoolGrades_info()
general_info()
