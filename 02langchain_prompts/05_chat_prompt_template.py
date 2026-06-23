from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ("system", "From the point of view of {character}, answer the query."),
    ("user", "{query}")
])

prompt = chat_template.invoke({"character": "Madam Pomfrey", "query": "Were the children safe when the troll entered the castle?"})

print(prompt)
