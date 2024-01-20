import csv
from collections import Counter
from nltk.corpus import stopwords

def find_duplicate_phrases_sorted(csv_filename, column_index, output_csv_filename):

    with open(csv_filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row[column_index] for row in reader if len(row) > column_index]

    stop_words = set(stopwords.words('english'))

    phrase_count = Counter(data)

    sorted_phrases = sorted(phrase_count.items(), key=lambda x: x[1], reverse=True)

    with open(output_csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Phrase', 'Frequency'])
        writer.writerows(sorted_phrases)

csv_filename = 'plane.csv'
column_index = 5
output_csv_filename = 'ACtype.csv'
find_duplicate_phrases_sorted(csv_filename, column_index, output_csv_filename)

print(f"排序后的结果已保存到 {output_csv_filename} 文件中。")
