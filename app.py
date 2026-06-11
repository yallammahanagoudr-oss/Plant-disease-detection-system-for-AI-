import google.generativeai as genai

# Gemini API Key
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

print("🌱 Plant Disease Diagnosis Expert")
print("Type 'exit' to quit\n")

while True:
    user_input = input("Describe plant disease symptoms: ")

    if user_input.lower() == "exit":
        break

    prompt = f"""
    You are an agriculture expert.

    Analyze the following plant symptoms:
    {user_input}

    Give:
    1. Disease Name
    2. Cause
    3. Symptoms
    4. Treatment
    5. Prevention Tips
    """

    response = model.generate_content(prompt)

    print("\nDiagnosis Result:")
    print(response.text)
    print("-" * 50)
