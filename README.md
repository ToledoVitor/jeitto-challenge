# jeitto-challenge

Esse projeto é parte de um teste para uma posição de analista de sustentação na Jeitto.

O projeto consiste em três partes principais, um teste de python, um teste de query em sql, e teste de um CRUD em [FastAPI](https://fastapi.tiangolo.com).

## Python

O desafio em python consiste em duas partes:
- Solução para a sequência de Fibonacci
- Perguntas conceituais sobre listas x tuplas

### Fibonacci
A solução se encontra na pasta fibonacci, e é composta de um arquivo apenas.

Dentro deste arquivo se encontram duas funções, uma usando recursão, uma das maneiras mais simples e comuns de se calcular a sequência, e a outra função usando uma lista de valores. Essa segunda sendo a solução ótima, pois evita-se de recalcular inúmeras vezes o mesmo valor, uma vez que ele já estará salvo dentro da lista.

Para executar o arquivo e ver a resposta para um dado valor, rode na raíz do projeto o seguinte comando:

~~~bash  
  python fibonacci/fibonacci.py
~~~

### Listas X Tuplas

Tanto listas quantos tuplas são tipos de dados que armazenam elementos de forma sequencial. Os itens podem ser strings, inteiros, floats, objetos, etc. e tem a sua posição definida na lista/tupla.

A principal diferença entre as duas é que, enquanto a lista é mutável, ou seja, pode-se adicionar, remover ou alterar os seus elementos, a tupla por sua vez é imutável, não podendo sofrer quaisquer alterações. Por conta dessa diferença, tuplas são mais eficientes no quesito de memória e velocidade.

Tuplas são usadas quando se pretende evitar que os dados sejam alterados, e quando se deseja fazer uma operação como um for iterando por algum elemento fixo. Nesse caso, a tupla seria mais rápida do que a lista.

Listas por sua vez são usadas quando se pretende alterar e definir dinamicamente os dados, como quando se deseja retornar uma lista que não se sabe o tamanho, se deseja alterar os seus elementos, remover, adicionar novos, e afins. 


## SQL

A solução se encontra na pasta sql, e é composta de um arquivo apenas.

A proposta do problema era bem simples: "consulta SQL para encontrar o número total de pedidos feitos por cada cliente em uma tabela chamada 'Pedidos', incluindo apenas os clientes que fizeram mais de 5 pedidos". Deste modo, a consulta foi escrita de modo simples e suscinta.


## Pergunta Lista X Tupla



## CRUD / FastAPI

Esse CRUD tem como objetivo simular um serviço simples para gerenciar informações de clientes. Com isso, foram criadas rotas para a criação de novos clientes, e para a busca de clientes.

### Dependências

Esse projeto usa o [poetry](https://python-poetry.org/docs/) para gerenciar todas as dependências. Antes de começar você irá precisará ter instalado o python 3.11 ou superior e o poetry.

### Rodando o proejto

Para rodar o projeto, a partir da raiz do repositório rode o seguinte comando:

~~~bash  
  uvicorn src.main:app
~~~

Caso prefira rodar diretamente pela IDE do VSCode assim como eu, você pode adicionar essa configuração ao seu arquivo launch.json:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Depurador do Python: FastAPI",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "src.main:app",
                "--reload"
            ],
            "jinja": true
        }
    ]
}
```

### API's

Aqui seguem dois exemplos de requests que você pode copiar para testar o projeto.

A primeira, feita para criar um novo usuário:

```bash
curl --location 'http://localhost:8000/clients/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Cliente Teste",
    "email": "cliente@teste.com",
    "phone": "1199990000"
}'
```

E a segunda, feita para buscar um usuário:

```bash
curl --location 'http://localhost:8000/clients/1'
```

Ps. Lembre-se de primeiro criar o cliente antes de buscá-lo.

### Testes

Os teste unitários ficam dentro da pasta tests/ e foram escritos usando pytest. Para rodá-los direto da linha de comando rode o comando:

~~~bash
python -m pytest
~~~
