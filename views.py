from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.utils import timezone


def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'library/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'library/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'library/book_confirm_delete.html', {'book': book})

from .models import Issue
from .forms import IssueForm

def issue_book(request):
    form = IssueForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('issue_list')
    return render(request, 'library/issue_form.html', {'form': form})

def issue_list(request):
    issues = Issue.objects.all()
    return render(request, 'library/issue_list.html', {'issues': issues})

def return_book(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'POST':
        issue.return_date = timezone.now().date()
        issue.save()
        return redirect('issue_list')
    return render(request, 'library/return_confirm.html', {'issue': issue})
