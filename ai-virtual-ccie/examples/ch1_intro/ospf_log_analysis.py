from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = ChatOpenAI(model_name="gpt-4", temperature=0)

prompt = PromptTemplate(
    input_variables=["log"],
    template="""You are a senior network engineer. Analyze the following OSPF log and explain the issue.

Log:
{log}

Response:"""
)

log_chain = LLMChain(llm=llm, prompt=prompt)

ospf_log = "%OSPF-4-ERRRCV: Received invalid packet: MD5 authentication failed from neighbor 10.0.0.2 on GigabitEthernet0/1"
response = log_chain.run(log=ospf_log)
print(response)