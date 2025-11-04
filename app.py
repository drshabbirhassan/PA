import streamlit as st
from groq import Groq

# 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---------------------------
# 1. Initialize Groq client
# ---------------------------
# Make sure you have your API key ready and stored safely
# (Do NOT hardcode it in production)
client = Groq(api_key="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")

# ---------------------------
# 2. Prompt Template
# ---------------------------
prompt_template = """
You are an academic assistant designed for undergraduate students of Public Administration. 
Your role is to help students understand and integrate ideas about:
- Public Administration theories
- Classic and New Public Administration
- Public Policy and Governance
- Administrative Thinkers (Weber, Taylor, Gulick, etc.)
- Modern approaches like New Public Management and E-Governance.

### Your Tasks:
1. When a user asks a question, identify its type:
   - Definition
   - Explanation
   - Comparison
   - Application / Example
   - Policy analysis
2. Give a **clear, short, and easy-to-read answer** suitable for BS students.
3. Use **simple language**, avoid jargon, and if you must use a technical term, explain it briefly.
4. Keep responses educational, accurate, and neutral.
5. Optionally, suggest one or two related questions to help the student explore more.

### Example Interaction:

**Student:** What is New Public Management?  
**Assistant:**  
New Public Management (NPM) is a modern approach to running public organizations.  
It focuses on efficiency, results, and using private-sector ideas in government work.  
For example, it promotes competition, performance measurement, and customer service in public offices.  
**Question Type:** Definition  
**Related Questions:**  
- How is NPM different from Traditional Public Administration?  
- What are the main features of NPM?

Now respond to the user's question.
"""

# ---------------------------
# 3. Streamlit App Interface
# ---------------------------
st.set_page_config(page_title="Public Administration AI Assistant", page_icon="📘")

st.title("📘 Public Administration AI Assistant")
st.write("Ask questions about Public Administration, Public Policy, or Governance in simple language.")

user_input = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if user_input.strip() == "":
        st.warning("Please enter a question first.")
    else:
        # Combine system prompt with user's question
        full_prompt = f"{prompt_template}\n\nStudent: {user_input}\nAssistant:"

        # Call the Groq model
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama3-8b-8192",  # you can change to other Groq-supported models
                messages=[
                    {"role": "system", "content": prompt_template},
                    {"role": "user", "content": user_input},
                ],
                max_tokens=500,
                temperature=0.7,
            )

        # Extract and show AI's response
        answer = response.choices[0].message["content"]
        st.markdown("### 🧠 AI Response:")
        st.write(answer)
