import json

def schema_extract(file_path):
    """ This function takes in the file_path of a JSON file,
        and extracts the attributes of the message keyword to
        create a schema with the following output

        {
            "key_one":{
                "type":"data type",
                "tag":"",
                "description":"",
                "required":false
            }

            "key_two":{
                "type":"data type",
                "tag":"",
                "description":"",
                "required":false
            }
        }

    """
    #load the input file in json 
    while True:
        try: 
            with open(file_path) as f:
                object = json.load(f)
            break
        except:
            print("invalid file path or file name")
            print ("try again")
            file_path = input("Enter the file path that contains the JSON file: ")

    #Create a dictionary of datatypes that helps to map input data
    #to expected type in the schema
    dtypes = {
        "<class 'dict'>":"array",
        "<class 'list'>":"enum",
        "<class 'str'>":"string",
        "<class 'int'>":"integer",
        "<class 'float'>":"float",
        "<class 'bool'>":"boolean",
    }

    #Create a property for each attribute found in message
    property ={
        "type":None,
        "tag":"",
        "description":"",
        "required":False
    }

    schema = {}
    #Check if message key is in the dataset
    if not "message" in object.keys():
        raise KeyError("Key: 'message' does not exist in the dataset")
    for x in object["message"].keys():
        try:
            #check if datatype is valid else it assigns string by default
            property["type"] = dtypes[str(type(object["message"][x]))]
        except:
            property["type"] = "string"
        schema[x] = property.copy()
    
    return schema
    

if __name__ == "__main__":
    file_path = input("Enter the file path that contains the JSON file: ")
    
    #generate schema
    schema = schema_extract(file_path)
    
    schema_name = file_path.split("/")[-1].split(".")[0]
    
    #Save the Schema in JSON format
    with open(f"./schema/schema_{schema_name}.json", "w") as f:
        json.dump(schema, f, indent=4)
    print("Schema has been Successfully created")