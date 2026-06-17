key="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"
from openai import OpenAI
client=OpenAI(api_key=key)

while True :
    user=input("You : ")
    if(user.lower()=="bye"):
        print("Ok bye !!")
        break
    else:
        response=client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {'role':"user",'content':user}
            ]
        )
        print("Bot :",response.choices[0].messages.content)