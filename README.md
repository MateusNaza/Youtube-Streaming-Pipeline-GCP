# Youtube-Streaming-Pipeline-GCP
      
Projeto de Streaming de dados do Youtube utilizando ecosistema Kafka e GCP.
     
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
       
### 3. Suba a estrutura Kafka em containeres Docker com o comando a seguir.
```bash
docker compose up -d
```