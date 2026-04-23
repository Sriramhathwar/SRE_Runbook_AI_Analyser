## 🏗️ Architecture Diagram


                 ┌──────────────────────┐
                 │        User          │
                 │   (Browser UI)       │
                 └─────────┬────────────┘
                           │ HTTP Request
                           ▼
                 ┌──────────────────────┐
                 │     Flask Backend    │
                 │   (/ask API Route)   │
                 └─────────┬────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
   Memory Store      RAG Engine        Prompt Builder
        │                  │
        ▼                  ▼
   FAISS Vector DB   Embedding Model
        │
        ▼
   Mistral LLM (GGUF)
        │
        ▼
     Response to UI