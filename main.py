from string import ascii_uppercase, digits, ascii_lowercase
from quart import Quart, send_file, request
from random import choice
import config, imghdr
from os import path

app = Quart(__name__)

async def randomString(size=8, chars=ascii_uppercase + digits + ascii_lowercase):
	return ''.join(choice(chars) for _ in range(size))

@app.route("/screenshots/upload", methods=["POST"])
async def uploadScreenshot():
	u = request.args.get("u")
	request_files = await request.files
	ss_file = request_files["sh"]
	ss_name = await randomString()
	ss_data = ss_file.read()

	if request.args.get("key") != config.secretKey:
		return f"Hello, {u} it would seem that your secret key is incorrect."

	if not ss_file:
		return "I see what you're doing here."

	if not (ext := imghdr.what(h=ss_data, file="")) in ("gif", "png", "jpeg"):
		return "Unknown extension."

	screenshot_file = f"{config.screenshotPath}{ss_name}.{ext}"

	if path.exists(screenshot_file):
		ss_name = await randomString()

	with open(screenshot_file, "wb") as file:
		file.write(ss_data)

	return f"{config.mainURL}{ss_name}.{ext}"

@app.route("/screenshots/<string:screenshotID>")
async def getScreenshot(screenshotID):
	_path = f"{config.screenshotPath}{screenshotID}"
	if path.exists(_path): 
		return await send_file(_path)

	return "We could not find the screenshot you were looking for."

app.run(host=config.host, port=config.port)
