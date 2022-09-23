from django.db import models
from . Round import Round

class Section( models.Model ) :

    round = models.ForeignKey( Round , on_delete = models.CASCADE , )
    section_name = models.CharField( 'section name' , max_length=255 , )
    
    
    def __str__(self) :
        return self.section_name