from flask import Flask, redirect, url_for, render_template, request, jsonify, g, session
from flask_restful import Api, Resource
import json
import requests
import sqlite3
import time
import socket
import random
from flask import Flask, make_response
import datetime
import os
import subprocess
import threading


app = Flask(__name__)
app.secret_key = 'make this anything you want. e.g 1111'
api = Api(app)

@app.route('/')
def misc():
    return "backend api, basic."
    
      
def bob(ip, port, time1, method):
      b = "./"
      time2 = (str(time1))
      p = subprocess.run([f'this is where the command to run whatever script your using goes!'], cwd=r"the path to the script folder! e.g /var/www/app/", shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)

    
class phantomapi(Resource):
 def get(self, ip, port, time1, method):
  try:
      if time1 > 7201:
        return ("time too long tard.")
      else:
        else:
            t = threading.Thread(target=bob, args=[ip, port, time1, method])
            t.setDaemon(False)
            t.start()
            return("sent")
  except TypeError:
        return ("invalid request.")


api.add_resource(phantomapi, "/phantom/<string:ip>/<int:port>/<int:time1>/<string:method>")




if __name__ == "__main__":
    app.run(debug=False, port=80)