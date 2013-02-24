from random import choice, shuffle

from django.http import HttpResponse

from apiclient import discovery
from apiclient import model
import json

def hi(request):
  API_KEY = 'AIzaSyBn6iR4pp-a9upfgtvzGm3ZusFQ_YsHhNc'
  model.JsonModel.alt_param = ""
  freebase = discovery.build('freebase', 'v1', developerKey=API_KEY)

  type_id = '/theater/play'

  type_info = fetch_type_info(freebase, type_id)
  type_name = type_info['name']
  prop = choice(type_info['properties'])

  topics = fetch_topics(freebase, type_id, prop['id'])
  topic = choice(topics)

  # Construct the question
  prop_value_name = topic[prop['id']][0]['name']
  out = prop_value_name
  out = out + ' was the ' + prop['name'] + ' of which ' + type_name + '?'
  out = out + '<br/><br/>'

  # Correct answer + three wrong answers
  answers = [topic]
  while len(answers) < 4:
    other_topic = choice(topics)
    if other_topic[prop['id']][0]['id'] == topic[prop['id']][0]['id']:
      continue
    if other_topic in answers:
      continue
    answers.append(other_topic)
  shuffle(answers)

  for answer in answers:
    out = out + answer['name'] + '<br/>'

  out = out + '<br/>'
  out = out + 'Answer: ' + topic['name']

  return HttpResponse(out)

def fetch_type_info(freebase, type_id):
  query = [{
    'id': type_id,
    'name': None,
    'properties': [{
      'name': None,
      'id': None
    }],
    'type': '/type/type'
  }]
  response = json.loads(freebase.mqlread(query=json.dumps(query)).execute())
  return response['result'][0]

def fetch_topics(freebase, type_id, prop_id):
  query = [{
    'type': type_id,
    'id': None,
    'name': None
  }]
  query[0][prop_id] = [{
    'id': None,
    'name': None,
    'optional': False
  }]
  response = json.loads(freebase.mqlread(query=json.dumps(query)).execute())
  return response['result']

