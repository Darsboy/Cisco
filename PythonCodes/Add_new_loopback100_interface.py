import requests

url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces"

payload="{\n    \"ietf-interfaces:interface\": {\n        \"name\": \"Loopback100\",\n        \"description\": \"Configured by DarcyLiu\",\n        \"type\": \"iana-if-type:softwareLoopback\",\n        \"enabled\": true,\n        \"ietf-ip:ipv4\": {\n            \"address\": [\n                {\n                    \"ip\": \"172.16.100.1\",\n                    \"netmask\": \"255.255.255.0\"\n                }\n            ]\n        }\n    }\n}"
headers = {
  'Authorization': 'Basic cm9vdDpEX1ZheSFfMTAm',
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}


response = requests.request("POST", url, headers=headers, data=payload)

print(response)
print(response.text)
