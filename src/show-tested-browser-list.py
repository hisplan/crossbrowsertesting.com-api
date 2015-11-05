# api info @ https://crossbrowsertesting.com/apidocs/v3/screenshots
import requests, json, time
import argparse
import ConfigParser

class ScreenshotTestApi:

	def __init__(self, username, password, screenshot_test_id):

		self.auth = (username, password)
		self.baseUrl = "http://crossbrowsertesting.com/api/v3/screenshots"
		self.currentTest = None
		self.allTests = []
		self.recordCount = 0

		self.url = self.baseUrl + "/" + str(screenshot_test_id)

	def callApi(self, url, method="GET", params={}):

		if method == "GET":
			response = requests.get(url, auth=self.auth, params=params)
		elif method == "POST":
			response = requests.post(url, auth=self.auth, params=params)
		elif method == "PUT":
			response = requests.put(url, auth=self.auth, params=params)
		elif method == "DELETE":
			response = requests.delete(url, auth=self.auth, params=params)
		else:
			response = requests.get(url, auth=self.auth, params=params)

		#print response.text
		result = json.loads(response.text)

		if "status" in result:
			print "http error " + str(result["status"]),
			if "message" in result:
				print " : " + result["message"]
			quit()
		else:
			return result

	def getResultInfo(self):

		result = self.callApi(self.url, "GET")

		return result


config = ConfigParser.ConfigParser()
config.read("auth.config")

# set authentication info
username = config.get("Authentication", "username")
password = config.get("Authentication", "password")

parser = argparse.ArgumentParser()
parser.add_argument(
    '--id',
    dest='test_id',
    required=True,
    help='Screenshot test ID (e.g. 822563)'
)

settings = parser.parse_args()

api = ScreenshotTestApi(username, password, settings.test_id)

info = api.getResultInfo()

version_count = info["version_count"];

for version in info["versions"]:

	print "Tested Browsers: {}".format( version["show_results_public_url"] )

	for index, result in enumerate(version["results"]):
		print "# {} / {} ".format( result["os"]["name"], result["browser"]["name"] )

	print

