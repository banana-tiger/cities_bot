import csv

def main():
    with open('city.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        cities_list = [row['address'].split('г ')[-1].lower() for row in reader]

    
    used_list = []
    trash_letters_list = ['ь', 'ъ', 'ы']
    last_letter = ''


    while True:
        input_text = input().lower()

        if not used_list:
            if input_text not in cities_list:
                print('Введенного города нет в списке')
            else:
                used_list.append(input_text)
                if input_text[-1] in trash_letters_list:
                    for letter in input_text[::-1]:
                        if letter in trash_letters_list:
                            continue
                        else:
                            last_letter = letter
                            break        
                else:
                    last_letter = input_text[-1]
        else:
            if input_text not in cities_list:
                print('Введенного города нет в списке')
            elif last_letter != input_text[0]:
                print('Первая буква введенного города не соответствует последней букве предыдущего либо город уже игрался')
            else:
                used_list.append(input_text)
                if input_text[-1] in trash_letters_list:
                    for letter in input_text[::-1]:
                        if letter in trash_letters_list:
                            continue
                        else:
                            last_letter = letter
                            break
                else:
                    last_letter = input_text[-1]
                        

        print(used_list, last_letter)


if __name__ == '__main__':
    main()