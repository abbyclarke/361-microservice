from bs4 import BeautifulSoup
import requests
import time
import json

with open("companies.json", "r") as infile:
    companies_dict = json.load(infile)

while True:
    time.sleep(2)
    f = open('salary.txt', 'r')
    company = f.readline()
    if company and "$" not in company and "Could not find" not in company:
        f.close()

        url = f"https://www.levels.fyi/internships/{company}/Software-Engineer-Intern/"
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        error_404 = soup.find("div", class_="not-found-message text-left")
        
        if error_404 == None:

            hourly_salary = soup.find("span", class_="row-hourly-salary").text
            monthly_salary = soup.find("span", class_="row-monthly-salary").text

            with open('salary.txt', 'w') as f:
                f.write(f"{hourly_salary} per hour, {monthly_salary} per month")
        
        else:
            company_lower = company.lower()
            if company_lower in companies_dict:
                new_company = companies_dict[company_lower]
                url = f"https://www.levels.fyi/internships/{new_company}/Software-Engineer-Intern/"
                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')
                hourly_salary = soup.find("span", class_="row-hourly-salary").text
                monthly_salary = soup.find("span", class_="row-monthly-salary").text

                with open('salary.txt', 'w') as f:
                    f.write(f"{hourly_salary} per hour, {monthly_salary} per month")
            else:
                with open('salary.txt', 'w') as f:
                    f.write(f"Could not find {company}'s salary")



