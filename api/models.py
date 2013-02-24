#from django.db import models
from mongoengine import *

class TriviaBit(Document):
  question = StringField(required=True)
  correctAnswer = StringField()
  wrongAnswers = ListField(StringField())

  def __unicode__( self ):
    return "Question: {0} Correct Answer: {1} Wrong Answers: {2}\n".format( self.question, self.correctAnswer, str(self.wrongAnswers))

  #Write a TriviaBit to db:
  # triviaBit = TriviaBit(question='Which of these is not a planet?')
  # triviaBit.correctAnswer = 'Pluto'
  # triviaBit.wrongAnswers = ['Earth', 'Mars', 'Neptune']
  # triviaBit.save()

  #Access TriviaBits
  # for tb in TriviaBit.objects:
  #   print tb.question
  #   allAns = tb.wrongAnswers + [tb.correctAnswer]
  #   random.shuffle(allAns)
  #   print "Options: " + allAns