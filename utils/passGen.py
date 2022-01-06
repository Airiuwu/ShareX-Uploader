from string import ascii_uppercase, digits, ascii_lowercase
from random import choice
from os import system
import asyncio

async def randomString(size=8, chars=ascii_uppercase + digits + ascii_lowercase):
	return ''.join(choice(chars) for _ in range(size))

async def main():
    system('clear')

    print('Please input the amount of characters you want to create for your secret key')
    amount = int(input())
    confirmed = True

    while confirmed:
        password = await randomString(amount)
        print(f'Your randomly generated password is, {password}. Would you like to add it to your config? (Y/N)')
        answer = input()

        if answer.lower() is "y":
            with open('config.py', 'r') as f:
                lines = f.readlines()
                lines[2] = f"secretKey = '{password}' # Execute utils/passGen.py\n"
                with open('config.py', 'w') as conf:
                    conf.writelines(lines)
                    conf.close()

            confirmed = False
            exit()
        else:
            confirmed = True

asyncio.run(main())
