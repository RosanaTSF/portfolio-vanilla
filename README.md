# Portfolio & Gerador de Sites Estáticos

Este projeto é um gerador de páginas estáticas minimalista desenvolvido em Python. Ele funciona como um laboratório de aprendizado para processar arquivos de conteúdo em Markdown, aplicar templates estruturados com Jinja2 e gerar um site final para a apresentação de portfólio e currículo digital.

## Objetivo

Automatizar a criação de páginas web a partir de arquivos de texto, garantindo a separação entre o conteúdo e a apresentação visual.

## 🛠️ Tecnologias

* **Python 3** — Lógica principal do gerador.
* **Jinja2** — Mecanismo de templates.
* **Markdown** — Escrita e organização do conteúdo.
* **HTML5 & CSS3** — Estrutura e estilização da página gerada.

## Fluxo de Trabalho

O processo de compilação do site ocorre através das seguintes etapas:

```text
Markdown ➔ Python ➔ Jinja2 ➔ HTML ➔ CSS
```

## Estrutura do Projeto

```text
portfolio/
├── src/
│   ├── data.md        # Dados em Markdown
│   ├── template.html  # Estrutura do HTML com as tags do Jinja2
│   └── render.py      # Script Python responsável pelo build
├── style.css          # Estilos do site
├── index.html         # Página final gerada automaticamente
└── .gitignore         # Arquivos ignorados pelo Git
```

## Como Executar

1. **Instale as dependências necessárias:**
   ```bash
   pip install markdown jinja2
   ```

2. **Execute o script de geração:**
   ```bash
   python src/render.py
   ```

3. **Visualize o resultado:**
   Abra o arquivo `index.html` recém-gerado diretamente no seu navegador.

## Roadmap de Desenvolvimento

* [x] Estrutura inicial do repositório configurada.
* [x] Integração de leitura e processamento de Markdown com Python e Jinja2.
* [x] Geração automatizada do arquivo `index.html`.
* [ ] Implementação de parametrização dinâmica de metadados.
* [ ] Ajustes e layout.
* [ ] Adição de novos projetos e experiências profissionais no arquivo `data.md`.
