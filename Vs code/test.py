# import requests

# params = {
#   "api_key": "{YOUR_API_KEY}",
#   "offset": "0",
#   "include_options": "1"
# }
# r = requests.get('https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}', params=params)
# print(r.text)
import requests

params = {
  "api_key": "{YOUR_API_KEY}",
  "start_url": "http://www.example.com",
  "start_template": "main_template",
  "start_value_override": "{\"query\": \"San Francisco\"}",
  "send_email": "1"
}
r = requests.post("https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/run", data=params)

print(r.text)
