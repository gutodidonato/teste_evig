# FastAPI Application with OAuth2 and Ollama Integration

Este é um aplicativo FastAPI que utiliza OAuth2 para autenticação e integração com o Ollama para geração de descrições de propriedades. 
O aplicativo também inclui testes unitários para garantir que as operações de criação, atualização, exclusão e leitura de usuários estejam funcionando corretamente.


```sh
docker build -t fastapi-app .
docker run -d -p 8080:8080 --name fastapi-app fastapi-app