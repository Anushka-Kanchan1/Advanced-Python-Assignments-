import re

# Get a sentence from the user
message = input("Enter a sentence containing email addresses: ")

# Regex pattern to identify email addresses
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Search for email addresses
found_emails = re.findall(email_regex, message)

# Display the result
if len(found_emails) > 0:
    print("\nEmails found:")
    
    for item in found_emails:
        print("-", item)
    
    print("\nTotal emails:", len(found_emails))
else:
    print("\nNo email addresses were found.")


OUTPUT

Emails found:
- anushka@gmail.com
- student2026@college.edu

Total emails: 2
