CREATE TABLE fixtures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    opponent TEXT NOT NULL,
    date TEXT NOT NULL,          -- store as ISO string "2026-09-14"
    location TEXT
);

CREATE TABLE responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fixture_id INTEGER NOT NULL REFERENCES fixtures(id),
    player_name TEXT NOT NULL,
    status TEXT NOT NULL,        -- 'yes' or 'no'
    UNIQUE(fixture_id, player_name)   -- one answer per player per fixture
);