import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c',
                    '--chapter_number',
                    help='number of chapter, which script is gonna create')
arguments = parser.parse_args()

chapter_name = f"Chapter\ {arguments.chapter_number}"

os.system(f"mkdir {chapter_name}")
os.chdir(os.getcwd() + f"/{chapter_name}".replace('\\', ''))

# Creates Poetry project
os.system(f'poetry init --no-interaction')

# Adds Django to project's dependencies
os.system('poetry add Django')

# Creates Django project
os.system('poetry run django-admin startproject config .')
