import requests
import pandas as pd
from bs4 import BeautifulSoup

site="https://www.wikidex.net/wiki/Movimiento_Z"
response=requests.get(site)
if response.status_code == 200:	
	web=response.text
	soup=BeautifulSoup(web)
	print('Success!')

tables=soup.find_all("table")
#Skip the first table
tables.pop(0)
#Drop the last table
tables.pop(-1)

z=[]

for table in tables:
    lines=table.find_all("tr")
	#Drop the header
    lines.pop(0)
	#Read each row and extract the info
    for line in lines:
        z.append(line.find_all("td")[1].get_text(strip=True))

df = pd.DataFrame(z,columns=["Spanish"])

df.to_csv("zMoves.csv")
