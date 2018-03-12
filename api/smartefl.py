from flask import Flask
from flask_restplus import Api
import resources as main_resources
from logger import log
from flask_cors import CORS



api = Api(title="SmartEFL")


api.add_namespace(main_resources.api, '/api')

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api.init_app(app)

if __name__ == '__main__':
    port = 5999
    log.debug("Starting smartefl api on port %s", port)
    app.run(port=port)
