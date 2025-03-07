
# Le script generate_embeddings charge les fichiers texte de extracted_text/ et divise leur contenu en morceaux (chunks) de taille définie, par exemple 500 mots.
# Il utilise un modèle comme SentenceTransformer (ex. nomic-ai/nomic-embed-text-v1.5) pour convertir ces chunks en embeddings vectoriels, qui sont ensuite sauvegardés dans embeddings.npy.
# Un fichier chunk_mapping.txt est créé pour associer chaque chunk à son fichier d’origine, facilitant la récupération ultérieure des textes pertinents.

import os
import numpy as np
from sentence_transformers import SentenceTransformer

def split_text(text, chunk_size=500):
    words = text.split()
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

def generate_embeddings(text_dir, embedding_dir):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    if not os.path.exists(embedding_dir):
        os.makedirs(embedding_dir)
    
    all_chunks = []
    chunk_mapping = []  # Associe chaque chunk à son fichier d'origine
    
    for filename in os.listdir(text_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(text_dir, filename), 'r', encoding='utf-8') as f:
                text = f.read()
            chunks = split_text(text)
            all_chunks.extend(chunks)
            chunk_mapping.extend([(filename, chunk) for chunk in chunks])
    
    embeddings = model.encode(all_chunks, convert_to_tensor=False)
    np.save(os.path.join(embedding_dir, 'embeddings.npy'), embeddings)
    
    # Sauvegarder les métadonnées (mapping)
    with open(os.path.join(embedding_dir, 'chunk_mapping.txt'), 'w', encoding='utf-8') as f:
        for filename, chunk in chunk_mapping:
            f.write(f"{filename}|||{chunk}\n")
    
    print(f"Embeddings générés et sauvegardés : {len(embeddings)} chunks")

if __name__ == "__main__":
    generate_embeddings('../extracted_text', '../embeddings')