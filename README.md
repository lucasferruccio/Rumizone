# Rumizone - Gerenciamento de Fazenda 🐄

## 📌 Descrição do Projeto

**Rumizone** é um sistema de gerenciamento para fazendas, com foco no controle de gado. Desenvolvido durante o primeiro período da faculdade, ele permite:

- **Cadastro e gerenciamento de usuários** 👥
- **Controle e monitoramento do rebanho** 🐂
- **Registro de relatórios sobre o gado** 📊
- **Análise automatizada das vacas via YOLO** 📷

## 📂 Estrutura do Projeto

```
RUMIZONE
└───Rumizone_App
    │   crud.py
    │   funcApp.py
    │   GUI_Definitivo.py
    │   readme.txt
    │
    ├───DataBase
    │       rumizonedb_fazenda.sql
    │       rumizonedb_keeplogin.sql
    │       rumizonedb_relatorios.sql
    │       rumizonedb_usuario.sql
    │       rumizonedb_vacas.sql
    │
    ├───imagens
    │       (arquivos de interface e monitoramento)
    │
    └───monitoramento
            coco.names
            main.py
            yolov4-tiny.cfg
            yolov4-tiny.weights
```

## 🛠 Principais Arquivos:

- **crud.py** - Operações de CRUD no banco de dados
- **funcApp.py** - Funções de negócio do sistema
- **GUI\_Definitivo.py** - Interface gráfica principal
- **monitoramento/main.py** - Monitoramento automatizado via YOLO
- **DataBase/\*.sql** - Scripts do banco de dados MySQL

## 🚀 Como Instalar e Executar

### 1️⃣ Requisitos

- **Python 3.x**
- **MySQL**
- **Bibliotecas:** MySQLdb, OpenCV, YOLO (entre outras)

### 2️⃣ Instalação

Clone o repositório e instale as dependências

### 3️⃣ Configuração do Banco de Dados

- Crie um banco no MySQL chamado `rumizonedb`.
- Execute os arquivos `.sql` dentro da pasta `DataBase` para criar as tabelas.

### 4️⃣ Executar o Sistema

```sh
python Rumizone_App/GUI_Definitivo.py
```

Para rodar o monitoramento via YOLO:

```sh
python Rumizone_App/monitoramento/main.py
```

## ⚠️ Nota Importante

Este projeto foi desenvolvido com fins acadêmicos e pode não conter todas as funcionalidades esperadas em um sistema de produção. Melhorias e novas funcionalidades podem ser implementadas no futuro.

