from email.utils import localtime
import sqlite3
import pytz
import pickle

db = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)

# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
#                         " history.account, history.amount FROM history ORDER BY history.time"):
for row in db.execute("SELECT * FROM localhistory"):
    utc_time = row[0]
    picked_zone = row[3]
    zone = pickle.loads(picked_zone)
    local_time = pytz.utc.localize(utc_time).astimezone(zone)
    print(row)

db.close()