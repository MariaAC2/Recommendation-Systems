from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.exceptions import APIException
from recombee_api_client.api_requests import *
import pandas as pd
import uuid

client = RecombeeClient('universityproject-upb-db',  'HTZGfcry85wdv110Cwmie21hudn0ygIEZ5vbgnwgUOhlD7xuGizHhEc44xcQ2aZp', region=Region.EU_WEST)

client.send(AddItemProperty('description', 'string'))

df = pd.read_csv('nike_data_2022_09.csv')

df['itemId'] = [str(uuid.uuid4()) for _ in range(len(df))]

for _, row in df.iterrows():
    item_id = str(row['itemId'])

    client.send(AddItem(item_id))

    client.send(SetItemValues(
        item_id,
        {
            'name': row['name'],
            'url': row['url'],
            'price': float(row['price']),
            'description': row['description']
        },
        cascade_create=True
    ))

client.send(AddUserProperty('sales_person', 'string'))
client.send(AddUserProperty('sp_id', 'string'))
client.send(AddUserProperty('team', 'string'))
client.send(AddUserProperty('location', 'string'))

df = pd.read_csv('people.csv')

for _, row in df.iterrows():
    item_id = str(row['sp_id'])

    client.send(AddUser(item_id))

    client.send(SetUserValues(
        item_id,
        {
            'sales_person': row['sales_person'],
            'team': row['team'],
            'location': row['location']
        },
        cascade_create=True
    ))