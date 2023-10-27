def buildPrompt(user_message):
    prompt = {"user_message":user_message, "system_message":"You are a product owner helping a user understand their new feature request requirements."}
    return prompt