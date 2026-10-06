import markdown
from jinja2 import Template

# Lê markdown
with open("src/data.md", "r", encoding="utf-8") as file:
    content = file.read()

# Converte de markdown em html
content_html = markdown.markdown(content)

# Lê html
with open("src/template.html", "r",encoding="utf-8") as file:
    template = Template(file.read())

# Insere conteúdo na página
page = template.render (content = content_html, title="Portfólio de Engenharia | Rosana Francisco")

# Escreve a página final
with open("index.html", "w",encoding="utf-8") as file:
    file.write(page)

print("Portfólio gerado!")