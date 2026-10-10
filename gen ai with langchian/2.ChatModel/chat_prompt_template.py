from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'you are a help ful {domain} assistant.'),
    ('human', 'explain {topic} to me in simple terms.')
])

prompts = chat_template.invoke({'domain': 'ai', 'topic': 'ollama'})
print(prompts)