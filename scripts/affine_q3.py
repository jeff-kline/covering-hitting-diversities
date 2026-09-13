#!/usr/bin/env python3
"""Exact q=3 illustration data and finite hitting-ratio enumeration (stdlib only)."""
from fractions import Fraction
import itertools
import json


def data():
    points = [(x, y) for x in range(3) for y in range(3)]
    supplies = {(a, b): {(x, (a*x+b) % 3) for x in range(3)}
                for a in range(3) for b in range(3)}
    selected = {(0, 0), (1, 0), (2, 1)}
    return points, supplies, selected


def verify():
    points, supplies, selected = data()
    if len(supplies) != 9 or any(len(e) != 3 for e in supplies.values()):
        raise ValueError('Invalid affine supply')
    for x in range(3):
        column = {(x, y) for y in range(3)}
        if any(len(e & column) != 1 for e in supplies.values()):
            raise ValueError('Every supply must hit each column once')
        if any(column <= e | f for e, f in itertools.combinations(supplies.values(), 2)):
            raise ValueError('Two supplies cover a column')
        if not column <= set.union(*(supplies[0, b] for b in range(3))):
            raise ValueError('Horizontal cover failed')
    counts = []
    maximum = Fraction(0)
    maximizers = []
    for mask in range(1 << len(points)):
        test = {point for i, point in enumerate(points) if mask & (1 << i)}
        columns_hit = len({x for x, y in test})
        supplies_hit = sum(bool(test & edge) for edge in supplies.values())
        if not test:
            if columns_hit or supplies_hit:
                raise ValueError('Empty-cut counts must vanish')
            ratio = None  # 0/0 is not assigned a ratio.
        else:
            if not supplies_hit:
                raise ValueError('Nonempty test has zero supply hitting')
            ratio = Fraction(3*columns_hit, supplies_hit)
            if ratio > maximum:
                maximum, maximizers = ratio, [mask]
            elif ratio == maximum:
                maximizers.append(mask)
        counts.append({'mask': mask, 'columns_hit': columns_hit,
                       'supplies_hit': supplies_hit,
                       'ratio': None if ratio is None else str(ratio)})
    hit_rows = [list(key) for key, edge in supplies.items() if edge & selected]
    if hit_rows != [[0, 0], [0, 1], [1, 0], [1, 2], [2, 0], [2, 1]]:
        raise ValueError('Selected hitting rows differ')
    if maximum != Fraction(3, 2) or len(maximizers) != 18:
        raise ValueError('Unexpected maximum or multiplicity')
    if any(bin(mask).count('1') != 3 for mask in maximizers):
        raise ValueError('Maximizer is not a triple')
    if any({p for i, p in enumerate(points) if mask & (1 << i)} <= edge
           for mask in maximizers for edge in supplies.values()):
        raise ValueError('Maximizer is collinear')
    return {'q': 3, 'point_order': points, 'subsets_checked': 512,
            'nonempty_ratios_checked': 511, 'maximum_ratio': str(maximum),
            'maximizer_count': len(maximizers), 'maximizer_masks': maximizers,
            'selected_test': sorted(selected), 'selected_hit_rows': hit_rows,
            'moment_bound': '5/3', 'counts': counts}


def serialized():
    return json.dumps(verify(), indent=2, sort_keys=True) + '\n'


if __name__ == '__main__':
    result = verify()
    print('PASS: 27 affine incidences; three column costs; 512 subsets (511 nonempty ratios)')
    print('Maximum hitting ratio: 3/2; 18 maximizers, all non-collinear triples')
    print('Selected hitting rows: ' + str(result['selected_hit_rows']))
    print('Scope: q=3 only; the empty set has zero hits and no ratio')
