from flask import Flask
app = Flask(__name__)

import sourcingzen.views.views
import sourcingzen.views.login

