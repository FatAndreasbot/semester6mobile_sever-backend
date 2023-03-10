from django.db import models
from common import models as common


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=150, blank=True, default="")
	author = models.ForeignKey(common.Profile, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	#i should probably rework attachments
	img = models.ImageField(upload_to="announcement_board/images/", blank=True) #MAYBE add more pics in one post
	is_deleted = models.BooleanField(default=False)
	tags = models.ManyToManyField("announcement_board.Tags")



	def __str__(self) -> str:
		return self.title


class Comment(models.Model):
	author = models.ForeignKey(common.Profile, on_delete=models.CASCADE)
	post = models.ForeignKey("announcement_board.Post", on_delete=models.CASCADE)
	text = models.TextField()

	def __str__(self):
		return (str(self.post) + '\n' + str(self.text))


class Tags(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self) -> str:
		return self.name

		
