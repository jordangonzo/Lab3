def average_grade(roster)
    total=0
    grade_num=0
    for item in roster:
        total+=get_grade()
        grade_num+=1
    return total/grade_num
