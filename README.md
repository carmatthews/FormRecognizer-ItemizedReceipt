# FormRecognizer-ItemizedReceipt
Sample Python function for extracting items from a table in a form (in this example, a grocery store receipt) that has been processed with an Azure Form Recognizer model.

## Prerequisites ##
You need to install Python and setup a Form Recognizer service on Azure.  

1. Instructions for requesting access to Form Recognizer and installing python are [here](https://docs.microsoft.com/en-us/azure/cognitive-services/form-recognizer/quickstarts/python-train-extract#prerequisites).

2. Once you have Form Recognizer access on you Azure subscription, follow these [steps](https://docs.microsoft.com/en-us/azure/cognitive-services/form-recognizer/quickstarts/python-train-extract#create-a-form-recognizer-resource) to setup your service.

## Train an Azure Form Recognizer Model ##
In order to train the model, collect 5 examples of the  forms you want to train with and store in Azure Blob storage.  Here are tips for setting up [training data](https://docs.microsoft.com/en-us/azure/cognitive-services/form-recognizer/build-training-data-set).

Follow the instructions to setup your Azure Cognitive Service and create Form Recognizer Resource: [Train a Form Recognizer Model](https://docs.microsoft.com/en-us/azure/cognitive-services/form-recognizer/quickstarts/python-train-extract#train-a-form-recognizer-model). [FormAnalyzer_Train.py](Form_Analyzer_Train.py) is based on the code used for training the model and you can use it for your model with the following changes:  

Replace the values in the sample code for:
1. **base_url**: The region your cognitive service is deployed to
2. **source**: The SAS URL for the blob storage with training documents (instructions in Step 3 - note the date/time expiration of the link and make suitable for your use case).   
3. **Ocp-Apim-Subscription-Key**: the key from your cognitive service

**NOTE**
The values to replace are all denoted with angle brackets <> - replace the brackets and the sample text. 
'Ocp-Apim-Subscription-Key': '<replace with your key>'
  should become
 'Ocp-Apim-Subscription-Key': '123456789123456789'

Once you run the code to train your model, you should get a response back that includes the ModelID for the model created, note this down for the next step.

## Analyze a form and extract items ##
The next step is to use the model to extract data from a new form.  The steps for getting top level entites are documented in the next section of the quick start <a href="https://docs.microsoft.com/en-us/azure/cognitive-services/form-recognizer/quickstarts/python-train-extract#extract-key-value-pairs-and-tables-from-forms" target="_blank">Extract key-value pairs and tables from forms</a>.

In addition to extracting the table, [FormAnalyzer_ExtractColumn](FormAnalyzer_ExtractColumn.py), iterates over the columns in the table to extract all the entries for one of the columns, giving you a list of those entries.

An example receipt is included [Tesco Example Receipt](Tesco_Example_Receipt.pdf) that can be processed and the values in the "Product" column are extracted.

Replace the values in the sample code for:
1. **base_url**: The region your cognitive service is deployed to
2. **file_path**: Your local path to Tesco_Example_Receipt.pdf (could be setup as a URL/SAS URL as well).
3. **model_id**: The model id from the trained model (see previous section).
4. **Ocp-Apim-Subscription-Key**: the key from your cognitive service
5. (Optional) you can change the **columnheader** to "Quantity" or "Total" for the example Tesco receipt to extract other entries.

Optionally, if you don't need/want to train and analyze with your own model, you can use the [Analyzed Tesco Example Reciept in JSON](Tesco_Example_Receipt.json) file, which is an output from analyzing the example receipt with a model.  [FormAnalyzer_ExtractColumn_FromJSON.py](FormAnalyzer_ExtractColumn_FromJSON.py) is code that iterates over the table results and get used to the model of the results from Azure Form Recognizer.


