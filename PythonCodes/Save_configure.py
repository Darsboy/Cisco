import requests

url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/operations/cisco-ia:save-config/"

payload={}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic cm9vdDpEX1ZheSFfMTAm'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response)
print(response.text)
