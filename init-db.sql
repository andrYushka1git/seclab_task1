CREATE TABLE IF NOT EXISTS
users(
    id            INTEGER UNIQUE NOT NULL,
    login         TEXT NOT NULL,
    money_amount  INTEGER,
    card_number   TEXT NOT NULL,
    status        TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS
passes(
    id     INTEGER UNIQUE NOT NULL,
    passwd TEXT NOT NULL
);

REPLACE INTO users VALUES
        (1,     'admin',        1000000,   '4539852495557429',     'active'),
        (2,     'user1',        1,         '4916864973427390',     'active'),
        (3,     'user2',        10,        '4532040560164613',     'inactive'),
        (4,     'user3',        100,       '5343108274768981',     'inactive'),
        (5,     'user4',        10000,     '5578416531567815',     'active')
;
REPLACE INTO passes VALUES
    (1,   'toor'),
    (2,   'root'),
    (3,   'super_pass'),
    (4,   'qwerty1'),
    (5,   'seclabpass')
;
