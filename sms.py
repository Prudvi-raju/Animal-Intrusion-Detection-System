import requests

val = input("Enter your value: ")

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {"authorization":"cA1HNurq2FCAxwvL306ABdwvkbvPWSBuY62jQHGQswNDxlT3JM79Kv6eJM5d","message":val+" is detected","language":"english","route":"q","numbers":"6300401682,8688607436,9392304863,9642827247,6302208228"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)