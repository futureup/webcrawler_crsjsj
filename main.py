import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

def save_to_csv(url):
    html = urlopen(url)
    if 'text/html' in html.getheader('Content-Type'):
        html_bytes = html.read()
        html_string = html_bytes.decode("utf-8")

    bsObj = BeautifulSoup(html_string, "lxml")
    table = bsObj.findAll("table")[3]
    rows = table.findAll("tr")
    csvFile = open("editors.csv", 'at', newline='', encoding="utf-8")
    writer = csv.writer(csvFile)
    try:
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)
            # print(csvRow)
    finally:
        csvFile.close()

save_to_csv('http://www.crs.jsj.edu.cn/index.php/default/approval/detail/386')
'''
def get_course_link(province_url):
    source_code = requests.get(province_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    for link in soup.findAll('a'):
        course_link = link.get('href')
        print(course_link)

        if "http://www.crs.jsj.edu.cn/index.php/default/approval/detail/" in course_link:
            save_to_csv(course_link)
        else:
            print('not in list')


for i in range(1, 32):
    province_link = 'http://www.crs.jsj.edu.cn/index.php/default/approval/getbyarea/' + str(i)
    get_course_link(province_link)
'''