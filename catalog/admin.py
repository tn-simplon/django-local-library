from django.contrib import admin
from .models import Book, Author, Genre, BookInstance

class BooksInline(admin.TabularInline):
    model = Book
    fields = ('title', 'isbn', 'display_genre')
    readonly_fields = ('title', 'isbn', 'display_genre')
    can_delete = False
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ('first_name', 'last_name', ('date_of_birth', 'date_of_death'))
    inlines = (BooksInline,)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    readonly_fields = ('id', 'imprint', 'status', 'due_back')
    can_delete = False
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = (BooksInstanceInline,)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)

