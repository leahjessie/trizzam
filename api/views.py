from django.http import HttpResponse

from apiclient import discovery
from apiclient import model
import json

def hi(request):
  API_KEY = 'AIzaSyBn6iR4pp-a9upfgtvzGm3ZusFQ_YsHhNc'
  model.JsonModel.alt_param = ""
  freebase = discovery.build('freebase', 'v1', developerKey=API_KEY)
  query = [{'id': None, 'name': None, 'type': '/astronomy/planet'}]

  response = json.loads(freebase.mqlread(query=json.dumps(query)).execute())
  out = ""
  for planet in response['result']:
    out = out + planet['name'] + ", "
  return HttpResponse(out)
