import json
import re
import random

# Die format 2D6, 1D10, 20D100
DIE_DEF: re = re.compile(r'\d+d\d+', re.IGNORECASE)


def lambda_handler(event, context):
    # TODO implement
    show_work = False

    if 'ping' in event:
        return 'pong'

    if 'show_work' in event:
        show_work = event['show_work']

    die_counts = parse_die(event['die_count'])

    if show_work:
        return json.dumps(
                [item for sublist in list([roll_die(d, show_work) for d in die_counts]) for item in sublist])
        
    return  json.dumps(sum([roll_die(d) for d in die_counts]))


def parse_die(die_count: str):
    if not die_count:
        raise RuntimeError("Properly formatted die definitions not found (ex. '1D2,2D4')")

    if DIE_DEF.match(die_count):
        return [die for die in DIE_DEF.findall(die_count)]


def roll_die(die_counts: str, show_work=False):
    count, sides = die_counts.lower().split(sep='d')
    _sum = 0
    count = int(count)
    sides = int(sides)

    if not (count > 0 and sides > 0):
        if show_work:
            return [0]
        return 0

    if show_work:
        work = []
        for i in range(1, count + 1):
            work.append(random.randint(1, sides))
        return work

    for i in range(1, count + 1):
        _sum += random.randint(1, sides)

    return _sum
