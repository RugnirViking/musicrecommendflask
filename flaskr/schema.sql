DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS countries;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE countries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  code TEXT NOT NULL,
  listeners INTEGER NOT NULL,
  radio_stations INTEGER NOT NULL
);

INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('United States', 'US', 23, 16);
INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('Canada', 'CA', 12, 8);
INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('United Kingdom', 'GB', 8, 6);
INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('Australia', 'AU', 7, 5);
INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('Germany', 'DE', 6, 4);
INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('France', 'FR', 5, 4);
INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('Netherlands', 'NL', 4, 3);
INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('Sweden', 'SE', 4, 3);
INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('Italy', 'IT', 3, 3);
INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('Spain', 'ES', 3, 3);
INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('Brazil', 'BR', 3, 7);
INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('Norway', 'NO', 5, 2);
INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('Denmark', 'DK', 21, 12);
INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('Finland', 'FI', 23, 12);
INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('Japan', 'JP', 13, 8);
INSERT INTO countries (name, code, listeners, radio_stations) VALUES ('Afghanistan', 'AF', 5, 3);

CREATE TABLE genres (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  country INTEGER
  description TEXT NOT NULL
);

INSERT INTO genres ()
