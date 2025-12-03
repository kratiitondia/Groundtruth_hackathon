from typing import List, Dict, Any
import numpy as np
from .embeddings_openai import embed_texts
from .datastore import InMemoryFAISS

class RAG:
    def __init__(self, vectorstore: InMemoryFAISS):
        self.vs = vectorstore

    def retrieve(self, query: str, k: int = 4) -> List[Dict[str, Any]]:
        q_emb = embed_texts([query])
        if q_emb.size == 0:
            return []
        q_emb = np.array(q_emb, dtype="float32")
        D, I = self.vs.search(q_emb, k=k)
        dists = D[0]
        idxs = I[0]
        results = []
        for idx, dist in zip(idxs, dists):
            if idx == -1:
                continue
            meta = self.vs.get_metadata(int(idx))
            results.append({"metadata": meta, "score": float(dist)})
        return results
