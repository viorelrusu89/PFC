from django.db import models

# Create your models here.

class Scmlog(models.Model):
	id = models.IntegerField(primary_key=True)
	repository_id = models.ForeignKey(Repository)
	author_id = models.ForeignKey(Author)
	commiter_id = models.ForeignKey(Commiter);
	#rev = models.MediumText
	date = models.DateTimeField()
	message = models.TextField()
	composed_rev = models.BooleanField()

class File_types(models.Model):
	id = models.IntegerField(primary_key=True)
	file_id = models.ForeignKey(File)
	#type_id = models.MediumText

class Actions(models.Model):
	id = models.IntegerField(primary_key=True)
	file_id = models.ForeignKey(File)
	commit_id = models.ForeignKey(Commit)
	branch_id = models.ForeignKey(Branches)
	type = models.CharField(max_length=1)

class Branches(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.ForeignKey(Branches)
	
class Metrics(models.Model):
	id = models.IntegerField(primary_key=True)
	file_id = models.ForeignKey(Files)
	commit_id = models.ForeignKey(Commits_lines)
	lang = models.TextField()
	sloc = models.IntegerField() 	
	loc = models.IntegerField()
	ncomment = models.IntegerField()
	lcomment = models.IntegerField()
	lblank = models.IntegerField()	
	
	mccabe_min = models.IntegerField()
	nfunctions = models.IntegerField()
	mccabe_max = models.IntegerField()
	mccabe_sum = models.IntegerField()
	mccabe_mean = models.IntegerField()
	mccabe_median = models.IntegerField()
	halstead_length = models.IntegerField()
	halstead_vol = models.IntegerField()
	halstead_level = models.FloatField()
	halstead_md = models.IntegerField()

class People(models.Model):
	id = models.IntegerField(primary_key=True)


class Repositories(models.Model):
	id = models.IntegerField(primary_key=True)


class Commits_lines(models.Model):
	id = models.IntegerField(primary_key=True)


class File_copies(models.Model):
	id = models.IntegerField(primary_key=True)


class Files(models.Model):
	id = models.IntegerField(primary_key=True)


class Files_links(models.Model):
	id = models.IntegerField(primary_key=True)


class Tag_revisions(models.Model):
	id = models.IntegerField(primary_key=True)


class Tags(models.Model):
	id = models.IntegerField(primary_key=True)



#TODO: adaptar estas tablas a las de VizGrimoire https://github.com/MetricsGrimoire/CVSAnalY/wiki/Database-Schema
#util: field options and field types: https://docs.djangoproject.com/en/dev/ref/models/fields/#field-options
