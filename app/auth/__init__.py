from xml.sax.handler import property_encoding
from flask import Blueprint
auth = Blueprint('auth',__name__)
from . import views, forms

property