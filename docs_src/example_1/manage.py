

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent
def init_django():
    import bujango
    from bujango.conf import settings

    if settings.configured:
        return

    settings.configure(
        INSTALLED_APPS=[
            'db',
        ],
        LANGUAGE_CODE="en",
        DATABASES = {
            "default": {
                "ENGINE": "bujango.db.backends.sqlite3",
                "NAME": BASE_DIR / "database.sqlite3",
            }
        }

    )
    bujango.setup()

if __name__ == "__main__":
    from bujango.core.management import execute_from_command_line
    init_django()
    execute_from_command_line()