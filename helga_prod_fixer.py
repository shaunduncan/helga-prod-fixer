import random

from helga.plugins import command


RESPONSES = [
    'There is no hope for {thing}, {nick}',
    'It looks ok to me...',
    'Turning {thing} off and back on again',
    'I really wish I could, but it looks past the point of no return',
]


@command('fix', help='Usage: helga fix <thing>')
def fix(client, channel, nick, message, cmd, args):
    return random.choice(RESPONSES).format(nick=nick, thing=args[0])
