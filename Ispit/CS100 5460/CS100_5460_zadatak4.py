def check_string(value):
    if value.isalpha():
        return value
    raise Exception('Vrednost moze sadrzati samo slova!')

def check_number(value):
    if value.isnumeric():
        return value
    raise Exception('Vrednost moze sadrzati samo brojeve!')

# def check_negative(value):
#     if int(value) > 0:
#         return value
#     return Exception('Vrednost ne moze biti negativna!')

def enter_student_data():
    student_name = check_string(input('Unesite ime studenta -> '))
    student_surname = check_string(input('Unesite prezime studenta -> '))
    birth_year = check_number(input('Unesite godinu rodjenja -> '))
    index_number = check_number(input('Unesite broj indeksa -> '))

    return [student_name, student_surname, birth_year, index_number]

def enter_student_courses():
    number_of_subjects = int(check_number(input('Broj predmeta -> ')))
    my_courses = {}

    for x in range(1, number_of_subjects + 1):
        my_courses[input('Unesite sifru predmeta -> ')] = input('Unesite naziv predmeta -> ')
    
    return my_courses

try:
    my_student = enter_student_data()
    my_courses = enter_student_courses()

    print(f'{my_student[0]} {my_student[1]}, {my_student[3]}, rodjen/a {my_student[2]}. godine, slusa sledece predmete:')

    for sifra, naziv in my_courses.items():
        print(f'{sifra}: {naziv}')

except Exception as msg:
    print(msg)
