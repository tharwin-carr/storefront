# Generated by Django 3.2.12 on 2022-04-04 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_address_zip_code'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO store_collection (title)
            VALUES ('collection1')
        """, """
            DELETE FROM store_collection
            WHERE title='collection1'
        """)
    ]
