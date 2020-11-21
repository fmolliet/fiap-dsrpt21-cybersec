# DSRPT SEARCH DATA API 🛰

API de webscrapying e public data. Para o desenvolvimento utilizei request, beatuiful soup para formatação e Flask para disponibilizar o serviço como API. Para subir o sistema ter nos requisitos:

  - Python 3.7.6 com a lib [Flask](https://flask.palletsprojects.com/en/1.1.x/)

## Instalação 🐍

Instale a biblioteca pelo pip install e clona o repositório.

```sh
$ pip install flask requests urllib3 beautifulsoup4
$ git clone https://github.com/fmolliet/fiap-dsrpt21-cybersec
$ cd fiap-dsrpt21-cybersec
```

OU


```sh
$ git clone https://github.com/fmolliet/fiap-dsrpt21-cybersec
$ cd fiap-dsrpt21-cybersec
$ pip install requirements.txt 
```

OU 

```Via virtual Env (venv)```

## Build 🐳
<br />

```sh
$ python server.py
```

## Testando ⚙

Para testar API basta iniciar o servidor. Ele estará rodando na porta 5000 de padrão.

As rotas liberadas são:

/search    - POST 

/haveibeen - POST 

### Em search:

Body: JSON
```
{
	"type": "default", // Pode ser: ( file | default | url | title | website )
	"query": "IMHERE" // Conteudo da query que será buscada
}
```

### Em haveibeen:

Body: JSON
```
{
	"email":"teste@teste.com" // email que será buscado
}
```