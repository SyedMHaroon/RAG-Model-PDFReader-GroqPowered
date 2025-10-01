# PDF Question-Answering RAG Application

A Streamlit-based Retrieval-Augmented Generation (RAG) application that allows you to upload PDF documents and ask questions about their content using AI-powered natural language processing.

## 🚀 Features

- **PDF Upload**: Upload any PDF document through a user-friendly interface
- **Text Extraction**: Automatically extracts text from uploaded PDFs
- **Intelligent Chunking**: Splits documents into optimal chunks for better processing
- **Vector Search**: Uses FAISS vector database for efficient similarity search
- **AI-Powered Q&A**: Leverages Groq's Llama model for accurate question answering
- **Real-time Processing**: Get instant answers to your questions about the document

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **PDF Processing**: PyPDF2
- **Text Processing**: LangChain
- **Embeddings**: HuggingFace Sentence Transformers
- **Vector Database**: FAISS
- **LLM**: Groq (Llama-3.1-8b-instant)
- **Environment Management**: python-dotenv

## 📋 Prerequisites

Before running this application, make sure you have:

1. **Python 3.8+** installed on your system
2. **Groq API Key** - Sign up at [console.groq.com](https://console.groq.com) to get your free API key

## 🔧 Installation

1. **Clone or download** this repository to your local machine

2. **Navigate to the project directory**:
   ```bash
   cd path/to/your/project
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the project root directory
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

## 🚀 How to Run

1. **Start the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

3. **Upload a PDF** using the file uploader widget

4. **Ask questions** about the document content in the text input field

5. **Get AI-powered answers** based on the document content

## 📖 How It Works

### 1. Document Processing
- **PDF Upload**: Users upload PDF files through the Streamlit interface
- **Text Extraction**: PyPDF2 extracts all text content from the PDF pages
- **Text Chunking**: The extracted text is split into manageable chunks (1000 characters with 200 character overlap)

### 2. Vectorization
- **Embeddings**: Text chunks are converted to vector embeddings using HuggingFace's `sentence-transformers/all-MiniLM-L6-v2` model
- **Vector Store**: FAISS creates a searchable vector database from the embeddings

### 3. Question Answering
- **Query Processing**: User questions are processed and converted to embeddings
- **Similarity Search**: The system finds the most relevant document chunks using vector similarity
- **AI Response**: Groq's Llama model generates accurate answers based on the retrieved context

## ⚙️ Configuration

### Model Settings
The application uses the following default configurations:

- **LLM Model**: `llama-3.1-8b-instant` (Groq)
- **Embedding Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Chunk Size**: 1000 characters
- **Chunk Overlap**: 200 characters

### Customization
You can modify these settings in the `app.py` file:

```python
# Change the LLM model
llm = ChatGroq(
    model="llama-3-70b-8192",  # or other available models
    groq_api_key=os.environ.get("GROQ_API_KEY")
)

# Adjust text chunking parameters
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1500,      # Increase for longer chunks
    chunk_overlap=300,    # Increase for more overlap
    length_function=len
)
```

## 🔑 API Key Setup

### Getting a Groq API Key

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Navigate to the API Keys section
4. Generate a new API key
5. Copy the key and add it to your `.env` file

### Environment File Example
Create a `.env` file in your project root:
```
GROQ_API_KEY=your_actual_api_key_here
```

## 📁 Project Structure

```
Rag/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## 🐛 Troubleshooting

### Common Issues

1. **"Model not found" error**:
   - Ensure you're using a valid Groq model name
   - Check the [Groq documentation](https://console.groq.com/docs/models) for available models

2. **API key errors**:
   - Verify your `.env` file is in the project root
   - Ensure your Groq API key is valid and has sufficient credits

3. **PDF upload issues**:
   - Make sure the PDF is not password-protected
   - Check that the PDF contains extractable text (not just images)

4. **Memory issues with large PDFs**:
   - Reduce chunk size in the configuration
   - Consider processing smaller sections of the document

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your API keys secure and don't share them publicly
- The `.gitignore` file is configured to exclude sensitive files

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve this application.

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Review the [Groq documentation](https://console.groq.com/docs)
3. Open an issue in this repository

---

**Happy Document Questioning! 🎉**
