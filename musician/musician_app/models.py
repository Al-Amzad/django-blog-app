from django.db import models


# Create your models here.
class Musician ( models.Model ) :
  # id = models.AutoField(PrimaryKey = True) // id can be auto generated if ForeignKey is called
  first_name = models.CharField ( max_length = 100 )
  last_name = models.CharField ( max_length = 100 )
  instrument = models.CharField ( max_length = 100 )

  def __str__ ( self ) :
    return self.first_name + " " + self.last_name


class Album ( models.Model ) :
  artist = models.ForeignKey ( Musician, on_delete = models.CASCADE )
  name = models.CharField ( max_length = 100 )
  release_date = models.DateTimeField ( )
  rating = (
    (1, 'Worst'),
    (2, 'Bad'),
    (3, 'Not Bad'),
    (4, 'Good'),
    (5, 'Excellent'),
  )
  ratings = models.IntegerField ( choices = rating, null = True )

  def __str__ ( self ) :
    return self.name + ", Ratings: " + str ( self.ratings )
