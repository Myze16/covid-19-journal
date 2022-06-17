from flask import Flask
import os

app = Flask(
    __name__,
    static_folder=os.path.abspath("journal/view/static"),
    template_folder=os.path.abspath("journal/view/templates")
    )


from journal.controller import noticias_controller
