import pandas as pd
import sqlalchemy as create_engine
import requests as rq

# please note that each variable would be different for each mysql database and user
MYSQL_HOSTNAME = ''
MYSQL_DATABASE = 'opiodTreatments'
MYSQL_USER = ''
MYSQL_PASSWORD = ''

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

print(engine.table_names())

api = rq.get('https://data.cms.gov/data-api/v1/dataset/f1a8c197-b53d-4c24-9770-aea5d5a97dfb/data')
api = api.json()
api = pd.DataFrame(api)
api.to_csv('data/opiodTreatments.csv')


df = pd.read_csv('data/opiodTreatments.csv')
df.to_sql('opiodData', con=engine, if_exists='append')