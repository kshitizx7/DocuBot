import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

# file_path = r"data\sample.pdf"

def extract_text_from_pdf(file_path: str) -> str: #file_path : str is the paramter and hint of type of parameter AND -> str is the hint of return type of function
    all_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            all_text += page.extract_text() or ""
    return all_text.strip() # this function remove the extra space from begining and ending form the all_text variable data
        




