from llama_cpp import Llama

llm = Llama(
    model_path="../models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_ctx=1024,
    n_threads=6,
    verbose=False
)

def generate_answer(query, context_chunks):
    context = "\n".join(context_chunks)

    prompt = f"""
[INST]
You are a Kubernetes SRE assistant.

STRICT RULES:
- Answer ONLY from runbooks
- Give step-by-step solution
- Do NOT hallucinate

Runbook:
{context}

Question:
{query}
[/INST]
"""

    output = llm(
        prompt,
        max_tokens=150,
        temperature=0.2,
        stop=["</s>"]
    )

    return output["choices"][0]["text"].strip()