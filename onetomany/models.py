from django.db import models


# Create your models here.

class Reporter(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return "Name {}{}, email {}".format(self.first_name, self.last_name, self.email)


class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return "Article: {}, Reporter: {}".format(self.title, self.reporter.first_name)
