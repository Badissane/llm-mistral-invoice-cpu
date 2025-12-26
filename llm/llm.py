from langchain.llms import CTransformers
import box
import yaml

from langchain_community.llms import Ollama


# Import config vars
with open('config.yml', 'r', encoding='utf8') as ymlfile:
    cfg = box.Box(yaml.safe_load(ymlfile))


llm = Ollama(
    model="mistral:instruct",  # or your Ollama model name
    temperature=0.1
'''
def setup_llm():
    llm = Ollama(model=cfg.MODEL_BIN_PATH,
                        model_type=cfg.MODEL_TYPE,
                        max_new_tokens=cfg.MAX_NEW_TOKENS,
                        temperature=cfg.TEMPERATURE
    )

    return llm
'''
