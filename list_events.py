# -*- coding: utf-8 -*-

from collections import defaultdict
import json
from pathlib import Path


DATA_DIR = 'comp_event_time'


def _get_events():
    for event_f in Path(DATA_DIR).glob('*.jsonl'):
        with open(event_f) as f:
            for row in f:
                stats = json.loads(row.strip())
                for event in stats['event_avg_times'].keys():
                    yield event


def list_events():
    all_events = set()
    for event in _get_events():
        all_events.add(event)
    return all_events


def print_event_freq():
    event2freq = defaultdict(int)
    for event in _get_events():
        event2freq[event] += 1

    for event, freq in sorted(event2freq.items(), key=lambda t: t[1], reverse=True):
        print(f'{event} : {freq}')


if __name__ == '__main__':
    _all_events = list_events()
    for _evt in sorted(list(_all_events)):
        print(_evt)
