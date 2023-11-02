# Write a script that formats the dates this way:
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$

from datetime import datetime

# Get the current date and time
now = datetime.now()

# Calculate the seconds since January 1, 1970 (Unix epoch)
s_since_epoch = (now - datetime(1970, 1, 1)).total_seconds()

# Format the output 4f is 4 digit after , and 2e is 2 digit on scientifical notation
# strftime if for returning a formatted date
output = f"Seconds since January 1, 1970: {s_since_epoch:,.4f} or {s_since_epoch:.2e} in scientific notation {now.strftime('%b %d %Y')}"

print(output)