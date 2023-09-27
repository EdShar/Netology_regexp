from pprint import pprint
import csv
import re
from collections import defaultdict


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


def edit_phone(contacts_list):
    for phone in contacts_list:
        if phone[5] != '':
            phone[5] = re.sub(r'\s+', '', phone[5])
            phone[5] = re.sub(r'\+7', '8', phone[5])
            phone[5] = re.sub(r'\(|\)|\-|доб.', '', phone[5])

            phone_prefix = '+7'
            area_code = phone[5][1:4]
            number = f'{phone[5][4:7]}-{phone[5][7:9]}-{phone[5][9:11]}'
            extension = None

            if len(phone[5]) > 11:
                extension = phone[5][11:15]

            if extension is not None:
                phone[5] = f'{phone_prefix}({area_code}){number} доб.{extension}'
            else:
                phone[5] = f'{phone_prefix}({area_code}){number}'


def find_duplicates(contacts_list):
    data = defaultdict(list)

    for info in contacts_list:
        key = tuple(info[:2])
        for item in info:
            if item not in data[key]:
                data[key].append(item)

    new_list = list(data.values())
    return new_list


def create_phonebook(contacts_list):
    with open("phonebook.csv", "w", encoding="utf8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


if __name__ == '__main__':
    main_phonebook = read_phonebook()
    edit_phone(main_phonebook)
    formatted_names = join_names(main_phonebook)
    update_names(main_phonebook, formatted_names)
    create_phonebook(find_duplicates(main_phonebook))

