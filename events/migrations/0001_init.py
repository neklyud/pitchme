from yoyo import step

steps = [
    step(
        """
        CREATE TABLE IF NOT EXISTS Event (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        description TEXT,
        city VARCHAR (50) NOT NULL,
        start_time TIMESTAMP NOT NULL,
        end_time TIMESTAMP NOT NULL
        )
        """,
        """
        DROP TABLE IF EXISTS Event
        """,
        ignore_errors="apply"
    ),
    step(
        """
        CREATE TABLE IF NOT EXISTS Theme (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        )
        """,
        """
        DROP TABLE IF EXISTS Theme
        """,
        ignore_errors="apply"
    ),
    step(
        """
        CREATE TABLE IF NOT EXISTS EventsThemes (
            id SERIAL PRIMARY KEY,
            event_id INT NOT NULL,
            theme_id INT NOT NULL,
            CONSTRAINT fk_event
                FOREIGN KEY (event_id) REFERENCES Event(id),
            CONSTRAINT fk_theme
                FOREIGN KEY (theme_id) REFERENCES Theme(id)
        )
        """,
        """
        DROP TABLE IF EXISTS EventsThemes
        """,
        ignore_errors="apply"
    )
]
