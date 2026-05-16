# Lab-9-Project3
# Lab 9 — Week 9: GenAI Domain Assistant (Part 1)
# Overview
This project demonstrates how to build an AI-powered chatbot using the OpenAI API. The lab focuses on creating conversational agents, handling multi-turn dialogue, and designing domain-specific assistants such as HR and customer support bots.By completing this lab, we learn how to integrate GPT models into Python applications and customize their behavior using system prompts.
# Objectives
1. Set up OpenAI API environment
2. Make first API call using GPT model
3. Build a conversational chatbot with memory 
4. Implement system prompts for behavior control
5. Create domain-specific assistants (HR + Customer Support)
# Technologies Used
Python
Gemini 2.5 Flash
Kaggle Notebook
# Objectives
1. Formulated an API connection using the up-to-date google-genai SDK.
2. Successfully implemented a multi-turn conversation loop maintaining context history natively.
3. Configured a generic chatbot with foundational persona boundaries via system instructions.  
4. Built and validated a domain-specific HR Policy Assistant.  
5. Built and validated a domain-specific TechShop Customer Support Agent.
# Setup & Configuration Instructions
Secure API Credentials
To ensure credentials are not committed to source control:  
Obtain an API Key from Google AI Studio.
In your Kaggle Notebook interface, navigate to the top toolbar: Add-ons Secrets.
Create a new secret entry:
Label: GEMINI_API_KEY
Toggle the visibility checkbox to Attach the secret securely to the notebook environment instance.
# Lab Verification & Automated Grading Responses
1. HR Assistant Validation   
System Persona Boundaries: Configured with fixed parameters defining a strict 15-day vacation cap, unlimited sick leave constraints, 3-day split remote work regimes, and custom 401(k) matching tiers.  
Pre-coded Verification Execution Questions Evaluated Natively:  
"How many vacation days do I get?"   
"Can I work from home?"   
"What about health insurance?"   
"How does 401(k) matching work?"   
2. Customer Support Bot Validation   
System Persona Boundaries: Configured with TechShop retail guidelines including a 30-day return enforcement matrix, dynamic shipping pricing thresholds ($50 order cutoff value), and standard hardware warranties.  
Pre-coded Verification Execution Scenarios Evaluated Natively:  
"I want to return a product I bought 2 weeks ago"   
"How much is shipping?"   
"My laptop stopped working after 6 months"
# Execute the Notebook
Open the .ipynb file within your Kaggle editor runtime environment.
Run the initialization cells sequentially to mount dependencies and establish the secure API hook.
Run the HR Assistant or Customer Support function modules.
Input statements directly into the interactive prompt line interface layout matching test cases or input your own text, typing quit anytime to safely drop the runtime loops.
# Outcome
Successfully built a working AI chatbot system capable of:
Multi-turn conversations
Role-based behavior (HR & Support)
Real-world use case simulation

# Author
Aliha Batool — AI Lab 9 (Week 9)
