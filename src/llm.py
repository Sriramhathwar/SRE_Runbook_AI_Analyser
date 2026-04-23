from llama_cpp import Llama

llm = Llama(
    model_path="../models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_ctx=1024,
    n_threads=6,
    verbose=False
)

def generate_answer(query, context_chunks, history):
    context = "\n".join(context_chunks)
    if history is None:
        history = []
    history_text = ""
    for msg in history[-4:]:  # last 4 messages only (important!)
        if msg["role"] == "user":
            history_text += f"User: {msg['content']}\n"
        else:
            history_text += f"Assistant: {msg['content']}\n"
    
    prompt = f"""
[INST]
You are a Kubernetes SRE assistant.

Conversation:
{history_text}

Runbook:
{context}

Current Question:
{query}

Give clear step-by-step answer.
[/INST]
"""

    output = llm(
        prompt,
        max_tokens=300,
        temperature=0.2,
        stop=["</s>"]
    )

    return output["choices"][0]["text"].strip()