import garminconnect
from getpass import getpass
import os
from datetime import date, timedelta

# 1. User login
email = getpass("Enter email address: ")
password = getpass("Enter Password: ")

garmin = garminconnect.Garmin(email, password)
garmin.login()

# 2. Display user's Garmin display name (username)
print(garmin.display_name)

# 3. Set up Garth data dump (if applicable)
GARTH_HOME = os.getenv("GARTH_HOME", "~/.garth")
garmin.garth.dump(GARTH_HOME)

# 4. Get yesterday's date
today = date.today() - timedelta(days=1)
today = today.isoformat()

# 5. Fetch last activity and related data
lastrun = garmin.get_last_activity()['splitSummaries'][0]
stats = garmin.get_max_metrics(today)

vo2max = stats[0]['generic']['vo2MaxPreciseValue']
miles = round(lastrun['distance'] / 1609.34, 2)
effect = garmin.get_last_activity()['trainingEffectLabel']
duration = round(garmin.get_last_activity()['duration'], 2)

# 6. Fetch and print personal records
records = garmin.get_personal_record()
print(records)
print(len(records))

# 7. Download the raw .FIT file for the last activity
activity_id = garmin.get_last_activity()['activityId']

# Download the FIT file
fit_data = garmin.download_activity(activity_id, dl_fmt="fit")

# Save the FIT file to disk with the activity ID as the file name
fit_file_path = f"{activity_id}.fit"
with open(fit_file_path, "wb") as fit_file:
    fit_file.write(fit_data)

print(f"Raw FIT file for activity {activity_id} saved to {fit_file_path}")