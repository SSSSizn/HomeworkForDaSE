import requests
from bs4 import BeautifulSoup
import csv

for year in range(2000,2025):
    response = requests.get(f'https://www.planecrashinfo.com/{year}/{year}.htm')
    trs = BeautifulSoup(response.text,'html.parser').find_all('tr')
    for tr in trs:
        url_content = tr.find('td').find('a')
        if url_content != None:
            url = (f'https://www.planecrashinfo.com/{year}/'+url_content.get('href'))
            response_detail = requests.get(url)
            trs_detail = BeautifulSoup(response_detail.text,'html.parser').find_all('tr')
            result = []
            for tr_detail in trs_detail:
                row_title = (tr_detail.find('td').text.replace('\n',''))
                if ('Date' in row_title) | ('Operator' in row_title)| ('Type' in row_title)| ('Aboard' in row_title) | \
                    ('Fatalities' in row_title) | ('Summary' in row_title):
                    result.append(tr_detail.find_all('td')[-1].text.replace('\n',''))
            print(result + [url])
            with open(f'plane.csv', encoding='utf-8-sig', mode='a', newline='')as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(result + [url])