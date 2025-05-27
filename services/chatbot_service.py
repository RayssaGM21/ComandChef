import google.generativeai as genai
import os
import json


def busca_modelo_disponivel():
    all_available_models = []
    # Verifica modelos disponíveis
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            all_available_models.append(m.name)

    PREFERRED_MODELS = [
        'gemini-1.5-flash',
        'gemini-1.5-flash-latest',
        'gemini-1.5-pro',
        'gemini-1.5-pro-latest',
        'gemini-pro',
        'gemini-2.5-flash-preview-05-20',
        'gemini-2.5-pro-preview-05-06',
        'gemma-3-8b-it',
        'gemma-3-4b-it'
    ]

    for preferred_model in PREFERRED_MODELS:
        if f'models/{preferred_model}' in all_available_models:
            # print(f"Modelo selecionado: '{preferred_model}'.")
            return f'models/{preferred_model}'
        elif preferred_model in all_available_models:
            # print(f"Modelo selecionado: '{preferred_model}'.")
            return preferred_model

    # nenhum dos modelos preferidos foi encontrado
    for model_name in all_available_models:
        if "vision" not in model_name.lower():
            # print(f"Modelo selecionado: '{model_name}'.")
            return model_name

    return None


def iniciar_chatchef(pratos_data, clientes_data, fila_pedidos_data, pratos_em_promocao):
    API_KEY = os.getenv("GOOGLE_API_KEY")

    if not API_KEY:
        API_KEY = "" # insira a chave aqui para testes, ou configure a variável de ambiente

    genai.configure(api_key=API_KEY)

    nome_modelo = busca_modelo_disponivel()

    if not nome_modelo:
        # verificar sua chave de API
        print("Ops!! Houve problema técnicos, tente novamente mais tarde")
        return

    model = genai.GenerativeModel(nome_modelo)

    pratos_str = json.dumps(pratos_data, ensure_ascii=False, indent=2)
    clientes_str = json.dumps(clientes_data, ensure_ascii=False, indent=2)
    fila_pedidos_serializavel = [pedido.to_dict() for pedido in fila_pedidos_data]
    fila_pedidos_str = json.dumps(fila_pedidos_serializavel, ensure_ascii=False, indent=2)


    prompt_inicial = f"""
    Você é um chatbot que se chama ChatChef, que auxilia um restaurante que se chama Command Chef. 
    Sua função é responder perguntas sobre o menu e os pedidos dos clientes.
    Mantenha as respostas concisas e diretas. Mas seja educado!
    
    Aqui estão as informações disponíveis:

    **PRATOS DISPONÍVEIS:**
    {pratos_str}

    **CLIENTES CADASTRADOS:**
    {clientes_str}

    **FILA DE PEDIDOS:**
    {fila_pedidos_str}

    **PRATOS EM PROMOÇÃO:**
    {pratos_em_promocao}

    Responda às perguntas usando apenas as informações fornecidas e seja útil ao cliente. 
    Fique atento a possíveis alergêncos presentes nos ingredientes dos pratos fornecidos e procure a tabela nutricional dos alimentos caso necessário!
    """

    chat = model.start_chat(history=[
        {"role": "user", "parts": [prompt_inicial]},
        {"role": "model", "parts": ["Ok, estou pronto para ajudar com informações sobre o restaurante Command Chef e seus respectivos pedidos!"]}
    ])


    print("\n" + "="*70)
    print("Olá! Eu sou o assistente do restaurante, o ChatChef. Como posso ajudar?")
    print("Digite 'sair' para encerrar a conversa a qualquer momento.")
    print("="*70 + "\n")

    while True:
        user_message = input("Você: ")

        if user_message.lower() == 'sair':
            print("ChatChef: Até mais! Volte sempre!")
            break

        try:
            response = chat.send_message(user_message)
            print(f"ChatChef: {response.text}")

        except Exception as e:
            print(f"Ocorreu um erro ao gerar a resposta: {e}")
            print("Verifique sua conexão com a internet ou sua chave de API.")


