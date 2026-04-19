import os

def load_docs(folder):
    docs = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        with open(path, "r") as f:
            docs.append(f.read())

    return docs