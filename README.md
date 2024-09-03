# 🐍 Python Script for Creating and Populating PostgreSQL Tables from CSVs

Below you can find a Python script that automatically creates and populates tables in an empty PostgreSQL database using data from CSV files.

## Things to Consider Before Running the Script

- **Required Libraries**:

  Ensure you have the required libraries installed:
  ```
  pip install pandas sqlalchemy psycopg2
  ```
- If  the files are large enough (e.g., more than 1,000,000 records), be patient and wait a few seconds before refreshing your DB GUI tool and see the created tables in the DB

- 🔑 Primary and Foreign Keys: These have to be set manually inside the DB software.

- 🔗 Connection Handling: Ensure to connect to the database using with `db.connect() as conn:` instead of manually closing the connection at the end of your script with `close_conn()` to ensure proper completion of the
  script and avoid possible uncommitted transactions or other issues.

- File Names: Check for the validity of your file names because this will be the name of the table in your DB and may lead to issues. Spaces, for example, are not allowed for naming a DB table. The script below replaces
  any spaces in the file name with an underscore (_). Nevertheless it is better to check this manually, since a file name like 'The&nbsp;&nbsp;&nbsp;Average&nbsp;&nbsp;Noob' will be replaced with 'the___average__noob', which might not be convenient for a DB table name.

- Database Setup: Create an empty database before running the script. You may use the script to add additional tables to an existing DB, but you should be extremely careful with the existing DB schema, and its constraints for    foreign keys, data types, indexing, etc. 

- Testing: The script has been tested with a limited number of files (up to 50). Feel free to experiment, and you may discover more interesting things.

Here’s an example of the script for a PostgreSQL database named 'demo':
```python
import pandas as pd
from sqlalchemy import create_engine

# Database connection
conn_string = 'postgresql://postgres:"YOUR_POSTGRESQL_PASSWORD"@localhost/demo'
db = create_engine(conn_string)

# File paths
files = ['file001', 'file002', 'file003', 'file004']  # Replace with your CSV file names
path = '/path/to/your/csv/files/'  # Replace with the path to your CSV files

with db.connect() as conn: 
    for file in files: 
        df = pd.read_csv(f'{path}{file}.csv')
        df.columns = [col.lower() for col in df.columns]
        table_name = file.replace(' ', '_').lower()
        df.to_sql(table_name, con=conn, if_exists='replace', index=False)
```
**Important Notes**
- Column Case Sensitivity: `df.columns = [col.lower() for col in df.columns]` ensures that columns in the tables are case-insensitive, simplifying queries without needing double quotes
- The file names where also converted with `.lower()` method and any empty spaces were replaced by'_', because it was found that they were causing various issues as well
- This script is provided "as-is" for educational and practice purposes.

Feel free to experiment, and I hope you find this brief tutorial useful!
