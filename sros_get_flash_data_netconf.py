#!/opt/gums/bin/python3
import xml.etree.ElementTree as ET

from ncclient import manager

connection = manager.connect(
    host="rtr1",
    username="username"
    password="password",
    hostkey_verify=False,
    allow_agent=False,
)

if connection is not None:
    # Get flash data using proper ncclient get method
    filter_xml = """
        <state xmlns="urn:nokia.com:sros:ns:yang:sr:state">
            <cpm>
            <cpm-slot>A</cpm-slot>
            <flash/>
            </cpm>
        </state>
        """
    response = connection.get(filter=("subtree", filter_xml))
    data = response.data

    # Convert XML to readable string with pretty formatting
    ET.indent(data, space="  ")
    xml_str = ET.tostring(data, encoding="unicode")
    print(xml_str)

    # Cleanup connection to router
    connection.close_session()
else:
    raise ConnectionError("Failed to establish NETCONF connection; 'connection' is None.")
