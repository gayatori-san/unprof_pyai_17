import os
import sys
import google.generativeai as genai

def main():
    # 1. Fetch the API key from the environment
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("⚠️  Error: GEMINI_API_KEY environment variable not found.")
        print("Please set it by running: export GEMINI_API_KEY='your_api_key_here'")
        sys.exit(1)

    # 2. Configure the Gemini API
    genai.configure(api_key=api_key)
    
    # We use gemini-1.5-flash as it is fast and highly efficient for text tasks
    model = genai.GenerativeModel('gemini-1.5-flash')

    print("========================================")
    print("🤖 Welcome to the Gemini CLI Assistant!")
    print("Type 'exit' or 'quit' to end the session.")
    print("========================================\n")

    # 3. Main Chat Loop
    while True:
        try:
            # Get user input
            user_input = input("You: ")
            
            # Exit condition
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye! 🚀")
                break
                
            # Skip empty prompts
            if not user_input.strip():
                continue

            # 4. Generate Response
            response = model.generate_content(user_input)
            print(f"\n🤖 AI: {response.text}\n")

        except Exception as e:
            # 5. Graceful Error Handling
            print(f"\n⚠️  An error occurred communicating with the API: {e}\n")
            print("Please check your internet connection or API key constraints.\n")

if __name__ == "__main__":
    main()