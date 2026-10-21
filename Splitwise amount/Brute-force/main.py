import argparse
import re 
from Splitwise import Splitwise

def main() :

    (members, expenses) = parse_input_file("input_files\input_file.txt")
    splitwise = Splitwise(members, expenses)
    transactions = splitwise.split_expense()

    print_output(transactions)

def print_output(transactions):

    print('-' * 75)
    print("OUTPUT")
    for x in transactions:
        print(x[0], '->', x[1], x[2])
    print('-' * 75)


def parse_input_file(input_file):

    with open(input_file, 'r') as f: 

        read_data = f.readlines() 
        members = read_data[0]
        members_list = re.findall(r'[a-zA-Z]', members) 

        expenses = []
        for line in read_data[2:]:
            expenses.append(line)

        expenses_list_temp = [re.sub('[\n]', '', x).split() for x in expenses]
        expenses_list = [(x[0], float(x[1]), x[2]) for x in expenses_list_temp]

        print('-' * 75)
        print("INPUT")
        print ("Reading input file", "input_files\input_file.txt")
        print ("Input Members", members_list)
        print ("Input Expenses", expenses_list)
        print('-' * 75)

        return members_list, expenses_list


if __name__ == '__main__':

    print("*" * 75)
    print("SPLITWISE EXPENSE DISTRIBUTION") 
    print("*" * 75)

    main() 