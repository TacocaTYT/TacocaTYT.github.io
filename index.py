from os import listdir as directory
from datetime import datetime

dates = directory("news/posts")
dates_parsed = [datetime.strptime(date[:-4], "%d-%m-%Y") for date in dates]
most_recent_date = max(dates_parsed)
most_recent_date_formatted = most_recent_date.strftime("%d-%m-%Y")
mostRecentPost = most_recent_date_formatted + ".txt"

