import logging
import azure.functions as func

def main(myblob: func.InputStream):     # Keep as 'main' for Azure Functions
    # Read the blob content
    blob_content = myblob.read()
    
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Size: {myblob.length} bytes")
    
    return blob_content

# Alias for testing purposes
ProcessNewBlob = main
__all__ = ['ProcessNewBlob']