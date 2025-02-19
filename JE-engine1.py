import requests
import json

api_key = "######################" 

url1 = "http://localhost:11434/api/chat" # for meta-llama model
url = "https://api.openai.com/v1/chat/completions" # for openai model

model1 = "gpt-3.5-turbo"
model2= "gpt-4"

#--------TRANSACTION READING-----------------------
transaction = "Paid $2,000 for inventory purchased on credit"
#transactionUser = input('Enter transaction: ')
#transactionRead = "hold" #read transaction from a file
#------------------------------------------

#--------prompt engineering-------------
start = "make a journal entry for this transaction, "
form = "output should be in this form: \n"
line1 = "D account, amount \n"
line2 = "C account, amount \n"
end = "number of lines should be equal to the number of accounts that are affected by the transaction; where D is debit and C is credit: "
post = "Do not add any explanation, notes or calculation in the output."
#----------------------------------------

#------------------OPENAI MODEL--------------------------------
def openai (prompt):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'model' : model2,
        'messages' : [
            {
                "role" : "user",
                "content" : prompt,
            }
            
        ],
        #'max_tokens': 50
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']
    #return response.json()
#----------------------------------------------------------------

#--------------------META LLAMA MODEL-----------------------------
def llama3(prompt):
    data = {
        "model": "llama3.1",
        "messages": [
            {
                "role": "user",
                "content": prompt

            }
        ],
        "stream": False,
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url1, headers=headers, json=data)
    return response.json()["message"]["content"]
#---------------------------------------------------------------


prompt = start + form + line1 + line2 + end + transaction + post 

response1 = openai(prompt)
response2 = llama3(prompt)

print("OpenAi Response \n")
#print(response1 + "\n") # from openai chat-gpt
print(response1)
print("Meta-llama Response \n")
print(response2) # from meta-llama