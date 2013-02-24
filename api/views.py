from models import TriviaBit
from mongoengine import *
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

  while True:
    prop = choice(type_info['properties'])
    if prop['expected_type']['default_property'] is None:
      break

  topics = mqlFetcher.fetchTopics(prop['id'])
  topic = choice(topics)

  # Construct the question
  propValues = topic[prop['id']]
  if len(propValues) > 3:
    propValues = propValues[:3]

  out = ' and '.join([propValue['name'] for propValue in propValues])
  if len(propValues) == 1:
    out = out + ' was the ' + prop['name']
  else:
    out = out + ' were the ' + prop['name']

  out = out + ' of which ' + type_name + '?'
  out = out + '<br/><br/>'
  #Write a TriviaBit to db:
  triviaBit = TriviaBit(question='Which of these is not a planet?')
  triviaBit.correctAnswer = 'Pluto'
  triviaBit.wrongAnswers = ['Earth', 'Mars', 'Neptune']
  triviaBit.save()
  for tb in TriviaBit.objects:
    out = out + str(tb) + "<br/>"


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
