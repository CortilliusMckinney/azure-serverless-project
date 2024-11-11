# Updated ProcessNewBlob/__init__.py
import logging
import azure.functions as func

def ProcessNewBlob(myblob: func.InputStream):     # Changed from 'main' to 'ProcessNewBlob'
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Size: {myblob.length} bytes")

__all__ = ['ProcessNewBlob']                      # Add this line