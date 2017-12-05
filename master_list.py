import csv
import pprint

def ret_list(new_csv):
    with open(new_csv, 'r') as f:
        reader = csv.reader(f)
        lister = list(reader)

    return lister
