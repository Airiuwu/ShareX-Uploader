import config
from quart import Quart, send_file, request
from os import path
from random import choice
from string import ascii_uppercase, digits, ascii_lowercase

app = Quart(__name__)

async def randomString(size=8, chars=ascii_uppercase + digits + ascii_lowercase):
	return ''.join(choice(chars) for _ in range(size))

@app.route("/screenshots/upload", methods=["POST"])
async def uploadScreenshot():
    u = request.args.get("u")
    request_files = await request.files
    ssFile = request_files["sh"]
    ssName = await randomString()

    if request.args.get("key") != config.secretKey:
        return f"Hello, {u} it would seem that your secret key is incorrect."

    if not ssFile:
        return "I see what you're doing here."
    
    if path.exists(f"{config.screenshotPath}{ssName}.png"):    
        ssName = await randomString()

    with open(f"{config.screenshotPath}{ssName}.png", "wb") as file:
        file.write(ssFile.read())

    return f"{config.mainURL}{ssName}"

@app.route("/screenshots/<string:screenshotID>")
async def getScreenshot(screenshotID):
    if path.exists(f"{config.screenshotPath}/{screenshotID}.png"):    
        return await send_file(f"{config.screenshotPath}/{screenshotID}.png")
    else:
        return "We could not find the screenshot you were looking for."

app.run(host=config.host, port=config.port)
