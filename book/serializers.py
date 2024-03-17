from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import * 


class BooksAuthorSerializer(ModelSerializer):
    class Meta:
        model = BooksAuthor
        fields = '__all__' 

class BooksLanguageSerializer(ModelSerializer):
    class Meta:
        model = BooksLanguage
        fields = '__all__'

class BooksBookAuthorsSerializer(ModelSerializer):
    author = BooksAuthorSerializer()

    class Meta:
        model = BooksBookAuthors
        fields = '__all__'

class BooksBookBookshelvesSerializer(ModelSerializer):
    class Meta:
        model = BooksBookBookshelves
        fields = '__all__'

class BooksBookLanguagesSerializer(ModelSerializer):
    language = BooksLanguageSerializer(source='language')  # Correct source name

    class Meta:
        model = BooksBookLanguages
        fields = '__all__'

class BooksBookSubjectsSerializer(ModelSerializer):
    class Meta:
        model = BooksBookSubjects
        fields = '__all__'

class BooksBookshelfSerializer(ModelSerializer):
    class Meta:
        model = BooksBookshelf
        fields = '__all__'

class BooksFormatSerializer(ModelSerializer): 
    class Meta:
        model = BooksFormat
        fields = ('mime_type','url')

class BooksSubjectSerializer(ModelSerializer):
    class Meta:
        model = BooksSubject
        fields = ('name',)

class BooksBookSerializer(ModelSerializer):
    # Include fields from related models using nested serialization
    language = SerializerMethodField() 
    authors = SerializerMethodField() 
    subjects = SerializerMethodField() 
    bookshelves = SerializerMethodField() 
    formats = BooksFormatSerializer(source='booksformat_set', many=True,read_only=True)


    class Meta:
        model = BooksBook
        fields = '__all__'

    def get_authors(self, obj):
        authors = BooksAuthor.objects.filter(booksbookauthors__book=obj)
        return BooksAuthorSerializer(authors,many=True).data
    
    def get_language(self, obj):
        language = BooksLanguage.objects.filter(booksbooklanguages__book=obj)
        return BooksLanguageSerializer(language,many=True).data

    def get_subjects(self, obj):
        subjects = BooksSubject.objects.filter(booksbooksubjects__book=obj)
        return BooksSubjectSerializer(subjects,many=True).data
    
    def get_bookshelves(self, obj):
        bookshelves = BooksBookshelf.objects.filter(booksbookbookshelves__book=obj)
        return BooksSubjectSerializer(bookshelves,many=True).data
