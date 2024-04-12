import azure.functions as func
from azure.cosmos import CosmosClient
import logging
import json
import uuid

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

#URL and key to acces our cosmosDB instance ( will have to be subbed by KeyVault)
url = "https://nbremotemond97a1.documents.azure.com:443/"
key = "2zOQ1PXR0Lx0ICGnyIxBhDoRiQQC3kAWXWXDqfKD7UrY2R8p6nJTAXSQ46f7YlcZ6mM1M6QoE1r0EYHW8olxiw=="

#Setup shared client connection
client_cosmos = CosmosClient(url,key)

database_name = "IOTDB"
container_name = "energyRaw"
            
            
            
database = client_cosmos.get_database_client(database=database_name)
container = database.get_container_client(container=container_name)
           
items = list(container.query_items(query='SELECT * from c where c.deviceid LIKE @deviceid',
                                        parameters=[dict(name="@deviceid",value="bpi_%"),],
                                        enable_cross_partition_query=True
                                 )
                        )
count =0
total = len(items)            
for item in items:
    count +=1
    container.delete_item(item=item['id'], partition_key= item['deviceid'])
    print(f"{count}/{total}")
print("Done")