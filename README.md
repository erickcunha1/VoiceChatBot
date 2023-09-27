Claro, vou criar um README em português para o seu projeto.

---

# Assistente de Voz com GPT-3.5 Turbo

Este projeto é um assistente de voz simples que utiliza o GPT-3.5 Turbo da OpenAI para gerar respostas com base na entrada do usuário.

## Funcionalidades

- Reconhecimento de fala para capturar a entrada do usuário.
- Modelo GPT-3.5 Turbo para gerar respostas do assistente.
- Texto para fala para vocalizar as respostas do assistente.

## Primeiros Passos

### Pré-requisitos

- Python 3.x
- Biblioteca Python `speech_recognition`
- Biblioteca Python `dotenv`
- Biblioteca Python `openai`
- Biblioteca Python `pyttsx3`

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu_usuario/assistente-voz-gpt3.git
    cd assistente-voz-gpt3
    ```

2. Instale as bibliotecas Python necessárias:

    ```bash
    pip install -r requirements.txt
    ```

### Configuração

1. Obtenha uma chave de API para o GPT-3.5 Turbo da OpenAI.

2. Crie um arquivo `.env` no diretório do projeto e adicione sua chave de API:

    ```plaintext
    OPENAI_API_KEY=sua_chave_api_aqui
    ```

## Uso

1. Execute o script Python:

    ```bash
    python main.py
    ```

2. Fale no microfone quando solicitado com "Comece a falar".

3. O assistente irá gerar uma resposta usando o GPT-3.5 Turbo e falar a resposta.

## Contribuições

Se deseja contribuir para este projeto, abra uma issue ou crie um pull request. Agradeço as contribuições!
