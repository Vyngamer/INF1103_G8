from google import genai
import json

client = genai.Client()
gemini_flash = "gemini-3.8-flash"
gemini_flash_lite = "gemini-3.1-flash-lite"

def interact(text_input, previous_interaction_id):
    interaction = client.interactions.create(
        model=gemini_flash_lite,
        input=text_input,
        previous_interaction_id=previous_interaction_id
    )
    return interaction

def chatbot_welcome_message(survey_data, previous_interaction_id):
    survey_data = json.dumps(survey_data)

    system_instruction = "You are a counseller for a student to assess whether he/she is going to experience burnout."
    prompt = "Here are the results of a survey:\n" + survey_data

    interaction = client.interactions.create(
        model=gemini_flash_lite,
        input=prompt,
        system_instruction=system_instruction,
        previous_interaction_id=previous_interaction_id
    )
    return interaction
