import streamlit as st
import pandas as pd
import PyPDF2
from transformers import pipeline
import os

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to extract text from uploaded PDFs
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() if page.extract_text() else ""
    return text

# Function to classify document types based on keywords
def classify_document(text):
    if any(keyword in text.lower() for keyword in ["income", "salary", "paystub"]):
        return "Supporting Financial Document"
    elif any(keyword in text.lower() for keyword in ["application", "account", "credit"]):
        return "Application Document"
    elif any(keyword in text.lower() for keyword in ["passport", "license", "id"]):
        return "Identity Document"
    elif any(keyword in text.lower() for keyword in ["receipt", "invoice"]):
        return "Receipt"
    else:
        return "Unknown Document Type"

# Function to summarize lengthy text
def summarize_text(text):
    if len(text.split()) > 150:  # Summarize only long text
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    return "No summarization required for short text."

# Main Streamlit Application
def main():
    st.title("📄 Automated Document Classification and Summarization")
    st.write("Upload financial documents to classify, summarize, and organize them.")

    uploaded_files = st.file_uploader("Upload PDF Documents", accept_multiple_files=True, type=["pdf"])

    if uploaded_files:
        # Initialize results container
        document_data = []

        # Process each uploaded PDF
        for uploaded_file in uploaded_files:
            st.write(f"Processing: **{uploaded_file.name}**")
            text = extract_text_from_pdf(uploaded_file)

            if not text:
                st.warning(f"Could not extract text from {uploaded_file.name}")
                continue

            # Classification and Summarization
            document_type = classify_document(text)
            summary = summarize_text(text)

            # Extract dummy person name (simulate extraction logic)
            person_name = "Unknown Person"
            for line in text.split("\n"):
                if "name:" in line.lower():
                    person_name = line.split(":")[1].strip()
                    break

            # Append data for results display
            document_data.append({
                "Document Name": uploaded_file.name,
                "Person": person_name,
                "Document Type": document_type,
                "Summary": summary
            })

        # Display results in DataFrame
        st.subheader("Processed Documents")
        df = pd.DataFrame(document_data)
        st.dataframe(df)

        # Download results as CSV
        st.subheader("Download Results")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Results as CSV", data=csv, file_name="classified_documents.csv", mime="text/csv")

if __name__ == "__main__":
    main()
