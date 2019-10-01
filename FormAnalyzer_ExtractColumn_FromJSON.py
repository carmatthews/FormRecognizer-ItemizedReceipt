#sample code for iterating through a section of the JSON returned by Form Recognizer to get to the contents of tables in the documents

import json

jsonfilename = 'Tesco_Receipt_Example.json'

with open(jsonfilename, "r") as read_file:
    receipt = json.load(read_file)

def getColumnEntries (jsonDict, headertext):
    columnentries = []

    for page in jsonDict['pages']:
        for table in page['tables']:
            #FOR DEBUG print ("Table ids are: " + table.get('id'))
            for column in table['columns']:
                #FOR DEBUG print(column.get('header')[0].get('text'))
                for header in column['header']:
                    #FOR DEBUG print(header.get('text'))
                    if header.get('text') == headertext:
                        #FOR DEBUG print(column.get('header'))
                        for entry in column['entries']:
                            #FOR DEBUG print(entry)
                            for entryitem in entry:
                                #FOR DEBUG print(entryitem.get('text'))
                                columnentries.append(entryitem.get('text'))

    return columnentries

print(getColumnEntries(receipt, 'Product'))
# Options for the Tesco Receipts are Quantity, Product, Total

