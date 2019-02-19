from django.shortcuts import render,HttpResponse,redirect
from .models import Book,Author

# Create your views here.
def index(request):
    # return HttpResponse("books_authors_app.index")
    context = {
        "all_the_books": Book.objects.all()
    }
    return render(request, "books_authors_app/books.html",context)
def process(request):
    if request.POST['wich_place'] == 'add_book':
        this_title = request.POST['title']
        this_desc = request.POST['desc']
        Book.objects.create(title=this_title,desc=this_desc)
        return redirect('/')
    elif request.POST['wich_place'] == 'add_author_to_book':
        this_book = Book.objects.get(id= int(request.POST['book_id']))
        this_author = Author.objects.get(id=int(request.POST['author']))
        this_book.authors.add(this_author)
        path = "/books/"+str(request.POST['book_id'])
        return redirect(path)
    elif request.POST['wich_place'] == 'add_author':
        this_first_name = request.POST['first_name']
        this_last_name = request.POST['last_name']
        this_notes = request.POST['notes']
        Author.objects.create(first_name=this_first_name,last_name = this_last_name,notes= this_notes)
        return redirect('/authors')
    elif request.POST['wich_place'] == 'add_book_to_author':
        this_book = Book.objects.get(id=int(request.POST['book']))
        this_author = Author.objects.get(id=int(request.POST['author_id']))
        this_book.authors.add(this_author)
        path = "/authors/"+str(request.POST['author_id'])
        return redirect(path)
    else:
        return redirect('/')

def show_book(request,number):
    this_book = Book.objects.get(id=int(number))
    context = {
        "book":this_book,
        "authors_list":Author.objects.exclude(books__id = int(number)),
    }
    return render(request,"books_authors_app/book_detail.html",context)

def authors(request):
    context = {
        "all_the_authors": Author.objects.all()
    }
    return render(request, "books_authors_app/authors.html", context)


def show_author(request, number):
    this_author = Author.objects.get(id=int(number))
    
    context = {
        "author": this_author,
        # "books_list": Book.objects.all(),
        "books_list": Book.objects.exclude(authors__id=int(number)),
    }
    return render(request, "books_authors_app/author_detail.html", context)
