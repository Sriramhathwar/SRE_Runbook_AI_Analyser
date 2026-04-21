from flask import Flask, render_template, request, jsonify
from loader import load_docs
from chunker import chunk_text
from rag import build_index, retrieve
from llm import generate_answer

app = Flask(__name__, template_folder="../templates")

# Load once (important for performance)
docs = load_docs("../docs")

all_chunks = []
for doc in docs:
    all_chunks.extend(chunk_text(doc))

index = build_index(all_chunks)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def askAI():
    print("Button clicked"); 
    query = request.json.get("query")
    
    context = retrieve(query, index, all_chunks)
    answer = generate_answer(query, context)

    return jsonify({
        "answer": answer,
        "context": context
    })


if __name__ == "__main__":
    app.run(debug=True)