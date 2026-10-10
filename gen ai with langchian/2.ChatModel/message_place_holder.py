from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system','you are a expert {domain} assistent'),
     MessagesPlaceholder(variable_name = 'chat_history'),
    ('Human', 'tell me {topic} in simple term')
])

chat_history =[]
with open(chat_history.txt) as f:
   chat_history.extend( f.readline())
print(chat_history)

prompt = chat_template.invoke({'domain': 'ai', 'topic':'ollama'})
print(prompt)