## Bar Graphs the top 5 Salary's in the current NBA

import matplotlib.pyplot as plt
import csv
x = []
y = []
filename = 'NBA_season1718_salary.csv'
with open(filename) as f:
   reader = csv.reader(f)
   header_row = next(reader)
   for index, column_header in enumerate(header_row):
       print(index, column_header)
   for row in reader:
       x.append(row[1])
       y.append(row[3])
plt.xlabel('x')
plt.ylabel('y')
plt.bar(x,y)
plt.show()

