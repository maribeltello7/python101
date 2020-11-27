import csv

def readCSVfile():
    with open('C:\\Users\\mari_\\Downloads\\email.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
                line_count += 1
            else:
                print(row)
                line_count += 1
        print(f'Processed {line_count} lines.')


if __name__ == '__main__':
    readCSVfile()
