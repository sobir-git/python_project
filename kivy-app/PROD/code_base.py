import csv
"""
#csvfile= open('library.csv', 'r').read()
def view_file(file_name):
    csvName= file_name + '.csv'
    with open(csvName, 'r') as csvfile:
        library = csv.reader(csvfile, delimiter=',')
        for row in library:
            print(row)
        return csvfile


def addRow(csv_column):
    with open('library.csv', 'w') as csvfile:
        lib_writer = csv.writer(csvfile, dialect='excel')
        lib_writer.writerow(csv_column)
    return csvfile


column = ['My hero academics', 'fighting', 'midoriya']

addRow(column)
view_file('library')"""
test_input= input("Test name: ")

newList= [test_input, "test1", "test2"]
with open('library.csv', 'r') as readcsvfile:
    readFile= csv.reader(readcsvfile)
    header= next(readFile)



with open('library.csv', 'a', newline='') as csvfile:
    print(header)
    fileUpdate= csv.writer(csvfile)
    fileUpdate.writerow(newList)