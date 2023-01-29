def print_numbers_to_file(n):
    with open('zadatak2.txt', 'w') as fw:
        for broj in range(n + 1):
            fw.write(str(broj) + '\n')

try:
    print_numbers_to_file(11)

    with open('zadatak2.txt', 'r') as fr:
        brojevi = fr.readlines()
        zbir = 0
        for broj in brojevi:
            zbir += int(broj)
        
        print(f'Zbir svih brojeva je {zbir}')
            
except FileNotFoundError as file_err:
    print('Datoteka nije pronadjena!')
except Exception as err2:
    print(err2)