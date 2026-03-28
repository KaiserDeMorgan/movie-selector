import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
)

questionOne = input("What is your favourite movie, and why?: ")
questionTwo= input("What is your genre?: ")
questionThree = input("Who is your favourite director?: ")
questionFour = input("Who is your favourite actor(s): ")
questionFive = input("Do you want something mainstream, or something, niche😏? (Pick one of the two options): ")
questionSix = input("Do you want something in english, or foreign? (Pick one of the two options): ")
questionSeven = input("Do you want something old, or something more recent, or maybe something in between?: ")
questionEight = input("Do you something long, medium, or short runtime?: ")

questions = [f"What is your favourite movie, and why?: {questionOne}", 
             f"What is your genre?: : {questionTwo}", 
             f"Who is your favourite director?: {questionThree}", 
             f"Who is your favourite actor(s)?: {questionFour}", 
             f"Do you want something mainstream, or something, niche? (Pick one of the two options): {questionFive}",
             f"Do you want something in english, or something foriegn? (Pick one of the two options): {questionSix}",
             f"Do you want something old, or something more recent, or maybe something in between?: {questionSeven}",
             f"Do you something long, medium, or short runtime?: {questionEight}"
            ]

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3.2:novita",
    messages=[
        {
            "role": "user",
            "content": f"Recommend me a movie based off of the questions and answers proivded from the user: {questions}. When you find a movie to recommend, \
            explain why this would be a good choice, the questions asked to the user. Note, the current year is 2026, so base the seventh question and answer off this year \
            If the context provided does not match the information given to you, respond, with `Sorry, I don't have a movie \
            for you, please try again using different responses`. (Don't include the quotations). Respond with this again if a question was answered incorrectly or \
            inappropiately (e.g answering neither to (Do you want something mainstream, or something, niche? (Pick one of the two options)), or, answering with swear words or \
            unrelated terms. Do not under any circumstance make up a movie." 
        }
    ],
)

print(completion.choices[0].message.content)