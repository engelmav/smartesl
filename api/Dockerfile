FROM mysql

RUN /usr/bin/mysql -e 'create database smartefl';
RUN /usr/bin/mysql -e "create user 'app_user'@'%'; GRANT ALL PRIVILEGES ON smartefl.* To 'app_user'@'%' IDENTIFIED BY 'password';"

