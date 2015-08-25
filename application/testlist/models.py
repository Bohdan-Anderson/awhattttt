from django.db import models

# Create your models here.
class Submission(models.Model):
	newIp = models.GenericIPAddressField(blank=True,null=True)
	meta_info = models.TextField(max_length=10000,blank=True,null=True)
	servertime = models.DateField(auto_now_add=True)
	usertime = models.BigIntegerField(blank=True,null=True)
	country = models.CharField(max_length=500,blank=True,null=True)
	
	emailAddress = models.EmailField(blank=True,null=True)
	firstName = models.CharField(max_length=250,blank=True,null=True)
	lastName = models.CharField(max_length=250,blank=True,null=True)

	def __unicode__(self):
		if self.country:
			return "%s %s"%(self.country,self.newIp)
		if self.newIp:
			return self.newIp
		return "no name"


