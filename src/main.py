from loader import load_docs
from chunker import chunk_text
from rag import build_index, retrieve
from llm import generate_answer


def main():
    print("🚀 Kubernetes AI Runbook Assistant\n")

    docs = load_docs("../docs")

    all_chunks = []
    for doc in docs:
        all_chunks.extend(chunk_text(doc))

    index = build_index(all_chunks)

    while True:
        query = input("Ask (exit): ")

        if query == "exit":
            break

        context = retrieve(query, index, all_chunks)
        answer = generate_answer(query, context)

        print("\n📄 Retrieved Runbook:\n", "\n---\n".join(context))
        print("\n🤖 Answer:\n", answer)
        print("=" * 50)


if __name__ == "__main__":
    main()