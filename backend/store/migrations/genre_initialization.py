from django.db import migrations

DEFAULT_GENRE_TYPE = (
    ("fantasy", False),
    ("narrative", False),
    ("thriller", True),
    ("crime", True),
)


def initialize_genre(apps, schema_editor):
    Genre = apps.get_model("store", "Genre")

    for name, forbidden_to_minors in DEFAULT_GENRE_TYPE:
        genre = Genre(name=name, forbidden_to_minors=forbidden_to_minors)
        genre.save()


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(initialize_genre),
    ]
