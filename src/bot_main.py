import asyncio
import os
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

from pluralkit import bot

pk = bot.PluralKitBot(os.environ["NDc3NjcxMjg2NzQ3OTU1MjIx.Dk_iJA.eEM2OZ6elVEAx4u3Ewe2njp-1r8"])
loop = asyncio.get_event_loop()
loop.run_until_complete(pk.run())
