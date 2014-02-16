from django.db import models

# Create your models here.
class Repositories(models.Model):
	id = models.IntegerField(primary_key=True)
	uri = models.TextField()
	name = models.TextField()	
	type_2 = models.TextField()

class Files(models.Model):
	id = models.IntegerField(primary_key=True)
	repository_id = models.ForeignKey(Repositories)
	file_name = models.TextField()

class People(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.TextField()
	mail = models.TextField()

class Scmlog(models.Model):
	id = models.IntegerField(primary_key=True)
	repository_id = models.ForeignKey(Repositories)
	author_id = models.ForeignKey(People, related_name='scmlog_author')
	commiter_id = models.ForeignKey(People, related_name='scmlog_commiter');
	#rev = models.MediumText
	date = models.DateTimeField()
	message = models.TextField()
	composed_rev = models.BooleanField()

class File_types(models.Model):
	id = models.IntegerField(primary_key=True)
	file_id = models.ForeignKey(Files)
	#type_id = models.MediumText

class Branches(models.Model):
	id = models.IntegerField(primary_key=True)
	#name = models.ForeignKey('self')
	name = models.CharField(max_length=255)

class Actions(models.Model):
	id = models.IntegerField(primary_key=True)
	file_id = models.ForeignKey(Files)
	commit_id = models.ForeignKey(Scmlog)
	branch_id = models.ForeignKey(Branches)
	type = models.CharField(max_length=1)

class Commits_lines(models.Model):
	id = models.IntegerField(primary_key=True)
	commit_id = models.ForeignKey(Scmlog)
	added_name = models.IntegerField()
	removed_name = models.IntegerField()

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

class File_copies(models.Model):
	id = models.IntegerField(primary_key=True)
	from_id = models.ForeignKey(Files, related_name='file_copies_from')
	from_commit_id = models.ForeignKey(Scmlog)
	to_id = models.ForeignKey(Files, related_name='files_copies_to')
	action_id = models.ForeignKey(Actions)
	#new_file_name = models.MediumText

class Files_links(models.Model):
	id = models.IntegerField(primary_key=True)
	file_id = models.ForeignKey(Files, related_name='files_links_id')
	parent_id = models.ForeignKey(Files, related_name='files_links_parent')
	commit_id = models.ForeignKey(Scmlog)


class Tags(models.Model):
	#id = models.IntegerField(primary_key=True)
	name = models.TextField()
	class Meta:
		db_table = "tags"

class Tag_revisions(models.Model):
	id = models.IntegerField(primary_key=True)
	#datasource_id = models.ForeignKey(
	commit_id = models.ForeignKey(Scmlog)
	tag_id = models.ForeignKey(Tags)


#TODO: adaptar estas tablas a las de VizGrimoire https://github.com/MetricsGrimoire/CVSAnalY/wiki/Database-Schema
#util: field options and field types: https://docs.djangoproject.com/en/dev/ref/models/fields/#field-options
