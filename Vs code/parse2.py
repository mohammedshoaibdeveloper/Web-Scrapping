# import requests

# params = {
#   "api_key": "{t4zc_Jf-kwcu}",
#   "offset": "0",
#   "include_options": "1"
# }
# r = requests.get('https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}', params=params)
# print(r.text)
import requests

params = {
  "api_key": "{'t4zc_Jf-kwcu'}",
  "offset": "0",
  "include_options": "1"
}
r = requests.get('https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}', params=params)
print(r.text)
