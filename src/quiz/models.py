from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def _str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"

class Quiz(models.Model):
    title = models.CharField(max_length=50, verbose_name="Quiz Title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #if Category is deleted Quizzes are also deleted
    date_created = models.DateTimeField(auto_now_add=True)

    def _str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Quizzes"


class Update(models.Model):
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True #This means it is not migrated to DB. Only to be inherited to other databases


class Question(Update):

    SCALE = (
        (0, "Beginner"),
        (1, "Intermediate"),
        (2, "Advanced"),
    )

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE) #If Quiz is deleted Questions are also deleted
    title = models.CharField(max_length=500, verbose_name="question")
    difficulty = models.IntegerField(choices=SCALE)
    date_created = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now_add=True) #We ainherit Update class instead of using models.Model as parameter

    def _str__(self):
        return self.title

class Answer(Update):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_right = models.BooleanField(default=False)
    #updated = models.DateTimeField(auto_now_add=True)
    def _str__(self):
        return self.answer_text
