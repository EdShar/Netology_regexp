from pprint import pprint
import csv
import re


def read_phonebook():
    with open("phonebook_raw.csv", encoding="utf8") as f:
        rows = csv.reader(f, delimiter=",")
        next(rows)
        contacts_list = list(rows)
    return contacts_list


def join_names(contact_list):
    names = []
    for contact in contact_list:
        names.append(' '.join(contact[:3]).strip().split(' '))

    return names


def update_names(phonebook, new_names):
    for str_el in range(len(phonebook)):
        phonebook[str_el][:3] = new_names[str_el][:3]


def edit_phone(phonebook):
    phone_pattern_main = re.compile(r'(\+7)(\(\d{3}\))(\d{3}-\d{2}-\d{2})')
    for phone in phonebook:
        print(phone[5])
        match = phone_pattern_main.match(phone[5])
        print(match)

    # phone_pattern_ext = re.compile(r'(\+7)(\(\d{3}\))(\d{3}-\d{2}-\d{2}) (доб.\d{4})')
    # for phone in phonebook:
    #     print(phone[5])
    #     match = re.findall(phone_pattern_ext, phone[5])
    #     print(match)

        # if match:
        #     phone_prefix = match.group(1)
        #     area_code = match.group(2)
        #     number = match.group(3)
        #     extension = match.group(4)
        #     print(f'Префикс: {phone_prefix}')

        #     formatted_phone = f"{phone_prefix}({area_code}){number} {extension}"
        # else:
        #     formatted_phone = re.sub(r'\D', '', phone)
        #     formatted_phone = re.sub(r'(\d)(\d{3})(\d{3})(\d{2})(\d{2})', r'+7(\2)\3-\4-\5', formatted_phone)
        #
        # phone[5] = formatted_phone

        # (\+7)(\(\d{3}\))(\d{3})-(\d{2})-(\d{2}) (доб.\d{4})|(\+7)(\(\d{3}\))(\d{3})-(\d{2})-(\d{2})

def create_phonebook(contacts_list):
    with open("phonebook.csv", "w", encoding="utf8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


if __name__ == '__main__':
    main_phonebook = read_phonebook()
    edit_phone(main_phonebook)

    # formatted_names = join_names(main_phonebook)
    # update_names(main_phonebook, formatted_names)


