# -*- coding: utf-8 -*-

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
import seaborn as sns

DATA_DIR = 'comp_event_time'

VALID_EVENTS = [
    '2x2x2 Cube', '3x3x3 Blindfolded', '3x3x3 Cube', '3x3x3 Fewest Moves', '3x3x3 One-Handed',
    '3x3x3 With Feet', '4x4x4 Blindfolded', '4x4x4 Cube', '5x5x5 Blindfolded', '5x5x5 Cube',
    '6x6x6 Cube', '7x7x7 Cube', 'Clock', 'Megaminx', 'Pyraminx', 'Skewb', 'Square-1',
]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('event_x', choices=VALID_EVENTS)
    parser.add_argument('event_y', choices=VALID_EVENTS)

    return parser.parse_args()


def plot_correlation(event_x, event_y):
    time_points = []
    for event_f in Path(DATA_DIR).glob('*.jsonl'):
        with open(event_f) as f:
            for row in f:
                stats = json.loads(row.strip())
                time_x = stats['event_avg_times'].get(event_x)
                time_y = stats['event_avg_times'].get(event_y)
                if time_x and time_y:
                    time_points.append([float(time_x), float(time_y)])

    data = pd.DataFrame(time_points, columns=['e1', 'e2'])
    ax = sns.scatterplot(x='e2', y='e1', data=data)

    plt.show()
    print(len(time_points))


def list_events():
    all_events = set()
    for event_f in Path(DATA_DIR).glob('*.jsonl'):
        with open(event_f) as f:
            for row in f:
                stats = json.loads(row.strip())
                for event in stats['event_avg_times'].keys():
                    all_events.add(event)

    return all_events


def main(args):
    event_x = args.event_x
    event_y = args.event_y
    plot_correlation(event_x, event_y)


if __name__ == '__main__':
    parsed_args = parse_args()
    main(parsed_args)
