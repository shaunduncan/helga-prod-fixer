import random

from helga.plugins import command


RESPONSES = [
    'There is no hope for {thing}, {nick}',
    'It looks ok to me...',
    'Did you power cycle {thing}? Are any of the lights blinking?',
    'I\'ll take {thing} to the Genius Bar after work',
    'Can we look at this tomorrow? I have Com Truise tickets...',
    'Just tell them not to use {thing} for now.',
    'Turning {thing} off and back on again',
    'I really wish I could, but it looks past the point of no return',
]


@command('fix', help='Usage: helga fix <thing>')
def fix(client, channel, nick, message, cmd, args):
    return random.choice(RESPONSES).format(nick=nick, thing=' '.join(args))
