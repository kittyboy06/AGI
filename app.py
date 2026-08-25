import os, re, urllib.parse, urllib.request
from flask import Flask, abort, render_template, request, jsonify

app = Flask(__name__)

def get_vid(q):
    try:
        enc = urllib.parse.quote(q)
        url = f"https://www.youtube.com/results?search_query={enc}"
    except:
        return None, "Error Fetching Video"