# -*- coding: utf-8 -*-

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression

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


def get_regression(x, y):
    X = x.reshape(-1, 1)  # array of feature array; in this case only 1 feature
    regressor = LinearRegression()
    reg = regressor.fit(X, y)

    pred_x = np.linspace(min(x) - 0.5, max(x) + 0.5 , 100)
    pred_y = reg.predict(pred_x.reshape(-1, 1))
    score = reg.score(X, y)

    slope = reg.coef_[0]
    intercept = reg.intercept_
    msg = f'e2 = {slope} x e1 + ({intercept})'

    return (pred_x, pred_y), score, msg


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

    x = data['e1'].values
    y = data['e2'].values

    predictions, score, msg = get_regression(x, y)
    corr = np.corrcoef(x, y)[0][1]

    ax = sns.scatterplot(x='e1', y='e2', data=data,
                         s=10)
    sns.lineplot(predictions[0], predictions[1], color='r', ax=ax)

    ax.text(s=f'{len(time_points)} records, r={corr}, R^2 = {score}',
            x=0.5, y=1.08, ha='center', va='bottom', transform=ax.transAxes)
    ax.text(s=msg,
            x=0.5, y=1.03, ha='center', va='bottom', transform=ax.transAxes)

    plt.xlabel(f'e1 {event_x}')
    plt.ylabel(f'e2 {event_y}')
    plt.show()


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
