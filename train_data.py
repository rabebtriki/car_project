import PyPDF2
from langchain_huggingface import HuggingFaceEmbeddings   
from langchain.vectorstores import Chroma
import os

embeddings = HuggingFaceEmbeddings()

def read_and_textify(file_path):
    text_list = []
    sources_list = []

    for file in file_path:
        with open(file, 'rb') as pdf_file:  
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for i in range(len(pdf_reader.pages)):
                page_obj = pdf_reader.pages[i]
                text = page_obj.extract_text()
                text_list.append(text)
                sources_list.append(file + "_page_" + str(i))
    return text_list, sources_list  

def vector_store(directory_pdf, persist_directory):

    files = [os.path.join(directory_pdf, x) for x in os.listdir(directory_pdf) if x.endswith(".pdf")]
    doc, source = read_and_textify(files) 

    print("hedi text_list:", doc)
    print("hedi source_list:", source)

    vector_db = Chroma.from_texts(doc,
                                embeddings,
                                metadatas=[{"source": s} for s in source],
                                persist_directory=persist_directory) 
    
    vector_db.persist()
    print("saved with success")
    return vector_db


persist_directory = "./projet_2/BD_VECTORS/"
directory_pdf = "./projet_2/filess/"

os.makedirs(persist_directory, exist_ok=True)
vector_store(directory_pdf, persist_directory)