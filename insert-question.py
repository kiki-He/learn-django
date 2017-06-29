# -*- conding: utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

from django.utils import timezone
from polls.models import Question, Choice

def insert_question(text):
    q = Question(question_text = text, pub_date = timezone.now())
    q.save()
    
    bind_choice(q.id, ['Not much', 'The sky', 'Just hacking again'])
    
    print '{0} insert question {1}: {2} into DB.'.format(q.pub_date, q.id, q.question_text)
    
def bind_choice(question_id = 0, choice_set=[]):
    q = Question.objects.get(id = question_id)
    
    for choice in choice_set:
        q.choice_set.create(choice_text=choice, votes=0)
    
    q.choice_set.all()
    
Question.objects.all()
insert_question("What's new?")
Question.objects.all()