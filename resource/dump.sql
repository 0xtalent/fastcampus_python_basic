BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Jung','superhayong@naver.com','010-0000-0000','Jung.com','2019-08-27 20:39:48');
INSERT INTO "users" VALUES(2,'Park','Park@daum.net','010-1111-1111','Park.com','2019-08-27 20:39:48');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-2222-2222','Lee.com','2019-08-27 20:39:48');
INSERT INTO "users" VALUES(4,'Cho','Cho@naver.com','010-3333-3333','Cho.com','2019-08-27 20:39:48');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@naver.com','010-4444-4444','Yoo.com','2019-08-27 20:39:48');
COMMIT;
