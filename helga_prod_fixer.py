import random

from helga.plugins import command


RESPONSES = [
    'There is no hope for {thing}, {nick}',
    'It looks ok to me...',
    'Did you power cycle {thing}? Are any of the lights blinking?',
    'I\'ll take {thing} to the Genius Bar after work.',
    'Can we look at this tomorrow? I have Com Truise tickets...',
    'Just tell them not to use {thing} for now.',
    'Did you try rebooting {thing}? Try that first.',
    'We could always switch to Wordpress.',
    'We could always switch to SharePoint.',
    'We\'re still on {thing} v2.4. This doesn\'t happen to people using {thing} 2.7.',
    'Remember that obscure issue {thing} had two years ago? We should look into that again.',
    'What if we tried ... no that wouldn\'t work.',
    'We could TRY reversing the polarity...',
    '{thing} is only IE6 compatible. Make sure you\'re using the right browser.',
    'Turning {thing} off and back on again...',
    'I really wish I could, but it looks past the point of no return...',
    'I jiggled the wire. Anything?',
]


@command('fix', help='Usage: helga fix <thing>')
def fix(client, channel, nick, message, cmd, args):
    return random.choice(RESPONSES).format(nick=nick, thing=' '.join(args))
