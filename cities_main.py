import string


def main():
    test_list = ['архангельск', 'астрахань', 'москва', 'норильск', 'калуга']
    used_list = []
    last_letter = ''


    while True:
        input_text = input()


        if not used_list:
            if input_text not in test_list:
                print('Введенного города нет в списке')
            else:
                used_list.append(input_text)
                last_letter = input_text[-1]
        else:
            if input_text not in test_list:
                print('Введенного города нет в списке')
            elif last_letter != input_text[0]:
                print('Первая буква введенного города не соответствует последней букве предыдущего')
            else:
                used_list.append(input_text)
                last_letter = input_text[-1]

        print(used_list, last_letter)


if __name__ == '__main__':
    main()