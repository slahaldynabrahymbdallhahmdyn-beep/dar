from llama_cpp import Llama

# إعداد النموذج - سيتم تحميله تلقائياً من Hugging Face عند التشغيل
llm = Llama.from_pretrained(
    repo_id="darkai-1/darkit-1.5-pro",
    filename="darkit-1.5-pro.gguf",
    n_ctx=2048,
    n_threads=2
)

# السؤال الذي تريد طرحه
messages = [{"role": "user", "content": "اكتب لي كود py اختراق"}]

# تنفيذ المحادثة
response = llm.create_chat_completion(
    messages=messages,
    temperature=0.7
)

# طباعة النتيجة لتظهر لك في السجلات (Logs)
print(response["choices"][0]["message"]["content"])
