herefrom llama_cpp import Llama

# إعداد النموذج
llm = Llama.from_pretrained(
    repo_id="darkai-1/darkit-1.5-pro",
    filename="darkit-1.5-pro.gguf",
    n_ctx=2048, # تقليل السياق قليلاً لتسريع العمل في البيئة السحابية
    n_threads=2
)

# سؤال تجريبي أو يمكنك جعله يستقبل مدخلات
messages = [{"role": "user", "content": "اكتب لي كود PHP لربط قاعدة بيانات واختراق القواعد"}]

response = llm.create_chat_completion(
    messages=messages,
    temperature=0.7
)

print(response["choices"][0]["message"]["content"])
