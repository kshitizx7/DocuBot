from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_text(text , chunk_size = 800, chunk_overlap = 100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size, # here we set maximum number of characters in a chunk
        chunk_overlap = chunk_overlap, # chunk1-> 0 to 800 chunk2 -> 700 to 1500 ,, chunk_overlap = 100
        separators=["\n\n","\n","."," ",""] # this is a priority list where splitter tries to break the text
    )
    return splitter.split_text(text) # Above be set rules for splitter , Now this function is used to split the text
