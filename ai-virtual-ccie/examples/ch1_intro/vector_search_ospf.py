from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document

docs = [
    Document(page_content="Issue: OSPF Authentication Mismatch. Solution: Ensure both routers have the same MD5 key."),
    Document(page_content="Issue: MTU Mismatch in OSPF. Solution: Adjust MTU or use 'ip ospf mtu-ignore'.")
]

embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embedding)

query = "MD5 authentication failed in OSPF"
results = vectorstore.similarity_search(query, k=1)
print(results[0].page_content)