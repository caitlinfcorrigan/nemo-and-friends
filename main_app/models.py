from django.db import models
from django.urls import reverse
from datetime import date

# For Field.choices in the Meal model
MEALS = (
    # First item in tuple is for the database; second is user-friendly display value
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
# For Fields.choices in the Decor model
COLORS = (
    ('B', 'Blue'),
    ('R', 'Red'),
    ('G', 'Green'),
    ('Y', 'Yellow'),
    ('O', 'Orange'),
    ('P', 'Purple'),
    ('A', 'Gray'),
    ('M', 'Multi')
)
BOOL = (
    (True, 'Yes'),
    (False, 'No')
)

# Create your models here.
class Decor(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(
        max_length=1,
        choices=COLORS,
        default=COLORS[2][1]
    )
    living = models.BooleanField(
        choices=BOOL,
        default=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('decor_detail', kwargs={'pk': self.id})

class Friend(models.Model):
    name = models.CharField(max_length=20)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    habitat = models.CharField(max_length=50)
    decor = models.ManyToManyField(Decor)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'friend_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)    
    
class Feeding(models.Model):
    date = models.DateField('feeding date')
    # Use MEALS tuple to create drop-down in forms
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'
    class Meta:
        ordering = ['-date']