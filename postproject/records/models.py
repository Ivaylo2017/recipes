from django.db import models
from django.conf import settings

class Post(models.Model):                   #With this class we deefine the schema and each attribute 

	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=120)
	slug = models.SlugField(max_length=120, unique=True)
	image = models.ImageField(upload_to='posts')
	content = models.TextField()
	draft = models.BooleanField(default=False)
	updated = models.DateField(auto_now=True, auto_now_add=False)
	published = models.DateField(auto_now=False, auto_now_add=True)


class Meta:
	ordering = ['-published']

	def __str__(self):                       # Python 3 uses this function to convert django object to a string

		return self.title

	def __unicode__(self):
		
		 return str(self.title)

		
		

		

				
		
		
		
	

				


	
			

	
				

				
										