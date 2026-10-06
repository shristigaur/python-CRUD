# import os
# from dotenv import load_dotenv
# load_dotenv()

# from openai import OpenAI

# client = OpenAI(
#     base_url="https://router.huggingface.co/v1",
#     api_key=os.environ["HF_TOKEN"],
# )

# completion = client.chat.completions.create(
#     model="meta-llama/Llama-3.1-8B-Instruct:novita",
#     messages=[
#         {
#             "role": "user",
#             "content": "What is the capital of France?"
#         }
#     ],
# )

# anser=completion.choices[0].message
# print(anser)

import os
import gradio as gr
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client=OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"]
)
def chatbot(message):
    completion=client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct:novita",
        messages=[
            {
            "role":"user",
            "content": message
            }
        ],
    )
    ans=completion.choices[0].message.content
    return ans

app = gr.Interface( fn=chatbot, 
    inputs=gr.Textbox( 
        placeholder="Ask me anything...", label="Your Message" ), 
        outputs=gr.Textbox( label="AI Response" ), 
        title="🤖 My AI Chatbot", 
        description="Ask a question and get an AI response." )
app.launch() # Start the application app.launch()