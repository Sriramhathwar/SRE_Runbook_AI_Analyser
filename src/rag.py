import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(chunks):
    embeddings = model.encode(chunks)
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    return index


def retrieve(query, index, chunks, k=2):
    q_emb = model.encode([query])
    distances, indices = index.search(np.array(q_emb), k)

    return [chunks[i] for i in indices[0]]