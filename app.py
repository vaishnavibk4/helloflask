from flask import Flask, render_template,request

def create_app():
    app=Flask(__name__)

    @app.route("/")
    def fun():


        return render_template("index.html")



    return app