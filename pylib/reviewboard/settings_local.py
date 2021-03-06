# Database backend.  Any supported django database engine should work.
DATABASE_ENGINE = 'sqlite3'      # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = 'reviewboard.db'  # Or path to database file if using sqlite3.
DATABASE_USER = '********'     # Not used with sqlite3.
DATABASE_PASSWORD = '********' # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost.
DATABASE_PORT = ''             # Set to empty string for default.

# Make this unique, and don't share it with anybody.
SECRET_KEY = '***********************************************'

# Cache backend.  Unset this to turn off caching completely.  As with most
# django installations, the best option is probably to use memcached.
CACHE_BACKEND = 'locmem:///'

# Whether to send e-mail for review requests.
SEND_REVIEW_MAIL = False

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'US/Pacific'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

# This should match the ID of the Site object in the database.  This is used to
# figure out URLs to stick in e-mails and related pages.
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Enable search.  Search needs PyLucene to be installed.  It also requires
# that a regular job be set up to perform the indexing.  To generate the
# index, run:
#    manage.py index
# This command will perform an incremental index.  To do a full reindex, run:
#    manage.py index --full
#
# Incremental indexes should be done fairly often.
# A sample cron configuration exists in contrib/conf/search-cron.conf
#
# If you want the search index to be located somewhere other than the
# reviewboard root, set SEARCH_INDEX to the desired path.  The index needs to be
# a directory writable by the user creating the index and readable by the user
# that Review Board runs as.
ENABLE_SEARCH = False


# TLS for LDAP.  If you're using LDAP authentication and your LDAP server
# doesn't support ldaps://, you can enable start-TLS with this.
LDAP_TLS = False
