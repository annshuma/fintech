import requests

headers = {'content-type': "application/json",
            'authorization': "Basic YW5uc2h1bWFAZ21haWwuY29tOmFubmEyOTA2OTI=",}
response = requests.get("https://api.github.com/user", headers=headers)

print(response.status_code)
print(response.text)