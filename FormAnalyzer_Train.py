########### Python Form Recognizer Train #############
from requests import post as http_post

# Endpoint URL
# replace with the URL for the region your cognitive service is in
base_url = r"<https://westus2.api.cognitive.microsoft.com>" + "/formrecognizer/v1.0-preview/custom"

#replace this with the SAS URL for the blob storage containing the training files
source = r"<https://xxxx.blob.core.windows.net/train?st=xxxx>"
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '<replace with your key>',
}
url = base_url + "/train" 
body = {"source": source}
try:
    resp = http_post(url = url, json = body, headers = headers)
    print("Response status code: %d" % resp.status_code)
    print("Response body: %s" % resp.json())
except Exception as e:
    print(str(e))