import logging
import azure.functions as func

def ProcessNewBlob(myblob: func.InputStream):
    # Read the blob content
    blob_content = myblob.read()
    
    logging.info(f"Python blob trigger function processed blob \n"
                f"Name: {myblob.name}\n"
                f"Size: {myblob.length} bytes")
    
    return blob_content  # Optional: return the content if needed