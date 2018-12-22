def set_grade(shots, errors_num):
    errors_prop = errors_num / shots 
    if errors_prop < 0.1:
        grade = '5 -'
    elif errors_prop < 0.3:
        grade = '4'
    elif errors_prop <= 0.5:
        grade = '3'
    else:
        grade = '2'
    return grade
