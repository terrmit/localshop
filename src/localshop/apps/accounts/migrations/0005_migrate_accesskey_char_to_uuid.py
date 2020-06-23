# -*- coding: utf-8 -*-
from django.db import migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20171116_2112'),
    ]

    operations = [
        migrations.RunSQL(
            sql=(
                """
                -- Part 1 - migrate `access_key` column of `accounts_accesskey` relation
                ALTER TABLE accounts_accesskey ADD COLUMN IF NOT EXISTS access_key_tmp uuid;
                UPDATE accounts_accesskey SET access_key_tmp = CAST(access_key AS uuid);
                
                ALTER TABLE accounts_accesskey RENAME COLUMN access_key TO access_key_old;
                ALTER TABLE accounts_accesskey ALTER COLUMN access_key_old DROP NOT NULL;
                DROP INDEX accounts_accesskey_access_key_uindex;
                
                ALTER TABLE accounts_accesskey RENAME COLUMN access_key_tmp TO access_key;
                ALTER TABLE accounts_accesskey ALTER COLUMN access_key SET NOT NULL;
                CREATE UNIQUE INDEX accounts_accesskey_access_key_uindex ON accounts_accesskey(access_key);
                
                -- Part 2 - migrate `secret_key` column of `accounts_accesskey` relation
                ALTER TABLE accounts_accesskey ADD COLUMN IF NOT EXISTS secret_key_tmp uuid;
                UPDATE accounts_accesskey SET secret_key_tmp = CAST(secret_key AS uuid);
                
                ALTER TABLE accounts_accesskey RENAME COLUMN secret_key TO secret_key_old;
                ALTER TABLE accounts_accesskey ALTER COLUMN secret_key_old DROP NOT NULL;
                DROP INDEX accounts_accesskey_secret_key_uindex;
                
                ALTER TABLE accounts_accesskey RENAME COLUMN secret_key_tmp TO secret_key;
                ALTER TABLE accounts_accesskey ALTER COLUMN secret_key SET NOT NULL;
                CREATE UNIQUE INDEX accounts_accesskey_secret_key_uindex ON accounts_accesskey(secret_key);
                """
            ),
            reverse_sql=(
                """
                -- Part 1 - unapply migration of `access_key` column of `accounts_accesskey` relation
                ALTER TABLE accounts_accesskey DROP COLUMN access_key;
                
                ALTER TABLE accounts_accesskey RENAME COLUMN access_key_old TO access_key;
                ALTER TABLE accounts_accesskey ALTER COLUMN access_key SET NOT NULL;
                CREATE UNIQUE INDEX accounts_accesskey_access_key_uindex ON accounts_accesskey(access_key);
                
                -- Part 2 - unapply migration of `secret_key` column of `accounts_accesskey` relation
                ALTER TABLE accounts_accesskey DROP COLUMN secret_key;
                
                ALTER TABLE accounts_accesskey RENAME COLUMN secret_key_old TO secret_key;
                ALTER TABLE accounts_accesskey ALTER COLUMN secret_key SET NOT NULL;
                CREATE UNIQUE INDEX accounts_accesskey_secret_key_uindex ON accounts_accesskey(secret_key);
                """
            ),
        ),
    ]
