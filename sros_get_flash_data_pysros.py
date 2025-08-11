#!/opt/gums/bin/python3
from pysros.management import connect

# Connect to router
connection = connect(
    host="rtr1",
    username="username",
    password="password",
    hostkey_verify=False,
)

# Get flash data
data = connection.running.get('/nokia-state:state/cpm[cpm-slot="A"]/flash')

# Cleanup connection to router
connection.disconnect()

# Format the retrieved data
for flash_id, flash_info in data.items():
    print(f"Flash {flash_id}:")
    for key, value in flash_info.items():
        val = value.data if hasattr(value, "data") else str(value)
        print(f"  {key}: {val}")
