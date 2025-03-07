# RAG Fitness

**Description:** A Retrieval-Augmented Generation system in Python to answer fitness-related questions from local scientific articles, leveraging SentenceTransformers and the Gemini API.

---

## Overview

**Objective:** Build a Retrieval-Augmented Generation (RAG) system to provide answers about fitness based on locally stored scientific articles, using vector embeddings and the Gemini API.  
**Date:** March 2025  

---

## Step 1 - Data Collection

**Description:** Gathering scientific articles on fitness.  

1. **Data Source:**  
   - Scientific articles (PDFs) on topics like strength training, cardio, and nutrition are sourced from databases like PubMed or specialized journals.  
   - Example: "Incidence of and risk factors for small vulnerable" or studies on strength training.  

2. **Organization:**  
   - Manual or automated download of relevant PDFs.  
   - Stored in a local directory: `C:\Users\sarto\OneDrive\Bureau\RAG\data`.  

3. **Outcome:**  
   - A collection of raw PDF files ready for processing (e.g., `article1.pdf`, `article2.pdf`).  
   - Initial dataset for the RAG system.  

---

## Step 2 - Text Extraction (`extract_text.py`)

**Description:** Converting PDFs into usable plain text.  

1. **PDF Loading:**  
   - Files from `data/` are read using `pdfplumber` to extract content page by page.  
   - Example: A PDF on strength training becomes a text string.  

2. **Text Cleaning:**  
   - Removal of excess spaces and unwanted characters for clean text.  
   - Result: "Strength training improves bone density."  

3. **Saving:**  
   - Each text is saved as `.txt` in `extracted_text/` (e.g., `article1.txt`).  
   - Prepares data for embedding generation.  

---

## Step 3 - Embedding Generation (`generate_embeddings.py`)

**Description:** Transforming texts into semantic vectors.  

1. **Chunking:**  
   - `.txt` files are split into 500-word chunks for detailed analysis.  
   - Example: A long text becomes chunks like "Strength training..." and "Protein aids...".  

2. **Embedding Creation:**  
   - `SentenceTransformer` (`nomic-ai/nomic-embed-text-v1.5`) generates 768-dimensional vectors.  
   - Saved in `embeddings.npy` and mapped in `chunk_mapping.txt` (e.g., `article1.txt|||text`).  

3. **Outcome:**  
   - Chunks are represented by vectors, close for similar concepts (e.g., strength and muscle).  
   - Stored in `C:\Users\sarto\OneDrive\Bureau\RAG\embeddings`.  

---

## Step 4 - RAG System (`rag_main.ipynb`)

**Description:** Retrieving and generating answers.  

1. **Data Loading:**  
   - Embeddings and chunks are loaded from `embeddings/`.  
   - Example: Vectors and texts ready for comparison.  

2. **Semantic Retrieval:**  
   - A question (e.g., "What are the benefits of strength training?") is encoded into a vector.  
   - `cosine_similarity` selects the top 3 closest chunks (e.g., strength-related texts).  

3. **Answer Generation:**  
   - Context is sent to the Gemini API (`gemini-2.0-flash-exp`) using a Google API key.  
   - Response: "Strength training strengthens muscles and improves bone density."  

---

## Conclusion

**Final Structure:**  
- `data/`: Raw collected PDFs.  
- `extracted_text/`: Extracted texts.  
- `embeddings/`: Embeddings and mapping.  

**Tools:** Python, `pdfplumber`, `SentenceTransformers`, `openai` for Gemini.  
**Next Steps:** Integration with Google Cloud Storage, embedding optimization.  
