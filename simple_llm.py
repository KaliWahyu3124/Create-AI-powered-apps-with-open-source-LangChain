import os
from langchain_openai import ChatOpenAI

# Mengatur environment variable "OPENAI_API_KEY" dengan OpenAI API key milikmu. ini diperlukan untuk proses autentikasi ke OpenAI API.
os.environ["OPENAI_API_KEY"] = "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"

# Mendefinisikan jenis model 
gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo" )

text = "Berikan fakta menarik tentang kentang!"
print(gpt3.invoke(text).content)