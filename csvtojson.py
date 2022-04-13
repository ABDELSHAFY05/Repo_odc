#convert csv file to json using pandas
# import csv
# import json

# csvfile = open('ouput.csv', 'r')
# jsonfile = open('json.json', 'w')
# count = 0
# fieldnames = ("Name","time","date")
# reader = csv.DictReader( csvfile, fieldnames)
# for row in reader:
#     count += 1
#     json.dump(row, jsonfile)
#     jsonfile.write('\n')
# print(f'{count} rows added. ')
import pandas as pd
csv_file = pd.DataFrame(pd.read_csv("ouput.csv", sep = ",", header = 0, index_col = False))
csv_file.to_json("json.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
print(csv_file)