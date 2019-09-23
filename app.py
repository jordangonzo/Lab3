#create roster
from mymodules.models import Student
from mymodules.math_utils import average_grade

def __main__():
    roster=[Student("Kaleb", 95),
            Student("Annie", 75),
            Student("Julius", 84),
            Student("Lenny", 95),
            Student("Nick", 95),
            Student("Sonny", 95),
            Student("Mike", 95),
            Student("David", 95),
            Student("Yvanna", 95),
            Student("Beatrice", 95)]

    for i in roster:
        i.print_stud_info()

    print(average_grade(roster))

__main__()
