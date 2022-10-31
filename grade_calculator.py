def welcome():
    print("********************")
    print("Welcome to Jack's grade calculator!\n")

def getMode():
    selection = None
    valid_selections = ["grade", "examgrade"]
    print("Do you want to calculate your grade or find out how much you need for the exam?")
    while selection not in valid_selections:
        selection = str(input("Enter \"grade\" or \"exam\" to select which mode you want: "))
    return selection

def grade():
    num_assignments = int(input("Enter how many assignments you have completed: "))
    percent_grade = []
    for i in range(num_assignments):
        print(f"\nAssignment {i + 1}")
        print("**********")
        # marks_out_of = None
        # marks_attained = None
        # weight = None
        marks_out_of = float(input("\nWhat is the maximum marks of the assignment? "))
        marks_attained = float(input("\nHow many marks did you get? "))
        weight = float(input("\nWhat percent of your final grade is this assignment worth? "))
        grade_attained = (marks_attained / marks_out_of) * weight
        percent_grade.append(grade_attained)
    current_grade = sum(percent_grade)
    print(f"\nYour current grade is {current_grade}%!")



def exam():
    current_grade = float(input("\nWhat is your current grade percentage? "))/100
    exam_weight = float(input("\nWhat percentage is the final exam worth? "))/100
    desired_pass = float(input("\nWhat percentage do you need to pass? "))/100

    needed_on_exam = round((desired_pass - ((1 - exam_weight) * current_grade)) / exam_weight, 2) * 100

    print(f"You need {needed_on_exam}% on your exam to get your desired grade!")




if __name__ == "__main__":
    welcome()
    player_mode = getMode()
    if player_mode == "grade":
        grade()
    else:
        exam()

