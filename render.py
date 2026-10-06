import markdown
from jinja2 import Template

# Lê markdown
with open("src/data.md", "r", encoding="utf-8") as file:
    content = file.read()

# Converte de markdown em html
content = markdown.markdown(content)

# Lê html
with open("src/template.html", "r",encoding="utf-8") as file:
    template = Template(file.read())

# Insere o conteúdo na página
page = template.render (content = content)

# Gera a página final
with open("index.html", "r",encoding="utf-8") as file:
    file.read()

print("Portfólio gerado!")