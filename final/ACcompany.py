import csv
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

def extract_keywords(csv_filename, column_index, output_csv_filename, top_n=80):
    with open(csv_filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row[column_index] for row in reader if len(row) > column_index]

    text = ' '.join(data)
    words = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    freq_dist = FreqDist(words)

    top_keywords = freq_dist.most_common(top_n)

    with open(output_csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Keyword', 'Frequency'])
        writer.writerows(top_keywords)

csv_filename = 'plane.csv'
column_index = 5
output_csv_filename = 'ACcompany.csv'
extract_keywords(csv_filename, column_index, output_csv_filename, top_n=80)

print(f"提取的关键词已保存到 {output_csv_filename} 文件中。")
