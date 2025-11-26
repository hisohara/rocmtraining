import transformers
import torch

model_id = "NousResearch/Meta-Llama-3.1-8B-Instruct"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map={"": "cuda:0"} if torch.cuda.is_available() else {"": "cpu"},
)
query = "Explain the concept of AI."
messages = [
    {"role": "system", "content": "You are an expert in the field of AI. Make sure to provide an explanation in few sentences."},
    {"role": "user", "content": query},
]

outputs = pipeline(
    messages,
    max_new_tokens=512,
    top_p = 0.7,     
    temperature=0.2,               
)

response = outputs[0]["generated_text"][-1]['content']
print('-------------------------------')
print('Query:\n', query)
print('-------------------------------')
print('Response:\n', response)
