
# CGPA calculator 
print("Let's Calculate Your CGPA")


def CGPA_calculator():
    number_of_courses = int(input("How many courses did you do? "))
    total_credit_point = 0

    grades = []
    credit_points = []
    
    total_unit_load = 0

    for intgr in range(number_of_courses):
        unit = int(input("Enter Course unit: "))

        score = int(input("Enter your score: "))

        total_unit_load += unit

        if score>=70 and score < 100:
            credit_rating = 5
            
        elif score>=60 and score<70 :
            credit_rating = 4
            
        elif score>=50 and score<60:
            credit_rating = 3
            
        elif score>=45 and score<50:
            credit_rating = 2
            
        elif score>=40 and score<45:
            credit_rating = 1
            
        else:
            credit_rating = 0
            
        total_credit_point += credit_rating*unit
    # print(grades.append(score))
    print(credit_points.append(credit_points))
    print(grades)
    print(credit_points)
    # print(credit_point)
    print(total_credit_point)
    CGPA = float(total_credit_point/total_unit_load)
    print(CGPA)
CGPA_calculator()
#my_scores = list(item) 
# print(my_scores) 
