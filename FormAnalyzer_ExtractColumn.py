########### Python Form Recognizer Analyze Example #############
from requests import post as http_post

# function that iterates through the dictionary containing results from Form Recognizer Analysis
# this function will specifically look for a column header in a table (e.g. headertext) within the document
def getColumnEntries (jsonDict, headertext):
    columnentries = []

    for page in jsonDict['pages']:
        for table in page['tables']:
            #FOR DEBUG print ("Table ids are: " + table.get('d'))
            for column in table['columns']:
                #FOR DEBUG print(column.get('header')[0].get('text'))
                for header in column['header']:
                    #FOR DEBUG print(header.get('text'))
                    if header.get('text') == headertext:
                        #FOR DEBUG print(column.get('header'))
                        for entry in column['entries']:  #Note that entries are a list of a list of dictionaries so extra step here
                            #FOR DEBUG print(entry)
                            for entryitem in entry:
                                #FOR DEBUG print(entryitem.get('text'))
                                columnentries.append(entryitem.get('text'))

    return columnentries


# To run against a live Form Recognizer Model 

# Setting up to execute against Form Recognizer API
# Endpoint URL - will need to change this based on the region your cognitive services are deployed to.  
base_url = r"https://westus2.api.cognitive.microsoft.com" + "/formrecognizer/v1.0-preview/custom"

#File path to file you want to analyze - change the path to your working directory with the example file in it
file_path = r"c:\[path to your file]\Tesco_Receipt_Example.pdf"

#Model_id - you will get this from the result of the training step
model_id = "<Your model id here>"

headers = {
    # Request headers
    'Content-Type': 'application/pdf',
    'Ocp-Apim-Subscription-Key': '<Your Key Here>',  #your Azure subscription key for cognitive services
}

# Setup the column you will extract - this is based on the PDF forms you are using.  
# In the case of the Tesco receipt, the column header "Product" is the header for the entries that contain the text for the items
columnheader = 'Product'
columnentries = []
try:
    url = base_url + "/models/" + model_id + "/analyze" 
    with open(file_path, "rb") as f:
        data_bytes = f.read()  
    resp = http_post(url = url, data = data_bytes, headers = headers)

    columnentries = getColumnEntries(resp.json(), columnheader)
    
    #DEBUG print(url)
    #DEBUG print("Response body:\n%s" % resp.json())   
    print("Response status code: %d" % resp.status_code)  
    print("{} entries: %s".format(columnheader) % columnentries)  
except Exception as e:
    print(str(e))