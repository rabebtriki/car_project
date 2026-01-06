from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain



groq_api_key = ""

def llm_groq():
    llm = ChatGroq(api_key=groq_api_key, model="llama-3.2-90b-vision-preview", temperature=0)

    prompt_template = ChatPromptTemplate.from_template(
        """
        You are an expert in cars.
        Act as if you are the car itself and possess all knowledge about cars. I will provide a context with information about a car, and you must respond as if you are the car, using only the given context. Do not generate any information beyond what is provided. If you do not know the answer, simply say, "I don't know," without making anything up.
        Do not include system messages or indicate that you are a chatbot—just provide the answer.
        <context>
        Context: {context}
        </context>
        
        <question>
        Question: {input}
        </question>
        """
        )

    # Create document chain with memory
    document_chain = create_stuff_documents_chain(llm, prompt_template)

    return document_chain