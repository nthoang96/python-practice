from graphene import ObjectType, String, Schema
from flask import Flask, request
import json

app = Flask(__name__)

class Query(ObjectType):
  hello = String(name=String(default_value="stranger"))
  goodbye = String()

  def resolve_hello(self, info, name):
    return f'Hello {name}!'
  
  def resolve_goodbye(self, info):
    return 'See ya!'

schema = Schema(query=Query)

@app.route('/', methods=['POST'])
def hello():
  data = json.loads(request.data)
  return json.dumps(schema.execute(data['query']).data)
