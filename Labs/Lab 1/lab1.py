from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.exceptions import APIException
from recombee_api_client.api_requests import *

client = RecombeeClient('universityproject-upb-db',  'HTZGfcry85wdv110Cwmie21hudn0ygIEZ5vbgnwgUOhlD7xuGizHhEc44xcQ2aZp', region=Region.EU_WEST)

client.send(AddItemProperty('name', 'string'))
client.send(AddItemProperty('url', 'string'))
client.send(AddItemProperty('price', 'double'))
