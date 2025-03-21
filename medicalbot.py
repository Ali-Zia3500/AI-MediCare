from langchain_chroma import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
import os 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
import streamlit as st



chroma_db_path = "D:\Chat_with_Pdf\content\chroma_db"

embedding = GoogleGenerativeAIEmbeddings(
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    model="models/embedding-001"
)

db = Chroma(persist_directory=chroma_db_path,embedding_function=embedding)

def get_medical_chain():
    prompt_template = """Answer the question as accurately and sensitively as possible based on the provided context.
    Provide clear, concise information while being considerate of the user's situation. 
    If the information is available, provide relevant medical advice, treatment, and medications. 
    If the situation is sensitive (e.g., serious health concerns), recommend contacting a healthcare professional and avoid giving incomplete or potentially harmful advice. 
    Additionally, ask for relevant information such as age, type of disease, and symptoms to tailor the response better.\n\n
    Context:\n {context}\n
    Question: {question}\n
    User Information:\n Age: {age}, Type of Disease: {disease_type}, Symptoms: {symptoms}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro",temperature=0.3)
    prompt = PromptTemplate(template=prompt_template,input_variables=["context", "question", "age", "disease_type", "symptoms"])
    chain = load_qa_chain(model,chain_type="stuff",prompt=prompt)
    return chain


#APP
def medical_chatbot_app():
    st.title("Medical_Asisstant_APP")


    query = st.text_input("Enter you Question")
    age = st.number_input("Enter Your AGe ",min_value=0)
    disease_type = st.text_input("Enter Your Type of Disease:","")
    symptoms = st.text_area("Describe your Symptoms:")


    if st.button("Get Medical Advice"):
        if query:
            results = db.similarity_search(disease_type,k=3)
                # Prepare input documents from the results
            input_documents = [{"page_content": result.page_content} for result in results]
            chain = get_medical_chain()

                # Generate response using the chain
            response = chain({"input_documents": input_documents, 
                                  "question": query, 
                                  "age": age, 
                                  "disease_type": disease_type, 
                                  "symptoms": symptoms})
            st.write("Advice:")
            st.write(response["output_text"])
        else:
            st.warning("The information for this disease is not available in the database. Please consult a healthcare professional.")
    else:
        st.error("Please Enter a Your Question ")


if __name__ == "__main__":
    medical_chatbot_app()