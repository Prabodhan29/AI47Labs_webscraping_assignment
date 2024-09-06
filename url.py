# Required imports
import requests
from bs4 import BeautifulSoup
import pandas as pd


hospital_name = []
hospital_url = []
state = []
awards = []

#! Get hospital data
def get_hospital_data(page_number):
    website_url = 'https://www.healthgrades.com/quality/americas-best-hospitals?americasBestAwardType=top250&sort=distance&page=' + str(page_number)
    response = requests.get(website_url)
    soup = BeautifulSoup(response.content, 'html.parser')   
    
    for item in soup.find_all('a', class_='RML7ZoJM_T0OsSL0'):  
        name = item.text.strip()
        link = 'https://www.healthgrades.com/' + item['href']
        hospital_name.append(name)
        hospital_url.append(link)
        
    for item in soup.find_all('div', class_='_uADKqSOi54AaFGS'):
        award_link = item.find('a')
        awards.append(award_link['aria-label'])
        
    for item in soup.find_all('div', class_='SVZInHE3UcK048AL'):
        address_link1 = item.find('address', class_='efB6RomtY4gvWNmF')
        address_link2 = address_link1.find('span', attrs={'data-qa-target': 'location-info-address__city-state'})
        state.append(address_link2.text)
        

for page_number in range(1, 13):
    get_hospital_data(page_number)


#! Export data to CSV
df = pd.DataFrame({'Hospital': hospital_name, 'URL': hospital_url, 'State': state, 'Awards': awards})

#! Data cleaning
# Only contain state abbreviations
df['State'] = df['State'].apply(lambda x: x.split(', ')[1])
df['State'] = df['State'].str.strip()

# Extract the integer 
df['Awards'] = df['Awards'].str.extract('(\d+)') 
df['Awards'] = df['Awards'].fillna(0).astype(int)  # Fill NaN with 0 and convert to integer

#! Export to CSV
df.to_csv('hospital_data.csv', index=False)
print('CSV file exported successfully!')





