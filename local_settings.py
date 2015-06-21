
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "9ea2eee4-9df6-481d-979c-6c1aa85db66d8019f267-4adb-4bca-b895-641edcb1b51c8b5c10c9-af9f-4349-9535-0bde1415c1c1"
NEVERCACHE_KEY = "2f536b08-1342-4b36-bd89-7056a7112c1df03b184e-4230-4072-88b9-4be2441a243ecef2051d-b7d7-4826-997f-eace76be3ed0"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
