from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from secret import api_key
import os

os.environ['OPENAI_API_KEY'] = api_key

llm=OpenAI(temperature=0.9)
prompt=PromptTemplate(
    input_variables=["query", "role"],
    template="Can you help me with the {query} as a {role}, that I am assigning to you.",
)
chain= LLMChain(llm=llm,prompt=prompt)
q=input("Enter the query: ")
r=input("Enter the role: ")
d = chain.invoke({'query':{q}, 'role':{r}})
print(d['text'])