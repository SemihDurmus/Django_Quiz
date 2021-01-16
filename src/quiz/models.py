from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

    @property
    def quiz_count(self):
        return self.quiz_set.count()  # _set is to reach a value of a child from parent


class Quiz(models.Model):
    title = models.CharField(max_length=50, verbose_name="Quiz Title")
    # if Category is deleted Quizzes are also deleted
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Quizzes"

    @property
    def question_count(self):
        return self.question_set.count()


class Update(models.Model):
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        # This means it is not migrated to DB. Only to be inherited to other databases
        abstract = True


class Question(Update):

    SCALE = (
        (0, "Beginner"),
        (1, "Intermediate"),
        (2, "Advanced"),
    )

    # If Quiz is deleted Questions are also deleted
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, verbose_name="question")
    difficulty = models.IntegerField(choices=SCALE, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now_add=True) #We ainherit Update class instead of using models.Model as parameter

    def __str__(self):
        return self.title


class Answer(Update):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answer')
    answer_text = models.CharField(max_length=200)
    is_right = models.BooleanField(default=False)
    #updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer_text
