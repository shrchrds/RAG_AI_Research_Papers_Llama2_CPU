from langchain import PromptTemplate
from langchain import LLMChain
from langchain.llms import CTransformers
from src.helper import *

B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

instruction = "Provide a concise answer in simple English under 500 words. Avoid repetition of words when answer is less than 500 words: \n\n {question}"

SYSTEM_PROMPT = B_SYS + CUSTOM_SYSTEM_PROMPT + E_SYS
template = B_INST + SYSTEM_PROMPT + instruction + E_INST

prompt = PromptTemplate(template=template, input_variables=['question'])

llm = CTransformers(model='model/llama-2-7b-chat.ggmlv3.q4_0.bin',
                    model_type='llama',
                    config={'max_new_tokens': 512,
                            'temperature': 0.01}
                   )
LLM_Chain=LLMChain(prompt=prompt, llm=llm)

print(LLM_Chain.run("Explain transformers architecture in brief"))