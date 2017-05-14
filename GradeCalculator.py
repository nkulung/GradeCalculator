def enterGrades():
    grades = []
    weight = []
    while True:
        try:
            d = int(input('How many grades:'))
            if 0 < d < 15:
                break
            else:
                continue
        except ValueError:
            print('Please enter a valid integer')
    for i in range(d):
        print('Enter Grade ',(i+1))
        g = float(input('Grade:'))
        print("Enter Grade",(i+1),"'s weight (ei. '.10' for 10%)")
        p = float(input('Weight:'))
        grades.append(g)
        weight.append(p)
    return grades, weight

            
    

def calculateGrade(grades, weight):
    total = 0
    for i in range(len(grades)):
        total += grades[i]*weight[i]
    return total


def changeGrade(grades,weight):
    print('Enter grade # you want to change')
    while True:
        try:
            g = int(input('>>>'))
            if 0 < g <= len(grades):
                print('Enter the new grade')
                h = float(input('>>'))
                grades[g-1] = h
                break
            else:
                continue
        except ValueError:
            print('Enter a number between 1 -',len(grades),'please')
    return grades


def changeGradeChoice(grades, weight):
    print('Press 1 to change a grade, 0 to continue')
    while True:
        try:
            choice = int(input('>>>'))
            if choice == 0:
                total = calculateGrade(grades,weight)
                print(total)
                break
            elif choice == 1:
                grades = changeGrade(grades,weight)
                total = calculateGrade(grades,weight)
                break
        except ValueError:
            print('Please enter either 1 or 0')
    return grades, total

def main():
    print('------------------------------')
    print('-------Grade Calculater-------')
    print('------By Nick Kulungian-------')
    print('------------------------------')
    grades, weight = enterGrades()
    grades, total = changeGradeChoice(grades,weight)
    print(grades)
    print("Final grade: ",total)
    input('Press ENTER to EXIT')

main()
          

