from typing import List, Dict, Any
from .embeddings_openai import embed_texts

def seed(vs) -> int:
    docs = [
        {"id": "doc1", "title": "Return Policy", "text": "Our return policy allows returns within 30 days with receipt."},
        {"id": "doc2", "title": "Hot Beverages", "text": "Hot beverages like Hot Cocoa are served from 7am to 10pm."},
        {"id": "doc3", "title": "Loyalty", "text": "We support gift-card redemption and loyalty points at POS."},
        {"id": "doc4", "title": "Delivery Help", "text": "If an order is marked delivered, contact support within 48 hours for missing items."}
    ]
    texts = [d["text"] for d in docs]
    embs = embed_texts(texts)
    metadatas = [{"id": d["id"], "text": d["text"], "title": d["title"]} for d in docs]
    vs.add(embs, metadatas)
    return len(docs)
