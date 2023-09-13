# Flask-login-app

Utilizamos nesta aplicação o Flask-Login e o Flask-SQLAlchemy para construir um sistema de login para o nosso aplicativo e abordamos como
autenticar um usuário. Primeiro, criamos um modelo de usuário e armazenamos suas informações. Em seguida, foi necessário verificar se a
senha do usuário estava correta utilizando o hash na senha do formulário e comparando-a com a armazenada no banco de dados. 
Também temos um botão para fazer Upload, aonde podemos salvar arquivos diretamente em uma pasta. 
Recomenda-se a utilização de uma maquina virtual, que pode ser executada pelos comandos: 
$ python3 -m venv auth $ source auth/bin/activate 
Os comandos para definição das variáveis de ambiente são: 
$ export FLASK_APP=project $ export FLASK_DEBUG=1 
Para instalação dos módulos necessários, de acordo com requeriments.txt. Fazer um cd para o diretório aonde requirements.txt está localizado, e
executar: /n
$ pip install -r requeriments.txt no seu shell. 
Por fim o comando para execução da aplicação: 
$ flask run
