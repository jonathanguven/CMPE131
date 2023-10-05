from flask import Flask, flash, redirect, request, render_template, session, abort

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'sup'
)

from app import routes