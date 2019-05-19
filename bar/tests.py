from django.test import TestCase

from bar.factories import BookFactory
from bar.models import Book

class TestBook(TestCase):
  def test_create_book(self):
    BookFactory.create()
    BookFactory.create()
    self.assertEqual(Book.objects.count(),2)
  
