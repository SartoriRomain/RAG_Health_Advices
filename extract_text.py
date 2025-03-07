# Le script extract_text lit des fichiers PDF stockés dans un dossier local, comme data/, en utilisant pdfplumber pour extraire leur contenu texte brut.
# Il nettoie le texte en supprimant les espaces multiples et les caractères indésirables, puis sauvegarde chaque résultat dans un fichier .txt dans le dossier extracted_text/.
# Cette étape prépare les données textuelles pour les étapes suivantes en transformant les PDFs en un format lisible et structuré.

# Extract the PDF and prepare the processing
import pdfplumber
import os
import re

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() or ''  # Ajoute '' si None
    return text

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remplace les espaces multiples
    text = text.strip()  # Supprime les espaces en début/fin
    return text

def process_pdfs(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, filename)
            text = extract_text_from_pdf(pdf_path)
            cleaned_text = clean_text(text)
            output_path = os.path.join(output_dir, f"{filename[:-4]}.txt")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_text)
            print(f"Texte extrait et sauvegardé : {output_path}")

if __name__ == "__main__":
    process_pdfs('../data', '../extracted_text')
    