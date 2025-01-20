import requests

GEMINI_API_KEY = "AIzaSyDxdqpnLVamqper0L5UjkCfVdXsdO8GwIk"

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

headers = {"Content_Type": "application/json"}

def get_gemini_response(user_input):
    # Preparing the request
    data = {"contents":[{"parts":[{"text":user_input}]}]}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        #Checks if successful, if yes then extracts the content
        response_data = response.json()

        #Extract the response text
        if response_data.get("candidates"):
            bot_response = response_data["candidates"][0]["content"]["parts"][0]["text"]
            return bot_response
        
        else:
            return "No response found in the API output"
        
def chat():
    print("Welcome to the Gemini AI Chatbot! Type exit to quit")

    while True:
        user_input = input("You: ")

        if user_input.lower()=="exit":
            print("Goodbye!")
            break

        bot_response = get_gemini_response(user_input)

        print("Bot: ", bot_response)

if __name__ == "__main__":
    chat()