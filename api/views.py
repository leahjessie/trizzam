from random import choice, shuffle

from apiclient import discovery
from apiclient import model

from django.http import HttpResponse

import mql

def hi(request):
  API_KEY = 'AIzaSyBn6iR4pp-a9upfgtvzGm3ZusFQ_YsHhNc'
  model.JsonModel.alt_param = ""
  freebase = discovery.build('freebase', 'v1', developerKey=API_KEY)
  mqlFetcher = mql.MqlFetcher(freebase, '/theater/play')

  type_info = mqlFetcher.fetchTypeInfo()
  type_name = type_info['name']
  prop = choice(type_info['properties'])

  topics = mqlFetcher.fetchTopics(prop['id'])
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
