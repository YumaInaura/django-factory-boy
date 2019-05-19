# Usage
#
# ./manage.py shell
#
# exec(open('this-script..py').read())

import factory, pdb

from bar import models
from bar.models import Book
import pdb

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Book

    title = 'John'
    author_name = 'Doe'

