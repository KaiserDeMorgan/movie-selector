import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
)

q1 = "What is your favourite movie, and why?: "
q2 = "What is your favourite genre?: "
q3 = "Who is your favourite director?: "
q4 = "Who is your favourite actor(s): "
q5 = "Do you want something mainstream, or something, niche😏? (Pick one of the two options): "
q6 = "Do you want something in english, or foreign? (Pick one of the two options): "
q7 = "Do you want something old, or something more recent, or maybe something in between?: "
q8 = "Do you want something long, medium, or short runtime?: "

q1Response = input(q1)
q2Response = input(q2)
q3Response = input(q3)
q4Response = input(q4)
q5Response = input(q5)
q6Response = input(q6)
q7Response = input(q7)
q8Response = input(q8)

questions = [f"{q1} {q1Response}", 
             f"{q2} {q2Response}", 
             f"{q3} {q3Response}", 
             f"{q4} {q4Response}", 
             f"{q5} {q5Response}",
             f"{q6} {q6Response}",
             f"{q7} {q7Response}",
             f"{q8} {q8Response}"
            ]

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1:novita",
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
    ]
)

print(completion.choices[0].message.content)