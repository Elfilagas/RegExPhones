import csv
import re
from pprint import pprint


def get_index_by_two_values(first:str, second:str, lst:list)->int:
    """find index of list in list by two first columns"""
    for i, row in enumerate(lst):
        if first == row[0] and second == row[1]:
            return i
        
def main():
    with open("./files/phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    corrected = []
    for line in contacts_list:
        name = re.findall(r"\w+", line[0])
        match len(name):
            case 3:
                line[2] = name[2]
                line[1] = name[1]
                line[0] = name[0]
            case 2:
                line[1] = name[1]
                line[0] = name[0]
        name = re.findall(r"\w+", line[1])
        if len(name) == 2:
            line[1] = name[0]
            line[2] = name[1]
        
        line[5] = re.sub(r"(\+7|8) ?\(?(\d{3})\)?[ -]?(\d{3})-?(\d{2})-?(\d{2})(?:[ (]*(доб\.)? (\d{4})\)?)?", 
                        r"+7(\2)\3-\4-\5 \6\7", line[5]).strip()

        if index := get_index_by_two_values(line[0], line[1], corrected):
            for i in range(len(corrected[index])):
                if not corrected[index][i]:
                    corrected[index][i] = line[i]
        else:
            corrected.append(line)

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(corrected)

if __name__ == "__main__":
    main()    