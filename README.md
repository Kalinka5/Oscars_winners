# 🌟 Oscars Winners Data Scraper 🌟

This Python project scrapes data from a Wikipedia page that lists all Academy Award winners for Best Actor. The script extracts the data from tables, processes it, and saves it into a CSV file. The resulting CSV contains a clean table with all winners organized by year.

---

## 📊 Features
- 🔎 Scrapes tables of Best Actor Oscar winners directly from Wikipedia.
- 📊 Extracts structured data: **Year**, **Actor Name**, **Movie Title**, and additional details.
- 🔧 Saves the extracted data into a CSV file for further analysis.

---

## 🛠️ Prerequisites
Ensure you have Python installed (version 3.8 or higher is recommended).

To run this project, you'll need the following Python libraries:
- 💪 `requests` - for sending HTTP requests to fetch the Wikipedia page.
- 🌐 `beautifulsoup4` - for parsing the HTML content.
- 📅 `pandas` - for creating and manipulating the data table.

You can install all the required dependencies using the `requirements.txt` file.

---

## 👨‍💻 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Kalinka5/Oscars_winners.git
   cd Oscars_winners
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv .venv  # Or python3 -m venv .venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💡 How to Run the Script

Run the Python script to fetch the data and save it to a CSV file:

```bash
python get_oscars.py
```

📦 After execution, the script generates a file named **oscars_winners.csv** in the same directory.

---

## 🧐 Code Explanation
Below is a breakdown of the key components of the script:

### 1. Importing Required Libraries
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
```
These libraries are essential for sending HTTP requests, parsing HTML, and handling tabular data.

### ↩️ 2. Sending a Request to Wikipedia
```python
URL = "https://en.wikipedia.org/wiki/Academy_Award_for_Best_Actor"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
```
- **`requests.get()`** fetches the page content.
- **`BeautifulSoup`** parses the page's HTML to extract meaningful data.

### ⚡ 3. Locating the Target Tables
```python
tables = soup.find_all("table", class_="wikitable sortable")
```
The script finds all tables with the class `wikitable sortable` on the Wikipedia page.

### 🔄 4. Extracting Table Headers
```python
header_elements = tables[0].find_all("th")
headers = [header_element.text.strip() for header_element in header_elements][:-3]
```
- Extracts the column headers from the first table.
- **`.text.strip()`** removes any unnecessary whitespace.

### 🔢 5. Creating a DataFrame
```python
df = pd.DataFrame(columns=headers)
```
Initializes an empty Pandas DataFrame with the extracted headers.

### 🤝 6. Extracting and Processing Table Data
```python
for table in tables:
    rows_data = table.find_all("tr")
    for row in rows_data[1:]:
        if len(row) == 10:
            year = row.find("th").text.strip()
            data_elements = row.find_all("td")
            individual_data = [element.text.strip() for element in data_elements][:-1]
            length = len(df)
            df.loc[length] = [year] + individual_data
```
- Iterates through each row of each table.
- Extracts the **Year** and corresponding data (Actor, Movie, etc.).
- Appends the row to the DataFrame.

### 📃 7. Saving Data to CSV
```python
df.to_csv(r"oscars_winners.csv", index=False)
```
Finally, the script saves the DataFrame to a CSV file named **oscars_winners.csv**.

---

## 📤 Output
The resulting **oscars_winners.csv** file contains clean, structured data with the following columns:
- **Year**: The year the award was given.
- **Actor**: The name of the winning actor.
- **Film**: The title of the film for which the actor won the award.

📅 Sample output in the CSV file:
```csv
Year,Actor,Film
1929,Emil Jannings,The Last Command / The Way of All Flesh
1930,Warner Baxter,In Old Arizona
1931,George Arliss,Disraeli
```

---

## 🔧 Troubleshooting
- If you encounter connection issues, ensure you have a stable internet connection.
- Verify that the Wikipedia page structure (HTML) has not changed, as it may affect the scraping logic.
- Update libraries to their latest versions if you encounter compatibility issues:
   ```bash
   pip install --upgrade requests beautifulsoup4 pandas
   ```

---

🛠️📏 Happy Scraping! 🛠️📏
