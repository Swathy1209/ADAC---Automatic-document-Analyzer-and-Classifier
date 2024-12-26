# AppianDocuSense

## Overview
AppianDocuSense is an intelligent document management platform that automates the classification and summarization of financial documents. The project leverages advanced natural language processing (NLP) models, a scalable backend, and an intuitive user interface to streamline document workflows. Designed for scalability and extensibility, it caters to modern document processing needs.

## Features
- **Automated Document Classification**: Categorizes documents (e.g., financial, identity, receipts) based on content keywords.
- **AI-Powered Summarization**: Summarizes lengthy text using the BART-large CNN NLP model, ensuring key details are retained.
- **Interactive UI**: Built with Streamlit for an easy-to-use and engaging interface, allowing users to upload and process multiple documents seamlessly.
- **Backend Storage**: Uses MongoDB to store and manage processed document data efficiently, supporting large-scale operations.
- **Scalability**: Designed for future extensions, including:
  - Invoice processing for classification and validation.
  - Fraud detection to identify discrepancies in financial records.

## Tech Stack
- **Frontend**: Streamlit for real-time interaction and visualization.
- **Backend**: MongoDB for robust and scalable database management.
- **NLP Model**: Facebook's BART-large CNN for accurate and efficient text summarization.
- **Document Processing**: PyPDF2 for extracting text from PDFs.
- **Programming Language**: Python for building a modular and extendable codebase.

## Installation and Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/appian-docusense.git
   cd appian-docusense
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. **Optional:** Configure MongoDB connection details in the `config.py` file.

## Usage
1. Open the Streamlit app in your browser.
2. Upload PDF documents for processing.
3. View the classification, summaries, and other extracted information.
4. Download results as a CSV file for further use.

## Future Enhancements
- **Invoice Processing**: Automate validation and categorization of invoices, making it easier to manage financial workflows.
- **Fraud Detection**: Integrate algorithms to detect anomalies and inconsistencies in financial records, enhancing trust and reliability.
- **Enhanced Classification**: Leverage more advanced machine learning models to improve accuracy and support additional document types.
- **Multi-Language Support**: Expand the platform's capabilities to process documents in multiple languages.
- **Customizable Summarization**: Allow users to define summarization parameters, such as length and focus areas.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- Facebook AI for the BART-large CNN model.
- Streamlit for the interactive UI framework.
- PyPDF2 for PDF text extraction.
