# Python program to demonstrate
# writing to CSV


import csv
  
# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']
  
# data rows of csv file
rows = [['1/2 NLH', '2', '5', ''], ['1/2 NLH w/BP', '2', '4', ''], ['1/3 NLH', '1', '1', ''], ['2/5 NLH', '0', '1', ''], ['5/10 NLH (Sat 3PM)', '0', '0', ''], ['1/2/5 PLO', '0', '6', ''], ['1/1 PLO w/ $5 BP', '0', '6', ''], ['10/25 PLO (Sun @ 2PM)', '0', '0', ''], ['$5 PLO Bomb Pots', '0', '1', ''], ['4/8 Limit Mix', '0', '0', ''], ['Lodge Live Stream', '0', '0', ''], ['$1/2 NLH', '1', '0', ''], ['$1/3 NLH', '0', '0', ''], ['$1/2/5 PLO TUE 11AM', '1', '2', ''], ['$1/2/5 PLO FRI 1PM', '0', '7', ''], ['$1/2/5 PLO', '0', '1', ''], ['ROUND & ROUND', '0', '0', ''], ['$2/5 NLH', '0', '1', ''], ['$5 PLO Bomb Pots', '0', '0', ''], ['$1/2/5 BIG O', '0', '0', ''], ['$100 SIT N GO', '0', '2', ''], ['$5/10 MIX THURS 6PM', '0', '0', '']]

  
# name of csv file
filename = "university_records.csv"
  
# writing to csv file
with open(filename, 'w') as csvfile:
  # creating a csv writer object
  csvwriter = csv.writer(csvfile)
    
  # writing the fields
  csvwriter.writerow(fields)
    
  # writing the data rows
  csvwriter.writerows(rows)
