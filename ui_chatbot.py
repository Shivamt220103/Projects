import tkinter as tk
from tkinter import scrolledtext

from llama_index.core import Settings, StorageContext, load_index_from_storage
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# 🧠 Set up LLM and Embeddings
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(model="mistral", request_timeout=360.0)

# 📁 Load the Index
storage_context = StorageContext.from_defaults(persist_dir="storage")
index = load_index_from_storage(storage_context)
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=False)

# 🚀 Query handler
def ask_bot():
    user_input = input_text.get("1.0", tk.END).strip()
    if not user_input:
        return

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"\nMaster: {user_input}\n", "user")
    input_text.delete("1.0", tk.END)

    response = chat_engine.chat(user_input)
    answer = response.response

    chat_window.insert(tk.END, f"Margdarshak: {answer}\n", "bot")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)

# 🌌 Tkinter GUI setup (Dark Mode)
root = tk.Tk()
root.title("🧾 Budget 2025 Chatbot")
root.geometry("700x550")
root.configure(bg="#121212")

# 💬 Chat display area
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, bg="#1e1e1e", fg="white", font=("Consolas", 12))
chat_window.pack(padx=12, pady=10, fill=tk.BOTH, expand=True)

# 🎨 Chat text tags
chat_window.tag_config("user", foreground="cyan", font=("Consolas", 12, "bold"))
chat_window.tag_config("bot", foreground="light green", font=("Consolas", 12))

# ✍️ Input area
input_text = tk.Text(root, height=3, bg="#2c2c2c", fg="white", insertbackground="white", font=("Consolas", 12))
input_text.pack(padx=12, pady=(0, 8), fill=tk.X)
input_text.insert(tk.END, "Ask your question here...")

# 🟢 Send button
send_button = tk.Button(root, text="Ask 🔍", command=ask_bot, bg="#03DAC6", fg="black", font=("Arial", 12, "bold"), relief=tk.RAISED, bd=3)
send_button.pack(padx=12, pady=(0, 12))

# 🧵 Focus input box on click
def clear_placeholder(event):
    if input_text.get("1.0", tk.END).strip() == "Ask your question here...":
        input_text.delete("1.0", tk.END)

input_text.bind("<FocusIn>", clear_placeholder)

# 🖱️ Pressing Enter also submits the question
input_text.bind("<Return>", lambda event: (ask_bot(), "break"))


# 🎬 Start GUI
root.mainloop()
