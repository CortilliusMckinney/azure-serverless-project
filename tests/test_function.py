import logging
import unittest.mock as mock
from ProcessNewBlob import ProcessNewBlob

def test_blob_trigger_basic_execution():
    """Test basic execution of the blob trigger function"""
    # Create mock blob input
    test_blob = mock.Mock()
    test_blob.name = "test_blob.txt"
    test_blob.length = 11
    test_blob.read.return_value = b"sample data"

    # Execute function
    ProcessNewBlob(test_blob)
    
    # Verify blob was processed (basic execution check)
    test_blob.read.assert_called_once()

def test_blob_trigger_logging():
    """Test that the function logs correct blob information"""
    # Create mock blob input
    test_blob = mock.Mock()
    test_blob.name = "test_blob.txt"
    test_blob.length = 20
    test_blob.read.return_value = b"sample data for testing"

    # Capture logs
    with mock.patch('logging.info') as mock_log:
        ProcessNewBlob(test_blob)
        
        # Verify logging occurred with correct information
        mock_log.assert_called_with(
            "Python blob trigger function processed blob \n"
            f"Name: {test_blob.name}\n"
            f"Size: {test_blob.length} bytes"
        )