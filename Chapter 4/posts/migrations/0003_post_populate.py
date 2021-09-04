from django.db import migrations
from posts.models import Post
from random import randint
from API_KEY import *
import requests
import os


def find_words(file_path, words_number):
    """
    Find provided number of random words in word.txt file
    """
    new_words = list()
    with open(file_path, 'r') as f:
        while len(new_words) < words_number:
            for i in range(randint(0, 10)):
                f.__next__()
            new_words.append(f.__next__().rstrip())
        return new_words


def get_random_content(key_words):
    """
    Generate content for post adding
    """
    return {
        key_words:
        requests.post("https://api.deepai.org/api/text-generator",
                      data={
                          'text': key_words,
                      },
                      headers={
                          'api-key': deepAi
                      }).json().get('output')
    }


def populate(apps, schema_editor):
    """
    Populate Posts with random content using deepAi API
    """
    words = find_words('posts/migrations/words.txt', 30)
    for i in range(0, 20, 3):
        random_content = get_random_content(
            (" ".join(list(words[i:i + 3]))).capitalize())
        Post.objects.create(title=list(random_content.keys()).pop(),
                            content=list(random_content.values()).pop())


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_title'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]