from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential(logging_enable=True)
print(credential)
token = credential.get_token("https://management.azure.com/.default")
print(token)