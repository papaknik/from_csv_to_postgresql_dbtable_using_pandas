# 🐍 Python Script for Creating and Populating PostgreSQL Tables from CSVs

Below you can find a Python script that automatically creates and populates tables in an empty PostgreSQL database with data from CSV files.

## Things to Consider Before Running the Script

- Required Libraries:

Ensure you have the required libraries installed:
  ```
  pip install pandas sqlalchemy psycopg2
  ```
- Database Setup:
  
Create an empty database with a name of your preference before running the script. You may also use the script to add additional tables to an existing DB, but you should be **extremely careful with the existing DB schema**, and possible constraints for foreign keys, data types, indexing, etc. Note that if the files are large enough (e.g., more than 2,000,000 records), be patient and wait a couple of minutes before refreshing your DB GUI tool and see the created tables in the DB

- 🔑 Primary and Foreign Keys:
  
Primary and foreign keys need to be set manually in the database software

- 🔗 Connection Handling:
  
Ensure to connect to the database using with `db.connect() as conn:` instead of manually closing the connection at the end of your script with `close_conn()` to ensure proper completion of the script and avoid possible uncommitted transactions or other issues

- File Names:
  
Check for the validity of your file names because this will be the name of the table in your DB and may lead to issues. Spaces, for example, are not allowed for naming a DB table. The script below replaces any spaces in the file name with an underscore (_). Nevertheless it is better to check this manually, since a file name like 'The&nbsp;&nbsp;&nbsp;Average&nbsp;&nbsp;Noob' will be replaced with 'the___average__noob', which might not be convenient when querying.

- Testing:
  
The script has been tested with a limited number of files (up to 50). It is probable that you may discover more interesting things when testing.

Here’s an example of the script for an empty PostgreSQL database named 'demo':
```python
import pandas as pd
from sqlalchemy import create_engine
import os

# Database connection
conn_string = 'postgresql://postgres::"YOUR_POSTGRESQL_PASSWORD"@localhost/demo'  # Replace with your PostgreSQL password
db = create_engine(conn_string)

# Path to the folder containing the CSV files
path = 'path/to/your/csv/files'  # Replace with the path to the CSV files

# Automatically generate the list of CSV file names
files = [f for f in os.listdir(path) if f.endswith('.csv')] # any CSVs in the above defined path will populate the list 

# Remove spaces and lowercase file names, then load them into the database
with db.connect() as conn: 
    for file in files:
        df = pd.read_csv(os.path.join(path, file))
        df.columns = [col.lower() for col in df.columns]
        table_name = file.replace(' ', '_').replace('.csv', '').lower()
        df.to_sql(table_name, con=conn, if_exists='replace', index=False)
```
**Important Notes**
- Column Case Sensitivity:
  
`df.columns = [col.lower() for col in df.columns]` ensures that columns in the tables are case-insensitive, simplifying queries without needing double quotes every time you need to query a column
- CSV file name Handling:
  
The file names of the CSVs where also converted with `.lower()` method and any empty spaces were replaced by'_', with `table_name = file.replace(' ', '_').lower()`. Otherwise various issues and errors may arise
- Disclaimer:

This script is provided "as-is" for educational and practice purposes

## Sample Data Attribution

The sample CSV files in this repository are obtained from [Kaggle]([https://www.kaggle.com](https://www.kaggle.com/datasets/mahendran1/icc-cricket) and used solely for demonstration purposes. The data files are © Original Authors.


Feel free to experiment, and I hope you find this brief tutorial helpful!
