from llama_index.core import Settings, StorageContext, load_index_from_storage
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Step 1: Load models
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(model="mistral", request_timeout=360.0)

# Step 2: Load stored index
storage_context = StorageContext.from_defaults(persist_dir="storage")
index = load_index_from_storage(storage_context)

# Step 3: Create Chat Engine
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

# Step 4: Chat loop
print("Ask questions about the Budget 2025 (type 'exit' to quit):")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting. Have a nice day!")
        break

    response = chat_engine.chat(user_input)
    print(f"\nAssistant: {response.response}")
