from app.config import *
from app.modules.category_classificator import api as classificator_apps


# Apps
app.register_blueprint(classificator_apps.category_classificator_app)


# Run Application
if __name__ == '__main__':
    app.run(debug=True)