import markdown
from jinja2 import Template

# 1. Ler o modelo HTML (src/template.html)
with open("src/template.html", "r", encoding="utf-8") as archive:
    template_text = archive.read()

# 2. Ler o texto em Markdown (src/data.md)
with open("src/data.md", "r", encoding="utf-8") as archive:
    markdown_text = archive.read()

# 3. CONVERTER o Markdown em HTML (transforma # em <h1>, - em <li> (item de lista), etc.)
content_html = markdown.markdown(markdown_text)

# 4. Injetar o HTML gerado no template usando o Jinja2
template = Template(template_text)
page = template.render(content=content_html)

# 5. Salvar o arquivo index.html estático final na raiz
with open("index.html", "w", encoding="utf-8") as archive:
    archive.write(page)

print("Página gerada e convertida com sucesso!")