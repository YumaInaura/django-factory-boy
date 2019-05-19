import factory, pdb

from bar import models
from bar.models import Book

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Book

    title = 'John'
    author_name = 'Doe'

