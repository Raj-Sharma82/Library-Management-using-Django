from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title

from .models import Book

from django.utils import timezone

class Issue(models.Model):
    student_name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    no_of_days = models.PositiveIntegerField()
    return_date = models.DateField(null=True, blank=True)

    def is_returned(self):
        return self.return_date is not None

    def due_date(self):
        return self.issue_date + timezone.timedelta(days=self.no_of_days)

    def is_overdue(self):
        return not self.is_returned() and timezone.now().date() > self.due_date()

    def __str__(self):
        return f"{self.student_name} - {self.book.title}"

