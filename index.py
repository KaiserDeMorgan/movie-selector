import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
)

questionOne = input("What is your favourite movie, and why?: ")
questionTwo= input("What is your genre?: ")
questionThree = input("Do you want something serious, or light hearted?: ")

questions = [questionOne, questionTwo, questionThree]

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3.2:novita",
    messages=[
        {
            "role": "user",
            "content": f"Recommend me a movie based off of this content: {questions}"
        }
    ],
)

print(completion.choices[0].message.content)