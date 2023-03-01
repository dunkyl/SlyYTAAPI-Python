import sys, asyncio, inspect

from SlySheets.sheets import Scope
from SlyAPI.flow import *

async def main(args: list[str]):

    match args:
        case ['grant']:
            await grant_wizard(Scope, kind='OAuth2')
        case _: # help
            print(inspect.cleandoc("""
            SlyYTAAPI command line: tool for YouTube Analytics OAuth2.
            Usage:
                SlyYTAAPI grant
                Same as SlyAPI, but scopes are listed in a menu.
            """))

if __name__ == '__main__':
    asyncio.run(main(sys.argv[1:]))