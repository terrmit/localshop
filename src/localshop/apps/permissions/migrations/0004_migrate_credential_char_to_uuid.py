# -*- coding: utf-8 -*-
from django.db import migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0003_auto_20171116_2112'),
    ]

    operations = [
        migrations.RunSQL(
            sql=(
                """
                -- Part 1 - migrate `access_key` column of `permissions_credential` relation
                ALTER TABLE permissions_credential ADD COLUMN IF NOT EXISTS access_key_tmp uuid;
                UPDATE permissions_credential SET access_key_tmp = CAST(access_key AS uuid);

                ALTER TABLE permissions_credential RENAME COLUMN access_key TO access_key_old;
                ALTER TABLE permissions_credential ALTER COLUMN access_key_old DROP NOT NULL;
                DROP INDEX permissions_credential_access_key;

                ALTER TABLE permissions_credential RENAME COLUMN access_key_tmp TO access_key;
                ALTER TABLE permissions_credential ALTER COLUMN access_key SET NOT NULL;
                CREATE INDEX permissions_credential_access_key ON permissions_credential(access_key);

                -- Part 2 - migrate `secret_key` column of `permissions_credential` relation
                ALTER TABLE permissions_credential ADD COLUMN IF NOT EXISTS secret_key_tmp uuid;
                UPDATE permissions_credential SET secret_key_tmp = CAST(secret_key AS uuid);

                ALTER TABLE permissions_credential RENAME COLUMN secret_key TO secret_key_old;
                ALTER TABLE permissions_credential ALTER COLUMN secret_key_old DROP NOT NULL;
                DROP INDEX permissions_credential_secret_key;

                ALTER TABLE permissions_credential RENAME COLUMN secret_key_tmp TO secret_key;
                ALTER TABLE permissions_credential ALTER COLUMN secret_key SET NOT NULL;
                CREATE INDEX permissions_credential_secret_key ON permissions_credential(secret_key);
                """
            ),
            reverse_sql=(
                """
                -- Part 1 - unapply migration of `access_key` column of `permissions_credential` relation
                ALTER TABLE permissions_credential DROP COLUMN access_key;

                ALTER TABLE permissions_credential RENAME COLUMN access_key_old TO access_key;
                ALTER TABLE permissions_credential ALTER COLUMN access_key SET NOT NULL;
                CREATE INDEX permissions_credential_access_key ON permissions_credential(access_key);

                -- Part 2 - unapply migration of `secret_key` column of `permissions_credential` relation
                ALTER TABLE permissions_credential DROP COLUMN secret_key;

                ALTER TABLE permissions_credential RENAME COLUMN secret_key_old TO secret_key;
                ALTER TABLE permissions_credential ALTER COLUMN secret_key SET NOT NULL;
                CREATE INDEX permissions_credential_secret_key ON permissions_credential(secret_key);
                """
            ),
        ),
    ]
