import pandas as pd
from sqlalchemy import create_engine

# Database connection
conn_string = 'postgresql://postgres:"YOUR_POSTGRES_PASSWORD"@localhost/demo' # Replace "YOUR_POSTGRES_PASSWORD" with your password
db = create_engine(conn_string)

# File_Names and Path
files = ['Bowling_ODI', 'Bowling_t20', 'Bowling_test', 'Fielding_ODI', 
         'Fielding_t20', 'Fielding_test', 'ODI  data', 't20', 'test']
path = '/path/to/your/csv/files/'  # Replace with the path to the CSV files

with db.connect() as conn: 
    for file in files: 
        df = pd.read_csv(f'{path}{file}.csv')
        df.columns = [col.lower() for col in df.columns]
        table_name = file.replace(' ', '_').lower()
        df.to_sql(table_name, con=conn, if_exists='replace', index=False)

