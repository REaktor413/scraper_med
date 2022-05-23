import requests
from bs4 import BeautifulSoup
import lxml
import json


headers = {'Mozilla/5.0': '(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}


# get all pages and collect data
for page in range(1, 26):
    print(f"Processing page # {page}")
    url = f"https://www.mortgageandfinancehelp.com.au/find-accredited-broker/?page={page}&query=&location=2000"

    req = requests.get(url=url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all('a', class_='viewdetails_button standard')

    for item in cards:
        collect_data = {}
        collect_data['Name'] = item.get('data-preferred_name')
        collect_data['Last_name'] = item.get('data-last_name')
        collect_data['Phone'] = item.get('data-phone')
        collect_data['Mobile'] = item.get('data-mobile')
        collect_data['Email'] = item.get('data-email')
        collect_data['ID'] = item.get('data-external_id')
        collect_data['City'] = item.get('data-city')
        collect_data['State'] = item.get('data-state')
        collect_data['Company'] = item.get('data-company')
        result_list.append(collect_data)
# save results in json
with open("result.json", "a", encoding="utf-8") as file:
    json.dump(result_list, file, indent=4, ensure_ascii=False)

print(f"Finish")
