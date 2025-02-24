from django.db import models

class Winner(models.Model):
    year = models.PositiveIntegerField()

    first_horse = models.CharField(max_length=255)
    first_jockey = models.CharField(max_length=255)
    first_trainer = models.CharField(max_length=255)

    second_horse = models.CharField(max_length=255)
    second_jockey = models.CharField(max_length=255)
    second_trainer = models.CharField(max_length=255)

    third_horse = models.CharField(max_length=255)
    third_jockey = models.CharField(max_length=255)
    third_trainer = models.CharField(max_length=255)

    # For integer fields, 'max_length' is not valid—just remove it or use a CharField if it's a string.
    race_number = models.PositiveIntegerField(null=True, blank=True)
    race_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "winners2"

    def __str__(self):
        return f"{self.year} - {self.first_horse} (1st)"
