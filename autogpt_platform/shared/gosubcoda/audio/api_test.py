import openai

def check_openai_api_key(api_key):
    client = openai.OpenAI(api_key=api_key)
    try:
        client.models.list()
    except openai.AuthenticationError:
        return False
    else:
        return True


OPENAI_API_KEY = "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"
if check_openai_api_key(OPENAI_API_KEY):
    print("Valid OpenAI API key.")
else:
    print("Invalid OpenAI API key.")