import requests

def send_azure_request(messages, model):
    """Send a request to Azure OpenAI and return the response."""
    endpoint = 'ENTER AZURE_OPENAI_ENDPOINT'
    api_key = 'AZURE_OPENAI_KEY'
    
    headers = {'Content-Type': 'application/json', 'api-key': api_key}
    payload = {'messages': messages, 'model': model}
    
    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to connect to Azure OpenAI. Details: {e}")
        return None

def main():
    print("Azure OpenAI Terminal Tester")
    print("This tool helps you test your Azure OpenAI connection and interact with models.")
    
    model = input("Enter the model name (default: gpt-4): ").strip() or "gpt-4"
    print(f"Using model: {model}")
    
    conversation_history = []
    
    while True:
        user_input = input("\nEnter your message (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the tester. Goodbye.")
            break
        
        conversation_history.append({"role": "user", "content": user_input})
        response = send_azure_request(conversation_history, model)
        
        if response:
            print(f"\nAzure AI response: {response}")
            conversation_history.append({"role": "assistant", "content": response})
        else:
            print("Failed to get a response. Please check your connection and try again.")

if __name__ == '__main__':
    main()
