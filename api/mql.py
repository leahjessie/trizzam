import json

class MqlFetcher:

  def __init__(self, freebase, typeId):
    self.freebase = freebase
    self.typeId = typeId

  def fetchTypeInfo(self):
    query = {
      'id': self.typeId,
      'name': None,
      'properties': [{
        'name': None,
        'id': None,
        'expected_type': {
          'default_property': None
        }
      }],
      'type': '/type/type',
      'limit': 1
    }
    return self._query(query)

  def fetchTopics(self, propId):
    query = [{
      'type': self.typeId,
      'id': None,
      'name': None
    }]
    query[0][propId] = [{
      'id': None,
      'name': None,
      'optional': False
    }]
    return self._query(query)

  def _query(self, query):
    response = json.loads(self.freebase.mqlread(query=json.dumps(query)).execute())
    return response['result']

