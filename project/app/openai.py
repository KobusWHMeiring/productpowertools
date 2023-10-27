import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")



def chat3turbo(prompt):
    
    user = prompt['user_message']
    system = prompt['system_message']
    
    
    print("completion running")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
        {"role": "user", "content": user},
        {"role": "system", "content": system}
        ]  
    )

    response = completion.choices[0].message.content
    
    
    return response

def chat4(prompt):
    user = prompt['user_message']
    system = prompt['system_message']
     
    print("chat4 ran")
    
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": user},
        {"role": "system", "content": system}
    ]  
    )
    
    response = completion.choices[0].message.content
    print("response in gpt4")
    print(response)
    return response