
# Projeto de Testes: Web Scraping, Transformação de Dados, Banco de Dados e API

![GitHub last commit](https://img.shields.io/github/last-commit/rafaelberg/test_rh_intuitive)

Este é um projeto completo que abrange quatro módulos principais: coleta de dados, transformação de dados, banco de dados e API.

## 📋 Sumário
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Pré-requisitos](#pré-requisitos)
- [Configuração](#configuração)
- [Uso](#uso)

## ✨ Funcionalidades
- **Web Scraping**: Coleta automática de PDFs do site da ANS.
- **Transformação de Dados**: Conversão de PDF para CSV com tratamento de dados.
- **Banco de Dados**: Estruturação relacional e criação de queries analíticas.
- **API**: Interface web com Vue.js e endpoints RESTful para interação com o backend.

## 🚀 Tecnologias
- **Backend**: Python 3.8+, Flask
- **Frontend**: Vue.js 3
- **Banco de Dados**: MySQL 8.0+
- **Ferramentas**: Postman

## 📋 Pré-requisitos
Certifique-se de ter as seguintes ferramentas instaladas:
- **Python 3.8+**
- **Node.js 14+**
- **MySQL 8.0+**
- **Git**

## ⚙️ Configuração
1. Clone o repositório:
```bash
git clone https://github.com/rafaelberg/test_rh_intuitive.git
cd test_rh_intuitive
```

2. Criação do arquivo `.env`:  
   Crie um arquivo `.env` na raiz do projeto com as variáveis de ambiente necessárias:
```env
DB_HOST=localhost
DB_USER=<seu_usuario>
DB_PASSWORD=<sua_senha>
DB_NAME=test_rh_intuitive
```

## 🚀 Uso
Após configurar o ambiente, execute o seguinte comando para iniciar tanto o backend quanto o frontend simultaneamente:
```bash
python start.py
```

## 📑 Documentação da API
A documentação completa da API pode ser acessada através do **Postman**. Para visualizar e testar os endpoints, utilize o link abaixo:

[Documentação da API no Postman](https://documenter.getpostman.com/view/33303998/2sB2cPjkPS)