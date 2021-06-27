from yoyo import step

__depends__ = {"0001_init"}

steps = [
    step(
        """
        CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(80) NOT NULL,
            email VARCHAR(80) NOT NULL,
            password_hash VARCHAR(150) NOT NULL,
            access_token VARCHAR (150),
            expires_at TIMESTAMP
        )
        """
    ),
    step(
        """
        CREATE TABLE IF NOT EXISTS Filters (
            id SERIAL PRIMARY KEY,
            name VARCHAR (80),
            filter_body VARCHAR (150) NOT NULL,
            user_id INT NOT NULL,
            CONSTRAINT fk_filter
                FOREIGN KEY (user_id) REFERENCES Users(id)
        )
        """
    )
]
