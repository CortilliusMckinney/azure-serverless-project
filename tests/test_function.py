import azure.functions as func
import logging
from ProcessNewBlob import ProcessNewBlob
from unittest.mock import patch

def test_blob_trigger_basic_execution():
    """Test basic execution of the blob trigger function"""
    test_blob = func.InputStream(
        data=b"sample data",
        name="test_blob.txt"
    )
    ProcessNewBlob(test_blob)

def test_blob_trigger_logging():
    """Test that the function logs correct blob information"""
    test_blob = func.InputStream(
        data=b"sample data for testing",
        name="test_blob.txt"
    )
    
    with patch('logging.info') as mock_logging:
        ProcessNewBlob(test_blob)
        expected_log = (
            f"Python blob trigger function processed blob \n"
            f"Name: {test_blob.name}\n"
            f"Size: {test_blob.length} bytes"
        )
        mock_logging.assert_called_with(expected_log)