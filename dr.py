from numpy import source
import pandas as pd
from bs4 import BeautifulSoup
import requests
import openpyxl
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'details'
print(excel.sheetnames)
sheet.append(['Full Name', 'Specialty', 'Address', 'Phone', 'URl'])


try:
    source = requests.get(
        "https://www.stfrancismedicalcenter.com/find-a-provider/")
    source.raise_for_status()
    soup = BeautifulSoup(source.text, "lxml")
    doctors = soup.find_all('div', class_="info")
    # print((doctors))

    for doctor in doctors:

        name = doctor.find('span', class_="title-style-5").text
        phone = doctor.find(
            'li', class_="inline-svg phone").get_text(strip=True)
        address = doctor.find('address', class_="mar-e-0").get_text(strip=True)
        speciality = doctor.find(
            'div', class_="specialty-list items-1 note-style-1 ui-repeater").get_text(strip=True)
    #     city = doctor.find('address', class_="mar-e-0").get_text(
    #         strip=True).split(",")[2]

        sheet.append([name, speciality, address, phone, ])

    # for link in soup.find_all('a', class_="flex-top-between-block-500"):
    #     urlt = link.get('href')
    #     sheet.append([urlt])

except Exception as e:
    print(e)
excel.save('doctordetails.xlsx')
