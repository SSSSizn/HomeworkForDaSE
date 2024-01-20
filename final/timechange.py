import csv

def process_and_write_txt(input_csv_filename, output_txt_filename):
    with open(input_csv_filename, 'r') as infile, open(output_txt_filename, 'w') as outfile:
        reader = csv.reader(infile)

        for row in reader:
            if len(row) > 1:
                time_str = row[1]

                if time_str.isdigit() and 1 <= len(time_str) <= 3:
                    new_time_str = time_str.zfill(4)
                    row[1] = new_time_str

                outfile.write(f"{row[1]}\n")


input_csv_filename = 'plane.csv'
output_txt_filename = 'new.txt'
process_and_write_txt(input_csv_filename, output_txt_filename)
