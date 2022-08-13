correction = True
print("Please enter your informations to learn if you can get your own driving licence situation ")

while correction:
    def query():
        def name_info():
            global name
            name = input('Name : ')

        def gender_info():
            global correction
            global gender
            gender = input('Gender (M/F) : ')

            while correction:
                if gender == "M" or gender == "F":
                    if gender == "M":
                        gender = "Male"
                    elif gender == "F":
                        gender = "Female"
                    correction = False
                else:
                    print("Please enter M or F")
                    gender_info()

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

        def school_grades_info():
            global schoolGrades
            schoolGrades = input(
                "School Grades \nElementary --> 1 \nIntermediate --> 2 \nHigh School --> 3 \nCollage --> 4 \n")
            global correction

            while correction:
                if schoolGrades == "1" or schoolGrades == "2" or schoolGrades == "3" or schoolGrades == "4":
                    correction = False
                else:
                    print("Please enter a valid option !!")
                    school_grades_info()
            if schoolGrades == "1":
                schoolGrades = "Elementary"
            elif schoolGrades == "2":
                schoolGrades = "Intermediate"
            elif schoolGrades == "3":
                schoolGrades = "High School"
            elif schoolGrades == "4":
                schoolGrades = "Collage"

        def message_can():
            print(
                f"Hello Mr.{name} you can get a driving licence because your age is {age} and your school grades is {schoolGrades}")

        def message_cannot():
            print(
                f"Hello Ms.{name} you cannot get a driving licence because your age is {age} and your school grades is {schoolGrades}")

        def general_info():
            if gender == "Male":
                if (age > 18 and schoolGrades == "High School") or (age >= 18 and schoolGrades == "Collage"):
                    message_can()
                elif (age < 18 or schoolGrades == "Elementary") or (age < 18 or schoolGrades == "Intermediate"):
                    message_cannot()

            elif gender == "Female":
                if (age > 18 and schoolGrades == "High School") or (age >= 18 and schoolGrades == "Collage"):
                    message_can()
                elif (age < 18 or schoolGrades == "Elementary") or (age < 18 or schoolGrades == "Intermediate"):
                    message_cannot()

        name_info()
        gender_info()
        age_info()
        school_grades_info()
        general_info()


    query()



    print("Do you want more query ?")
    answer = input("Answer (Y/N)")
    if answer == "N":
        correction = False
    elif answer == "Y":
        query()

