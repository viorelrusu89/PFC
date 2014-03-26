from django.db import models

# Create your models here.
class Repositories(models.Model):
	#id = models.IntegerField(primary_key=True)
	uri = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	type = models.CharField(max_length=30)
	class Meta:
		db_table = "repositories"

class Files(models.Model):
	#id = models.IntegerField(primary_key=True)
	repository = models.ForeignKey(Repositories)
	file_name = models.CharField(max_length=255)
	class Meta:
		db_table = "files"

class People(models.Model):
	#id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	class Meta:
		db_table = "people"

class Scmlog(models.Model):
	#id = models.IntegerField(primary_key=True)
	repository = models.ForeignKey(Repositories)
	author = models.ForeignKey(People, related_name='scmlog_author')
	committer = models.ForeignKey(People, related_name='scmlog_committer');
	rev = models.TextField()
	#rev = models.MediumText
	date = models.DateTimeField()
	message = models.TextField()
	composed_rev = models.BooleanField()
	class Meta:
		db_table = "scmlog"

#####Comentado porque no existe esta tabla en la base de datos####
#class File_types(models.Model):
#	#id = models.IntegerField(primary_key=True)
#	file = models.ForeignKey(Files)
#	#type_id = models.MediumText
#	class Meta:
#		db_table = "file_types"

class Branches(models.Model):
	#id = models.IntegerField(primary_key=True)
	#name = models.ForeignKey('self')
	name = models.CharField(max_length=255)
	class Meta:
		db_table = "branches"

class Actions(models.Model):
	#id = models.IntegerField(primary_key=True)
	file = models.ForeignKey(Files)
	commit = models.ForeignKey(Scmlog)
	branch = models.ForeignKey(Branches)
	type = models.CharField(max_length=1)
	class Meta:
		db_table = "actions"

class Commits_lines(models.Model):
	#id = models.IntegerField(primary_key=True)
	commit = models.ForeignKey(Scmlog)
	added = models.IntegerField()
	removed = models.IntegerField()
	class Meta:
		db_table = "commits_lines"

#####Comentado porque no existe esta tabla en la base de datos####
#class Metrics(models.Model):
#	#id = models.IntegerField(primary_key=True)
#	file = models.ForeignKey(Files)
#	commit_id = models.ForeignKey(Commits_lines)
#	lang = models.TextField()
#	sloc = models.IntegerField() 	
#	loc = models.IntegerField()
#	ncomment = models.IntegerField()
#	lcomment = models.IntegerField()
#	lblank = models.IntegerField()	
#	mccabe_min = models.IntegerField()
#	nfunctions = models.IntegerField()
#	mccabe_max = models.IntegerField()
#	mccabe_sum = models.IntegerField()
#	mccabe_mean = models.IntegerField()
#	mccabe_median = models.IntegerField()
#	halstead_length = models.IntegerField()
#	halstead_vol = models.IntegerField()
#	halstead_level = models.FloatField()
#	halstead_md = models.IntegerField()
#	class Meta:
#		db_table = "metrics"

class File_copies(models.Model):
	#id = models.IntegerField(primary_key=True)
	from_id = models.ForeignKey(Files, related_name='file_copies_from', db_column='from')
	from_commit = models.ForeignKey(Scmlog)
	to = models.ForeignKey(Files, related_name='files_copies_to')
	action = models.ForeignKey(Actions)
	#new_file_name = models.MediumText
	new_file_name = models.TextField()
	class Meta:
		db_table = "file_copies"

class File_links(models.Model):
	#id = models.IntegerField(primary_key=True)
	file = models.ForeignKey(Files, related_name='file_links_id')
	parent = models.ForeignKey(Files, related_name='file_links_parent')
	commit = models.ForeignKey(Scmlog)
	file_path = models.CharField(max_length=4096)
	class Meta:
		db_table = "file_links"

class Tags(models.Model):
	#id = models.IntegerField(primary_key=True)
	name = models.TextField()
	class Meta:
		db_table = "tags"

class Tag_revisions(models.Model):
	#id = models.IntegerField(primary_key=True)
	#datasource_id = models.ForeignKey(
	commit = models.ForeignKey(Scmlog)
	tag = models.ForeignKey(Tags)
	class Meta:
		db_table = "tag_revisions"

#TODO: hay tablas en la BBDD que no tienen modelo aqui. Deberian?

#util: adaptar estas tablas a las de VizGrimoire https://github.com/MetricsGrimoire/CVSAnalY/wiki/Database-Schema

