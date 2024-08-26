import os
from openai import AzureOpenAI

# client = AzureOpenAI(
#   azure_endpoint = os.getenv(""), 
#   api_key=os.getenv(""),  
#   api_version="2024-02-01"
# )

client = AzureOpenAI(
  azure_endpoint = "", 
  api_key="",  
  api_version="2024-02-01"
)

def gpt_response(user_input):
    response = client.chat.completions.create(
        model="your bot name", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content
