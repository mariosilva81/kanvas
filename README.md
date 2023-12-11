<p align="center">
  <a href="https://www.djangoproject.com" target="blank"><img src="https://cdn.worldvectorlogo.com/logos/django.svg" width="100" alt="Django Logo" /></a>
</p>

# Kanvas

## Descrição

API Rest para o gerenciamento de cursos e aulas de uma escola na modalidade EAD.

## Autor

Mario Silva

## Versão

1.0.0

## Tecnologias Utilizadas

<div style="display: flex;">
  <img src="https://cdn.worldvectorlogo.com/logos/django.svg" height="50" alt="Django" style="margin-right: 10px;">
  <img src="https://seeklogo.com/images/S/swagger-logo-A49F73BAF4-seeklogo.com.png" height="50" alt="Swagger" style="margin-right: 10px;">
</div>

## Dependências

Vide arquivo `requirements.txt` na raiz do projeto.

## Instalação

1. Clone o repositório: 

```bash
git@github.com:mariosilva81/kanvas.git
```

2. Navegue até o diretório do projeto.

3. Execute o seguinte comando para criar um ambiente virtual:

```
python -m venv venv
```

Se você estiver usando o Python 3.3 ou 3.4, pode ser necessário instalar a ferramenta venv separadamente usando pip install virtualenv.

4. Ative o ambiente virtual:

No Windows:

```
venv\Scripts\activate
```

No MacOS/Linux:

```
source ven/bin/activate
```

Quando o ambiente virtual estiver ativo, o prompt de comando mudará para mostrar o nome do ambiente.

5. Instale as dependências:

```
pip install -r requirements.txt
```

6. Crie e Aplique as Migrações:

```bash
# Cria as migrações
python manage.py makemigrations

# Aplica as migrações
python manage.py migrate
```

## Executando o Projeto

Execute o seguinte comando para iniciar o servidor:

```
python manage.py runserver
```

A aplicação estará acessível localmente em [http://localhost:8000](http://localhost:8000). 

Se precisar especificar uma porta diferente, você pode fornecer o número da porta como argumento para o comando runserver, por exemplo:

```
python manage.py runserver 8080
```

## Execução dos testes:

Para rodar a bateria de testes, utilize:

```
pytest --testdox -vvs
```

## Endpoints

|`Método`| `Endpoint`     | `Responsabilidade`                 | `Autenticação`      |
| ------ | -------------- | ---------------------------------- | ------------------- |
| POST   | /api/login/    | Gera o token de autenticação       | Livre               |
| POST   | /api/accounts/ | Criação de usuário                 | Livre               |
| POST   | /api/courses/  | Criação de cursos                  | Somente super usuários |
| GET    | /api/courses/  | Listagem de cursos                 | Somente usuários autenticados |
| GET    | /api/courses/<course_id>/ | Busca de curso por ID   | Acesso livre à administradores. Estudantes não podem acessar cursos que não participam |
| PATCH  | /api/courses/<course_id>/ | Atualização *somente* dos dados de curso | Somente super usuários |
| DELETE | /api/courses/<course_id>/ | Deleção de curso | Somente super usuários |
| POST   | /api/courses/<course_id>/contents/ | Criação de conteúdos e associação ao curso | Somente super usuários |
| GET | /api/courses/<course_id>/contents/<content_id>/ | Busca de conteúdo por ID | Super usuários têm acesso livre. Estudantes só podem acessar dos que participam |
| PATCH | /api/courses/<course_id>/contents/<content_id>/ | Atualização *somente* do conteúdo | Somente super usuários |
| DELETE | /api/courses/<course_id>/contents/<content_id>/ | Deleção de conteúdos | Somente super usuários |
| PUT | /api/courses/<course_id>/students/ | Adição de alunos ao curso | Somente super usuários |
| GET | /api/courses/<course_id>/students/ | Listagem dos estudantes do curso | Somente super usuários |


Para mais informações, consulte a documentação disponível em [http://localhost:8000/api/docs](http://localhost:8000/api/docs) ou em [https://kanvas-2ni9.onrender.com/api/docs/](https://kanvas-2ni9.onrender.com/api/docs/)

## Deploy

Caso queira testar a aplicação em produção, a mesma está disponível em [https://kanvas-2ni9.onrender.com](https://kanvas-2ni9.onrender.com).

## Contato

Para questões ou sugestões, entre em contato através do email: mariosilva.81@icloud.com.
