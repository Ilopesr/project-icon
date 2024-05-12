import os
from pathlib import Path


def remove_fill_attr_and_add_class_attr(file_path, new_path):
    """
    Primeiramente vamos ler o arquivo, e fazer o replace do seguinte código
    'xmlns="http://www.w3.org/2000/svg"' => 'xmlns="http://www.w3.org/2000/svg" class="{{class}}"'

    Posteriormente vamos retirar todos os fills do código, para isso precisamos
    verificar as cores padrões dos nossos icons, interessante sempre colocar
    cores padrões no figma.

    Fazer o replace dos attrs "fill" com os valores abaixo
    ''fill="#374957"' e 'fill="white"' => "" (empty str)

    E sobrescrever em outro local, com a extensão '.html', també reescrevendo
    o nome do icon, e gerando um documento com o seguinte texto:

    nome_do_icon: "path/to/icon/folder"

    """
    for filename in os.listdir(file_path):
        with open(file_path / filename, "r") as rfile:
            content = rfile.read()
            content = content.replace(
                'xmlns="http://www.w3.org/2000/svg"',
                'xmlns="http://www.w3.org/2000/svg" class="{{class}}"',
            )

            content = content.replace('fill="#374957"', "")
            content = content.replace('fill="white"', "")

            extract_filename = rfile.name.split("\\")[-1].split(".")[0]
            filename = "".join(extract_filename.split("-")[2:]) + ".html"
            re_new_path = os.path.join(new_path, filename)

        with open("components.yaml", "a+") as yaml_file:
            text = "%s: %s%s\n" % (
                "".join(extract_filename.split("-")[2:]),
                "interface/icons/",
                filename,
            )
            yaml_file.write(text)

        with open(re_new_path, "w") as wfile:
            wfile.write(content)


BASE_DIR = Path(__file__).resolve().parent
ICONS_SVG_PATH = BASE_DIR / "icons-svg/"
ICONS_HTML_PATH = BASE_DIR / "icons-html/"

remove_fill_attr_and_add_class_attr(ICONS_SVG_PATH, ICONS_HTML_PATH)
