from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ["HF_HOME"] = "E:/huggingface_cache"  # Replace

llm = HuggingFacePipeline.from_model_id(
    model_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = "text generation",
    pipeline_kwargs = {
        "temperature": 1.2,
        "max_new_tokens": 512
    }
    )

model = ChatHuggingFace(llm=llm)
prompt = input("you:")
result = model.invoke(prompt)
