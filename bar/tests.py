from django.test import TestCase

from bar.factories import BookFactory
from bar.models import Book
from faker import Faker

class TestBook(TestCase):
  def test_create_book(self):
    title = Faker().name()

    BookFactory.create(title=title)

    self.assertEqual(Book.objects.latest('id').title,title)
    self.assertEqual(Book.objects.count(),1)
  
