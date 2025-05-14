
import openai

# Coloque sua chave da OpenAI aqui
openai.api_key = "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"

def conversar():
    print("Bot IA: Olá! Pergunte qualquer coisa (digite 'sair' para encerrar).")
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == "sair":
            break

        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente inteligente e amigável."},
                {"role": "user", "content": pergunta}
            ]
        )

        print("Bot IA:", resposta['choices'][0]['message']['content'])

conversar()
