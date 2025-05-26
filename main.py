from llama_stack.distribution.library_client import LlamaStackAsLibraryClient

def main():
    print("Hello from llama-stack-rag-content!")

    client = LlamaStackAsLibraryClient(
        "./run.yaml",
        # provider_data is optional, but if you need to pass in any provider specific data, you can do so here.
        provider_data={},
    )
    client.initialize()

    # Register a vector db
    vector_db_id = "my_documents"
    response = client.vector_dbs.register(
        vector_db_id=vector_db_id,
        embedding_model="all-MiniLM-L6-v2",
        embedding_dimension=384,
        provider_id="faiss",
    )

    # You can insert a pre-chunked document directly into the vector db
    chunks = [
        {
            "content": "Your document text here",
            "mime_type": "text/plain",
            "metadata": {
                "document_id": "doc1",
                "author": "Jane Doe",
            },
        },
    ]
    client.vector_io.insert(vector_db_id=vector_db_id, chunks=chunks)

if __name__ == "__main__":
    main()
