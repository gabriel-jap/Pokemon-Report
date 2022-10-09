import requests
import pandas as pd
from bs4 import BeautifulSoup

site="https://www.wikidex.net/wiki/Lista_de_movimientos"
response=requests.get(site)
if response.status_code == 200:	
	web=response.text
	soup=BeautifulSoup(web)
	print('Success!')
tab=soup.find_all("table")
#Skip types table
tab.pop(0)
#Skip Index of the table
tab.pop(0)
#create the intermediates
nameESP=[]
nameENG=[]
tipe=[]
cat=[]
#Read each table
for table in tab:
	lines=table.find_all("tr")
	#Drop the header
	lines.pop(0)
	#Read each row and extract the info
	for line in lines:
		info=line.find_all("td")
		nameESP.append(info[0].get_text(strip=True))
		tipe.append(info[1].a["title"])
		cat.append(info[2].a["title"])
		nameENG.append(info[4].get_text(strip=True))
#Create a dictionary to form the Dataframe
dict={
    "Spanish":nameESP,
    "English":nameENG,
    "Type":tipe,
    "Class":cat
}
df = pd.DataFrame.from_dict(dict)
#Export CSV
df.to_csv("moves.csv")