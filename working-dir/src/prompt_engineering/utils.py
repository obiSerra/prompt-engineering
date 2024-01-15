import jinja2


def load_template(template_file, args={}):
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(template_file)
    outputText = template.render(**args)

    return outputText
