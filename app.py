import streamlit as st
import PyPDF2
import google.generativeai as genai

def retrieve_text_from_pdf(pdf):
    with open(pdf, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def main():
    pdf_path = "content.pdf"
    model_name = "gemini-1.5-pro-latest"
    
    # Read API key from a text file
    with open("keys/api key.txt", "r") as file:
        key = file.read()
        
    # Configure generative AI with API key
    genai.configure(api_key=key)
    
    # Streamlit interface
    st.title("RAG System on 'Leave No Context Behind' Paper")
    
    # Add balloon animation
    st.balloons()
    
    # Add snow animation
    st.snow()
    
    question = st.text_input("Enter your question:")
    
    if st.button("Generate"):
        if question:
            # Retrieve text from PDF
            text = retrieve_text_from_pdf(pdf_path)
            context = text + "\n\n" + question
            
            # Generate answer using generative model
            ai = genai.GenerativeModel(model_name=model_name)
            response = ai.generate_content(context)  
            
            # Display question and answer
            st.subheader("Question:")
            st.write(question)
            st.subheader("Answer:")
            st.write(response.text)
        else:
            st.warning("Please enter your question.")

if __name__ == "__main__":
    main()
