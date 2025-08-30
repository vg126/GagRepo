#!/usr/bin/env python3
"""
Legal Tools Document Retriever for Poe API Integration
Systematic document access using validated patterns from ChatGPT Agent mapping
"""
import requests
import os
from pathlib import Path

class LegalToolsRetriever:
    """Retrieves documents from ICC Legal Tools Database using systematic patterns"""
    
    BASE_URL = "https://www.legal-tools.org/doc"
    
    def __init__(self, download_dir="/tmp/legal_docs"):
        """Initialize with download directory"""
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(exist_ok=True)
    
    def get_document_pdf(self, document_id, filename=None):
        """
        Retrieve PDF document using document ID
        
        Args:
            document_id (str): Legal Tools document ID (e.g., 'i3dxot7g')
            filename (str, optional): Custom filename for saved PDF
            
        Returns:
            dict: Result with success status, file path, and metadata
        """
        if not filename:
            filename = f"legal_doc_{document_id}.pdf"
            
        pdf_url = f"{self.BASE_URL}/{document_id}/pdf"
        file_path = self.download_dir / filename
        
        try:
            response = requests.get(pdf_url, timeout=60, stream=True)
            response.raise_for_status()
            
            # Verify it's actually a PDF
            content_type = response.headers.get('content-type', '')
            if 'pdf' not in content_type.lower():
                return {
                    'success': False,
                    'error': f'Not a PDF file: {content_type}',
                    'document_id': document_id
                }
            
            # Save PDF
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            file_size = file_path.stat().st_size
            
            return {
                'success': True,
                'document_id': document_id,
                'file_path': str(file_path),
                'file_size': file_size,
                'url': pdf_url,
                'content_type': content_type
            }
            
        except requests.RequestException as e:
            return {
                'success': False,
                'error': str(e),
                'document_id': document_id,
                'url': pdf_url
            }
    
    def get_multiple_documents(self, document_ids):
        """
        Retrieve multiple documents in batch
        
        Args:
            document_ids (list): List of document IDs
            
        Returns:
            dict: Results with success/failure counts and details
        """
        results = []
        successful = 0
        failed = 0
        
        for doc_id in document_ids:
            result = self.get_document_pdf(doc_id)
            results.append(result)
            
            if result['success']:
                successful += 1
                print(f"✅ Retrieved {doc_id}: {result['file_size']} bytes")
            else:
                failed += 1
                print(f"❌ Failed {doc_id}: {result['error']}")
        
        return {
            'total': len(document_ids),
            'successful': successful,
            'failed': failed,
            'results': results
        }

# Validated document IDs from our mapping
VALIDATED_DOCUMENT_IDS = {
    'icc_situations': [
        'a076io',    # Afghanistan - ICC-02/17-204
        'bab8kl',    # Afghanistan - ICC-02/17-206  
        'v0r0673j',  # Libya - ICC-01/11-01/11-???
        'i3dxot7g',  # Libya Saif Suleiman - ICC-01/11-01/20-26-Red
    ],
    'otp_policies': [
        '4iaftrmo',  # Policy on Slavery Crimes
        '2hzyqht1',  # Policy on Complementarity (English)
    ],
    'asp_documents': [
        'dj3wqk66',  # ASP 23rd Session Resolution 2
    ],
    'basic_documents': [
        'n0k4lz',    # Regulations of the Court
        '7b9af9'     # Rome Statute
    ]
}

def main():
    """Test the retriever with validated document IDs"""
    retriever = LegalToolsRetriever("/storage/emulated/0/cc-android/ICC Keys Test/retrieved_docs")
    
    # Test with a few validated IDs
    test_ids = ['i3dxot7g', '4iaftrmo', 'dj3wqk66']
    
    print("🔍 Testing Legal Tools Document Retriever")
    print(f"Testing {len(test_ids)} validated document IDs\n")
    
    batch_result = retriever.get_multiple_documents(test_ids)
    
    print(f"\n📊 Batch Results:")
    print(f"Total: {batch_result['total']}")
    print(f"Successful: {batch_result['successful']}")
    print(f"Failed: {batch_result['failed']}")
    print(f"Success Rate: {batch_result['successful']/batch_result['total']*100:.1f}%")

if __name__ == "__main__":
    main()