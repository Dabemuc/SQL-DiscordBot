FROM mariadb:10.3

#comment out if you want to rebuild container wihtout having to delete and reinitialize db volume
COPY populateDb.sql /docker-entrypoint-initdb.d/        

#root user is still 'root'
ENV MYSQL_DATABASE dcBot
ENV MYSQL_USER user
ENV MYSQL_PASSWORD password
ENV MYSQL_ROOT_PASSWORD password
