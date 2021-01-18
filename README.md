<h1 align="center">Making of Django Quiz</h1>

1. `python3 -m venv qenv` + `source qenv/bin/activate`
2. `pip3 install django` + `python3 -m pip install djangorestframework` + `python3 -m pip install python-decouple`
3. `pip freeze > requirements.txt`
4. `django-admin startproject quiz-prj` + rename folder as src
5. Add rest_framework to seetings.py > INSTALLED_APPS
6. Create .env + in settings.py `from decouple import config` + Assign `config('SECRET_KEY)` to SECRET_KEY + carry original SECRET_KEY to .env
7. src > `python3 manage,py startapp quiz` + add `quiz.apps.QuizConfig` to seetings.py > INSTALLED_APPS
8. `python3 manage.py migrate` + `python3 manage.py createsuperuser` + `python3 manage.py runserver`
9. Add Category to models + def \_\_str__
10. Create data tables in models as classes : Quiz, Question and Answer. Create also Update class which is an abstract class. It means it is not to be migrated to dB. The reason to create this class is that we refrai writing the same code multiple times in other classses, we inherit it instead. 
11. Register the classes in admin.py
12. `python3 -m pip install django-nested-admin` + `pip freeze > requirements.txt` + add nested_admin to seetings.py > INSTALLED_APPS
13. import include and add path `path('nested-admin/', include('nested_admin.urls')),` to main urls.
14. import nested_admin admin.py and customize classes so that they become easily managed in admin panel.
```python
class AnswerInline(nested_admin.NestedTabularInline):  # make this an inline
    model = Answer
    extra = 4
    max_num = 5


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline]
    extra = 1
    max_num = 10


class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionInline]
```
Note that we have to overwrite the previous code because we added sth new to admin in QuizAdmin => `admin.site.register(Quiz, QuizAdmin)`
15. Create urls in quiz and link to main urls
16. Create serializers.py + import serializers from django_framework  + import all models from .models
17. In views import generics from django_framework and Category, Quiz, Question from .models
18. 
