import csv

def read_csv(file_path):
    url_start_end = []
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            url_start_end.append( [row['Url'],int(row['Start']),int(row['End']) ])
    return url_start_end