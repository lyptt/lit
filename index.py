"""
Testing LinkedIn scraping
"""
import os
from linkedin_api import Linkedin
from requests.cookies import cookiejar_from_dict
cookies = cookiejar_from_dict(
    {
        "liap": "true",
        "li_at": os.environ["LINKEDIN_COOKIE_LI_AT"],
        "JSESSIONID": os.environ["LINKEDIN_COOKIE_JSESSIONID"],
    }
)

api = Linkedin(os.environ["LINKEDIN_USERNAME"], os.environ["LINKEDIN_PASSWORD"], cookies=cookies)

results = api.search_companies('grocery')

print(results)
