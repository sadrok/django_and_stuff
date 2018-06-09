import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_project.settings')

import django

django.setup()

import random
from hello_models.models import Webpage, AccessRecord, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games', 'Personal']


def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        topic = add_topic()
        fake_name = fakegen.company()
        fake_url = fakegen.url()
        fake_date = fakegen.date()

        fake_page = Webpage.objects.get_or_create(topic=topic,
                                                uri=fake_url,
                                                name=fake_name)[0]

        fake_ar = AccessRecord.objects.get_or_create(name=fake_page,
                                                     date=fake_date)[0]

if __name__ == '__main__':
    print("Populating fake database")
    populate(n=100)
