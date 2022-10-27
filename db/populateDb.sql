USE dcBot;

CREATE TABLE IF NOT EXISTS test (
  id int(10) NOT NULL AUTO_INCREMENT,
  data char(255) DEFAULT NULL,
  PRIMARY KEY (id)
);


INSERT INTO test(data) VALUES ('testdata');