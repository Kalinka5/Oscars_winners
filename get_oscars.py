import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = "https://en.wikipedia.org/wiki/Academy_Award_for_Best_Actor"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

tables = soup.find_all("table", class_="wikitable sortable")

# get headers to our table
header_elements = tables[0].find_all("th")
headers = [header_element.text.strip()
           for header_element in header_elements][:-3]

# create data frame
df = pd.DataFrame(columns=headers)

# get all data to our table
# each table is tens of year (1920s, 1930s and so on)
for table in tables:
    rows_data = table.find_all("tr")

    # start looping without first empty element
    for row in rows_data[1:]:
        # find first  element (the winner)
        if len(row) == 10:
            # get winning year
            year = row.find("th").text.strip()

            # get all other data
            data_elements = row.find_all("td")
            individual_data = [element.text.strip()
                               for element in data_elements][:-1]

            # insert data by index
            length = len(df)
            df.loc[length] = [year] + individual_data

# convert to csv and save
df.to_csv(r"oscars_winners.csv", index=False)
