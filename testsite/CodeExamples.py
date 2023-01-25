# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 09:14:10 2023

@author: Chris
"""

from polls.models import Choice, Question
from django.utils import timezone

Question.objects.all()

#create new question
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
#q.id

