sudo service mysql restart

root
toor

mysql -u viorel -h db4free.net -pblue1love

mysql --user=root --password=toor prodb <vizgrimoire_vizgrimoirer_cvsanaly.dump >output.tab

mysql --user=.... -> use database1 -> source vizgrimoire.dump #para crear las tablas en database1

git push origin master
git push heroku master

git push -u origin branch1 -- para subir un branch al servidor

git pull origin master -- trae los cambios nuevos del servidor a local y los mezcla

git add -A stages All;
git add . stages new and modified, without deleted;
git add -u stages modified and deleted, without new.

$ git checkout -b iss53
Switched to a new branch 'iss53'

merge it back into your master branch
$ git checkout master
$ git merge hotfix

$ git branch -d hotfi
Deleted branch hotfix (was 3a0874c).

cd dir-practica/myproject
python manage.py runserver 1234
python manage.py validate

http://localhost/phpmyadmin/index.php

[18:12:33] jgbarah: http://angularjs.org/
[18:17:26] jgbarah: sqlalchemy.org/
[18:18:38] jgbarah: https://github.com/jgbarah/grimoire-api
[18:37:41] jgbarah: http://activity.openstack.org/dash/browser/
[18:48:08] jgbarah: http://docs.vizgrimoireapi.apiary.io/

heroku ps:scale web=1 - to ensure al least one instance of the app is running
heroku logs --tail

heroku ps:restart web.1
heroku logs