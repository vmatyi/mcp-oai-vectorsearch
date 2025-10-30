#!/usr/bin/env python3
"""Quick test script to verify vector store search returns correct file IDs"""

import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Vector store ID from environment
VECTOR_STORE_ID = os.environ.get("VECTOR_STORE_ID", "vs_68973dcf4a24819192f1bf39cb97e382")

print(f"Testing vector store search with ID: {VECTOR_STORE_ID}")
print("=" * 60)

try:
    # Search using the beta API
    response = client.beta.vector_stores.search(
        vector_store_id=VECTOR_STORE_ID,
        query="set deadline for tasks",
        max_num_results=3
    )
    
    print(f"Search query: 'set deadline for tasks'")
    print(f"Results found: {len(response.data)}\n")
    
    # Display results
    for i, item in enumerate(response.data, 1):
        file_id = getattr(item, 'file_id', 'NO FILE_ID')
        filename = getattr(item, 'filename', 'NO FILENAME')
        score = getattr(item, 'score', 'NO SCORE')
        
        print(f"Result {i}:")
        print(f"  File ID: {file_id}")
        print(f"  Filename: {filename}")
        print(f"  Score: {score}")
        
        # Check file ID format
        if file_id.startswith('file-'):
            print(f"  ✓ File ID format is CORRECT (file-xxx)")
        else:
            print(f"  ✗ File ID format is WRONG (expected file-xxx)")
        print()
        
except Exception as e:
    print(f"Error during search: {e}")
    import traceback
    traceback.print_exc()
