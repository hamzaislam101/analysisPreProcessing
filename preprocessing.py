
import csv

#create a function to read a csv file and copy rows to new csv file
def read_csv(file_name):
    with open(file_name, 'r') as csv_file:
        with open('new_csv.csv', 'a') as new_csv:
            writer = csv.writer(new_csv,delimiter=",", lineterminator='\n')
            filtered = (line.replace('\n', '') for line in csv_file)
            for row in csv.reader(filtered):
                if ',' in row[1]:
                    genres = row[1].split(',')
                    for genre in genres:
                        data = [row[0], genre.strip(), row[2]]
                        writer.writerow(data)
                else:
                    writer.writerow(row)


read_csv("nodes.csv")
print("done")
