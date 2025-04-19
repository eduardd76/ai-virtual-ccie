from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4", temperature=0)

cli_prompt = PromptTemplate(
    input_variables=["problem"],
    template="""You are a network automation assistant. Based on the problem below, generate Cisco, Arista, and Juniper CLI configurations.

Problem:
{problem}

Configuration:"""
)

cli_chain = LLMChain(llm=llm, prompt=cli_prompt)
problem_description = "OSPF authentication mismatch on interface. MD5 key is not aligned."
cli_output = cli_chain.run(problem=problem_description)
print(cli_output)