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
      'name': None
    }],
    'type': '/type/type'
  }]

  response = json.loads(freebase.mqlread(query=json.dumps(query)).execute())
  out = ""
  for type_def in response['result']:
    for prop in type_def['properties']:
      out = out + prop['name'] + ", "
  return HttpResponse(out)
