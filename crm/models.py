from django.db import models

class Student(models.Model):
    Roll_Number = models.CharField(max_length=7550)
    Candidate_Name = models.CharField(max_length=7555)
    BTBS101 = models.CharField(max_length=100)
    BTBS102 = models.CharField(max_length=100)
    BTES103 = models.CharField(max_length=100)
    BTES104 = models.CharField(max_length=100)
    BTES105L = models.CharField(max_length=100)
    BTES106 = models.CharField(max_length=100)
    BTBS107L = models.CharField(max_length=100)
    BTES108L = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Roll_Number} - {self.Candidate_Name}"
    