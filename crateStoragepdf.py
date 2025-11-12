from llama_index.core import VectorStoreIndex, Settings, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

# Step 1: Set LLM and Embeddings
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(model="mistral", request_timeout=360.0)




# Step 2: Load PDF and Create Index
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

# Step 3: Persist Index
index.storage_context.persist("storage")
