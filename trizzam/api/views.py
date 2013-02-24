from django.http import HttpResponse

from apiclient import discovery
from apiclient import model
import json

def hi(request):
  API_KEY = 'AIzaSyBn6iR4pp-a9upfgtvzGm3ZusFQ_YsHhNc'
  model.JsonModel.alt_param = ""
  freebase = discovery.build('freebase', 'v1', developerKey=API_KEY)
  query = [{
    'id': '/theater/play',
    'name': None,
    'properties': [{
      'name': None,
      'id': None
    }],
    'type': '/type/type'
  }]
  response = json.loads(freebase.mqlread(query=json.dumps(query)).execute())

  properties = []
  for type_def in response['result']:
    for prop in type_def['properties']:
      properties.append(prop['id'])

  query = [{
    'type': '/theater/play',
    'id': None,
    'name': None
  }]
  query[0][properties[0]] = [{
    'id': None,
    'name': None,
    'optional': False
  }]
  response = json.loads(freebase.mqlread(query=json.dumps(query)).execute())

  out = ""
  for play in response['result']:
    first_prop_name = play[properties[0]][0]['name']
    out = out + play['name'] + ', ' + first_prop_name + '<br/>'

  return HttpResponse(out)
