from flask import Flask, request, g, jsonify

app = Flask(__name__)
from app import views