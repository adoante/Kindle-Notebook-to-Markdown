import csv
import sys

user_args = (sys.argv)

with open(str(user_args[1]), encoding='utf-8-sig') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	output_file = open(str(user_args[2]) + ".md","w", encoding='utf-8')
	for row in csv_reader:
		if line_count == 8:
			if (row[0] == 'Note'):
				output_file.write("- Note: " + str(row[3]) + "\n" + "\n")
			else:
				output_file.write("> " + str(row[3]) + "\n" + "\n")
		else:
			line_count += 1
	output_file.close()