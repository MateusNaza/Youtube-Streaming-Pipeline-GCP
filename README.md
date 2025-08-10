# Youtube-Streaming-Pipeline-GCP
      
Projeto de Streaming de dados do Youtube utilizando ecosistema Kafka e GCP.
     
## Indice     
1. [Estrutura do Projeto (em construção)]()   
2. [Como Executar](#como-executar)
      
## Como executar
     
### 1. Crie um ambiente python e instale as dependências necessárias.
```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```         

### 2. Crie o diretório config e dentro dele insira o arquivo .env contendo a seguinte estrutura.
```bash
API_KEY=<sua_chave_api>
```   

> ℹ️ **Observação:** Para conseguir sua chave API do youtube recomendo que veja esse tutorial 
> [este vídeo tutorial passo a passo](https://www.youtube.com/watch?v=qNejkMYBxFg) que ensina como gerar sua chave dentro do Google Cloud Console.

       
### 3. Suba a estrutura Kafka em containeres Docker com o comando a seguir.
```bash
docker compose up -d
```
      
### 4. Rode o script para produzir os dados e inicializar o tópico
```bash
python main.py
```     
      
### 5. Acesse seu localhost na porta 9021 para visualizar a interface Kafka e interagir com os tópicos.