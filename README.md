# Considerações

O desafio foi feito em duas branchs, em uma está simplesmente a tarefa de parse do xml (master), já a outra branch reune
as features de extras (webservice). 

Para o extra foi implementado um microserviço em flask, esse texto exemplifica como executar e testar o webservice  


## Requerimentos

    python 3.5
    docker
    
    //Opcional
    docker-composer

## Instalação
Primeiro crie um ambiente virtual e ative-o

    python3 -m venv .env
    source .env/bin/active
    
    
Instale as dependencias
    
    pip install -r requirements.txt

Instale o redis

    docker run --name freeradius-redis -p 6379:6379/tcp -d redis redis-server --appendonly yes
    
Rode o programa

    sh run.sh DEV

Com os passos acima a aplicação rodará com gunicorn em modo de desenvolvimento.

Para orquestrar essa execução e executar de uma maneira mais automátizada execute (Opcional):

    docker-compose build
    docker-compose up
    
Com docker-composer todos os passos acima serão executados e a aplicação usará o postgres como banco de dados no lugar do sqlite

## Uso
Efetue o registro:

    curl -X POST \
      http://localhost:8000/auth/register \
      -H 'cache-control: no-cache' \
      -H 'content-type: application/json' \
      -d '{
      "first_name": "Felipe",
      "last_name": "Rodrigues",
      "login": "felipernx",
      "password": "123456",
      "email": "rodrigues882007@gmail.com"
      
    }'
    
Faça login:

    curl -X POST \
      http://localhost:8000/auth/login \
      -H 'cache-control: no-cache' \
      -H 'content-type: application/json' \
      -d '{
      "login": "felipernx",
      "password": "123456"
    }'     

Chame o endpoint para fazer p parser o feed:

    curl -X GET \
      http://localhost:8000/feed \
      -H 'authorization: Basic {{TOKEN_RETORNADO_NA_AUTENTICACAO}} \
      -H 'cache-control: no-cache' \
      -H 'content-type: application/json' \
      -H 'postman-token: bce8ede2-dd6c-81f2-872a-53c15cc1e300' \
      -d '{
      "login": "felipernx",
      "password": "password"
    }'
    
## Testes
Execute os testes unitários

    python3 -m unittest