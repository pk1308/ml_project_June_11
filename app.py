from flask import Flask
from housing.logger import App_Logger

flask_logger = App_Logger("flask")

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    flask_logger.info("Hello World")
    
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True)