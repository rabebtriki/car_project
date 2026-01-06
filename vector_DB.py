from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import create_retrieval_chain
from llm_execution import llm_groq
import os


embeddings = HuggingFaceEmbeddings()
persist_directory = "./projet_2/BD_VECTORS/"  

def vector_store(persist_directory):
    if os.path.exists(os.path.join(persist_directory, "chroma.sqlite3")):
        print("Loading existing vector store")

        result = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

        print("mhamed you are done")
        return result
    

def get_car(name_car):
    car_data = persist_directory + name_car
    print("this is data_car mhamed: ", car_data)
    vector_db = vector_store(car_data)
    print("this is done mhamed")
    document_chain = llm_groq()
    print("this done 2")
    retriever = vector_db.as_retriever()
    print("this is done 3")
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    print("this is the output of retravail mhamed :", retrieval_chain)
    return retrieval_chain