import pandas as pd
from sqlalchemy import create_engine
import os

# Database connection
conn_string = 'postgresql://postgres:"YOUR_POSTGRESQL_PASSWORD"@localhost/demo'  # Replace with your PostgreSQL password
db = create_engine(conn_string)

# Path to the folder containing the CSV files
path = 'path/to/your/csv/files'  

# Automatically generate the list of CSV file names
files = [f for f in os.listdir(path) if f.endswith('.csv')]

# Remove spaces and lowercase file names, then load them into the database
with db.connect() as conn: 
    for file in files:
        df = pd.read_csv(os.path.join(path, file))
        df.columns = [col.lower() for col in df.columns]
        table_name = file.replace(' ', '_').replace('.csv', '').lower()
        df.to_sql(table_name, con=conn, if_exists='replace', index=False)




