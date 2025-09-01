# Leduc-Poker-Bot
An implementation of counterfactual regret minimisation to compute strategies/Nash equilibria/game value for Kuhn and Leduc Poker

# Explanation of variants
Kuhn poker has a deck of 3 cards (J, Q, K), 1 betting round with no raises and a showdown for the highest card.
Leduc poker has a deck of 6 card, 2 x (J, Q, K), 2 betting rounds with 2 raises max, and a showdown with a community card flopped after the first round to determine the winner (pair beats high card etc.).

# Files
kuhnplay.py and leducplay.py will simulate a random game of each variant of poker, respectively
kuhnsolve.py and leducsolve.py both use counterfactual minimisation to calculate strategies in alignment with Nash equilibria for the respective variants of poker, as well as game value

# Output of leducsolve.py for 500 iterations :
Note: format is P1 card, hole card if shown, round, round 0 history, round 1 history: Strategy ( b= bet, c= call, f= fold, x=check, r=raise)
Node J|None|r0||: {'b': 0.08, 'x': 0.92}
Node J|None|r0|b|: {'c': 0.21, 'f': 0.72, 'r': 0.06}
Node J|Q|r1|bc|: {'b': 0.35, 'x': 0.65}
Node J|Q|r1|bc|b: {'c': 0.0, 'f': 0.99, 'r': 0.01}
Node J|Q|r1|bc|br: {'c': 0.0, 'f': 0.99, 'r': 0.01}
Node J|Q|r1|bc|brr: {'c': 0.32, 'f': 0.68}
Node J|Q|r1|bc|x: {'b': 0.68, 'x': 0.32}
Node J|Q|r1|bc|xb: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|Q|r1|bc|xbr: {'c': 0.0, 'f': 0.79, 'r': 0.21}
Node J|Q|r1|bc|xbrr: {'c': 0.43, 'f': 0.57}
Node J|None|r0|br|: {'c': 0.01, 'f': 0.0, 'r': 0.99}
Node J|Q|r1|brc|: {'b': 0.02, 'x': 0.98}
Node J|Q|r1|brc|b: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|Q|r1|brc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node J|Q|r1|brc|brr: {'c': 0.5, 'f': 0.5}
Node J|Q|r1|brc|x: {'b': 0.01, 'x': 0.99}
Node J|Q|r1|brc|xb: {'c': 0.01, 'f': 0.99, 'r': 0.01}
Node J|Q|r1|brc|xbr: {'c': 0.01, 'f': 0.98, 'r': 0.01}
Node J|Q|r1|brc|xbrr: {'c': 0.5, 'f': 0.5}
Node J|None|r0|brr|: {'c': 1.0, 'f': 0.0}
Node J|Q|r1|brrc|: {'b': 0.0, 'x': 1.0}
Node J|Q|r1|brrc|b: {'c': 0.0, 'f': 0.64, 'r': 0.35}
Node J|Q|r1|brrc|br: {'c': 0.21, 'f': 0.02, 'r': 0.77}
Node J|Q|r1|brrc|brr: {'c': 0.01, 'f': 0.99}
Node J|Q|r1|brrc|x: {'b': 0.04, 'x': 0.96}
Node J|Q|r1|brrc|xb: {'c': 0.0, 'f': 0.94, 'r': 0.06}
Node J|Q|r1|brrc|xbr: {'c': 0.02, 'f': 0.18, 'r': 0.8}
Node J|Q|r1|brrc|xbrr: {'c': 0.04, 'f': 0.96}
Node J|None|r0|x|: {'b': 0.08, 'x': 0.92}
Node J|None|r0|xb|: {'c': 0.01, 'f': 0.99, 'r': 0.01}
Node J|Q|r1|xbc|: {'b': 0.01, 'x': 0.99}
Node J|Q|r1|xbc|b: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|Q|r1|xbc|br: {'c': 0.06, 'f': 0.88, 'r': 0.06}
Node J|Q|r1|xbc|brr: {'c': 0.5, 'f': 0.5}
Node J|Q|r1|xbc|x: {'b': 0.0, 'x': 1.0}
Node J|Q|r1|xbc|xb: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|Q|r1|xbc|xbr: {'c': 0.05, 'f': 0.89, 'r': 0.05}
Node J|Q|r1|xbc|xbrr: {'c': 0.5, 'f': 0.5}
Node J|None|r0|xbr|: {'c': 0.99, 'f': 0.0, 'r': 0.01}
Node J|Q|r1|xbrc|: {'b': 0.12, 'x': 0.88}
Node J|Q|r1|xbrc|b: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|Q|r1|xbrc|br: {'c': 0.14, 'f': 0.01, 'r': 0.86}
Node J|Q|r1|xbrc|brr: {'c': 0.32, 'f': 0.68}
Node J|Q|r1|xbrc|x: {'b': 0.14, 'x': 0.86}
Node J|Q|r1|xbrc|xb: {'c': 0.0, 'f': 0.99, 'r': 0.01}
Node J|Q|r1|xbrc|xbr: {'c': 0.0, 'f': 0.95, 'r': 0.05}
Node J|Q|r1|xbrc|xbrr: {'c': 0.81, 'f': 0.19}
Node J|None|r0|xbrr|: {'c': 1.0, 'f': 0.0}
Node J|Q|r1|xbrrc|: {'b': 0.16, 'x': 0.84}
Node J|Q|r1|xbrrc|b: {'c': 0.01, 'f': 0.98, 'r': 0.01}
Node J|Q|r1|xbrrc|br: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|Q|r1|xbrrc|brr: {'c': 0.5, 'f': 0.5}
Node J|Q|r1|xbrrc|x: {'b': 0.14, 'x': 0.86}
Node J|Q|r1|xbrrc|xb: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|Q|r1|xbrrc|xbr: {'c': 0.03, 'f': 0.94, 'r': 0.03}
Node J|Q|r1|xbrrc|xbrr: {'c': 0.5, 'f': 0.5}
Node J|Q|r1|xx|: {'b': 0.0, 'x': 1.0}
Node J|Q|r1|xx|b: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|Q|r1|xx|br: {'c': 0.22, 'f': 0.07, 'r': 0.71}
Node J|Q|r1|xx|brr: {'c': 0.95, 'f': 0.05}
Node J|Q|r1|xx|x: {'b': 0.04, 'x': 0.96}
Node J|Q|r1|xx|xb: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|Q|r1|xx|xbr: {'c': 0.0, 'f': 0.98, 'r': 0.02}
Node J|Q|r1|xx|xbrr: {'c': 0.39, 'f': 0.61}
Node J|K|r1|bc|: {'b': 0.98, 'x': 0.02}
Node J|K|r1|bc|b: {'c': 0.0, 'f': 0.87, 'r': 0.13}
Node J|K|r1|bc|br: {'c': 0.0, 'f': 0.83, 'r': 0.17}
Node J|K|r1|bc|brr: {'c': 0.02, 'f': 0.98}
Node J|K|r1|bc|x: {'b': 0.42, 'x': 0.58}
Node J|K|r1|bc|xb: {'c': 0.03, 'f': 0.91, 'r': 0.05}
Node J|K|r1|bc|xbr: {'c': 0.0, 'f': 0.67, 'r': 0.33}
Node J|K|r1|bc|xbrr: {'c': 0.61, 'f': 0.39}
Node J|K|r1|brc|: {'b': 0.0, 'x': 1.0}
Node J|K|r1|brc|b: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|K|r1|brc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node J|K|r1|brc|brr: {'c': 0.5, 'f': 0.5}
Node J|K|r1|brc|x: {'b': 0.0, 'x': 1.0}
Node J|K|r1|brc|xb: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|K|r1|brc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node J|K|r1|brc|xbrr: {'c': 0.5, 'f': 0.5}
Node J|K|r1|brrc|: {'b': 0.42, 'x': 0.58}
Node J|K|r1|brrc|b: {'c': 0.0, 'f': 0.99, 'r': 0.01}
Node J|K|r1|brrc|br: {'c': 0.0, 'f': 0.93, 'r': 0.07}
Node J|K|r1|brrc|brr: {'c': 0.22, 'f': 0.78}
Node J|K|r1|brrc|x: {'b': 0.98, 'x': 0.02}
Node J|K|r1|brrc|xb: {'c': 0.0, 'f': 0.94, 'r': 0.06}
Node J|K|r1|brrc|xbr: {'c': 0.0, 'f': 0.81, 'r': 0.19}
Node J|K|r1|brrc|xbrr: {'c': 0.0, 'f': 1.0}
Node J|K|r1|xbc|: {'b': 0.0, 'x': 1.0}
Node J|K|r1|xbc|b: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|K|r1|xbc|br: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|K|r1|xbc|brr: {'c': 0.5, 'f': 0.5}
Node J|K|r1|xbc|x: {'b': 0.01, 'x': 0.99}
Node J|K|r1|xbc|xb: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|K|r1|xbc|xbr: {'c': 0.04, 'f': 0.92, 'r': 0.04}
Node J|K|r1|xbc|xbrr: {'c': 0.5, 'f': 0.5}
Node J|K|r1|xbrc|: {'b': 0.66, 'x': 0.34}
Node J|K|r1|xbrc|b: {'c': 0.0, 'f': 0.93, 'r': 0.07}
Node J|K|r1|xbrc|br: {'c': 0.03, 'f': 0.94, 'r': 0.03}
Node J|K|r1|xbrc|brr: {'c': 0.0, 'f': 1.0}
Node J|K|r1|xbrc|x: {'b': 0.01, 'x': 0.99}
Node J|K|r1|xbrc|xb: {'c': 0.05, 'f': 0.9, 'r': 0.05}
Node J|K|r1|xbrc|xbr: {'c': 0.0, 'f': 0.34, 'r': 0.66}
Node J|K|r1|xbrc|xbrr: {'c': 0.5, 'f': 0.5}
Node J|K|r1|xbrrc|: {'b': 0.0, 'x': 1.0}
Node J|K|r1|xbrrc|b: {'c': 0.09, 'f': 0.82, 'r': 0.09}
Node J|K|r1|xbrrc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node J|K|r1|xbrrc|brr: {'c': 0.5, 'f': 0.5}
Node J|K|r1|xbrrc|x: {'b': 0.23, 'x': 0.77}
Node J|K|r1|xbrrc|xb: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|K|r1|xbrrc|xbr: {'c': 0.2, 'f': 0.6, 'r': 0.2}
Node J|K|r1|xbrrc|xbrr: {'c': 0.5, 'f': 0.5}
Node J|K|r1|xx|: {'b': 0.1, 'x': 0.9}
Node J|K|r1|xx|b: {'c': 0.0, 'f': 0.99, 'r': 0.01}
Node J|K|r1|xx|br: {'c': 0.0, 'f': 0.87, 'r': 0.13}
Node J|K|r1|xx|brr: {'c': 0.01, 'f': 0.99}
Node J|K|r1|xx|x: {'b': 0.01, 'x': 0.99}
Node J|K|r1|xx|xb: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|K|r1|xx|xbr: {'c': 0.02, 'f': 0.95, 'r': 0.03}
Node J|K|r1|xx|xbrr: {'c': 0.3, 'f': 0.7}
Node Q|None|r0|b|: {'c': 0.76, 'f': 0.0, 'r': 0.23}
Node J|J|r1|bc|: {'b': 0.37, 'x': 0.63}
Node Q|J|r1|bc|b: {'c': 0.0, 'f': 0.96, 'r': 0.04}
Node J|J|r1|bc|br: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|J|r1|bc|brr: {'c': 0.01, 'f': 0.99}
Node Q|J|r1|bc|x: {'b': 0.01, 'x': 0.99}
Node J|J|r1|bc|xb: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|J|r1|bc|xbr: {'c': 0.0, 'f': 0.82, 'r': 0.18}
Node J|J|r1|bc|xbrr: {'c': 1.0, 'f': 0.0}
Node J|J|r1|brc|: {'b': 0.01, 'x': 0.99}
Node Q|J|r1|brc|b: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|J|r1|brc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|J|r1|brc|brr: {'c': 0.5, 'f': 0.5}
Node Q|J|r1|brc|x: {'b': 0.0, 'x': 1.0}
Node J|J|r1|brc|xb: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node Q|J|r1|brc|xbr: {'c': 0.33, 'f': 0.35, 'r': 0.33}
Node J|J|r1|brc|xbrr: {'c': 0.5, 'f': 0.5}
Node Q|None|r0|brr|: {'c': 1.0, 'f': 0.0}
Node J|J|r1|brrc|: {'b': 0.96, 'x': 0.04}
Node Q|J|r1|brrc|b: {'c': 0.0, 'f': 0.96, 'r': 0.04}
Node J|J|r1|brrc|br: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|J|r1|brrc|brr: {'c': 0.02, 'f': 0.98}
Node Q|J|r1|brrc|x: {'b': 0.0, 'x': 1.0}
Node J|J|r1|brrc|xb: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|J|r1|brrc|xbr: {'c': 0.0, 'f': 0.61, 'r': 0.38}
Node J|J|r1|brrc|xbrr: {'c': 1.0, 'f': 0.0}
Node Q|None|r0|x|: {'b': 0.57, 'x': 0.43}
Node J|J|r1|xbc|: {'b': 0.0, 'x': 1.0}
Node Q|J|r1|xbc|b: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|J|r1|xbc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|J|r1|xbc|brr: {'c': 0.5, 'f': 0.5}
Node Q|J|r1|xbc|x: {'b': 0.0, 'x': 1.0}
Node J|J|r1|xbc|xb: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node Q|J|r1|xbc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node J|J|r1|xbc|xbrr: {'c': 0.5, 'f': 0.5}
Node Q|None|r0|xbr|: {'c': 0.45, 'f': 0.0, 'r': 0.55}
Node J|J|r1|xbrc|: {'b': 0.42, 'x': 0.58}
Node Q|J|r1|xbrc|b: {'c': 0.0, 'f': 0.99, 'r': 0.01}
Node J|J|r1|xbrc|br: {'c': 0.14, 'f': 0.02, 'r': 0.84}
Node Q|J|r1|xbrc|brr: {'c': 0.44, 'f': 0.56}
Node Q|J|r1|xbrc|x: {'b': 0.01, 'x': 0.99}
Node J|J|r1|xbrc|xb: {'c': 0.01, 'f': 0.01, 'r': 0.97}
Node Q|J|r1|xbrc|xbr: {'c': 0.0, 'f': 0.66, 'r': 0.34}
Node J|J|r1|xbrc|xbrr: {'c': 0.99, 'f': 0.01}
Node J|J|r1|xbrrc|: {'b': 0.03, 'x': 0.97}
Node Q|J|r1|xbrrc|b: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|J|r1|xbrrc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|J|r1|xbrrc|brr: {'c': 0.5, 'f': 0.5}
Node Q|J|r1|xbrrc|x: {'b': 0.0, 'x': 1.0}
Node J|J|r1|xbrrc|xb: {'c': 0.5, 'f': 0.5, 'r': 0.01}
Node Q|J|r1|xbrrc|xbr: {'c': 0.09, 'f': 0.82, 'r': 0.09}
Node J|J|r1|xbrrc|xbrr: {'c': 0.5, 'f': 0.5}
Node J|J|r1|xx|: {'b': 0.0, 'x': 1.0}
Node Q|J|r1|xx|b: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|J|r1|xx|br: {'c': 0.23, 'f': 0.01, 'r': 0.76}
Node Q|J|r1|xx|brr: {'c': 0.23, 'f': 0.77}
Node Q|J|r1|xx|x: {'b': 0.0, 'x': 1.0}
Node J|J|r1|xx|xb: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|J|r1|xx|xbr: {'c': 0.02, 'f': 0.97, 'r': 0.02}
Node J|J|r1|xx|xbrr: {'c': 1.0, 'f': 0.0}
Node Q|Q|r1|bc|b: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|Q|r1|bc|brr: {'c': 1.0, 'f': 0.0}
Node Q|Q|r1|bc|x: {'b': 1.0, 'x': 0.0}
Node Q|Q|r1|bc|xbr: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|Q|r1|brc|b: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|Q|r1|brc|brr: {'c': 0.5, 'f': 0.5}
Node Q|Q|r1|brc|x: {'b': 0.0, 'x': 1.0}
Node Q|Q|r1|brc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|Q|r1|brrc|b: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|Q|r1|brrc|brr: {'c': 1.0, 'f': 0.0}
Node Q|Q|r1|brrc|x: {'b': 1.0, 'x': 0.0}
Node Q|Q|r1|brrc|xbr: {'c': 0.08, 'f': 0.0, 'r': 0.92}
Node Q|Q|r1|xbc|b: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node Q|Q|r1|xbc|brr: {'c': 0.5, 'f': 0.5}
Node Q|Q|r1|xbc|x: {'b': 0.0, 'x': 1.0}
Node Q|Q|r1|xbc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|Q|r1|xbrc|b: {'c': 0.63, 'f': 0.0, 'r': 0.37}
Node Q|Q|r1|xbrc|brr: {'c': 1.0, 'f': 0.0}
Node Q|Q|r1|xbrc|x: {'b': 1.0, 'x': 0.0}
Node Q|Q|r1|xbrc|xbr: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|Q|r1|xbrrc|b: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node Q|Q|r1|xbrrc|brr: {'c': 0.5, 'f': 0.5}
Node Q|Q|r1|xbrrc|x: {'b': 0.0, 'x': 1.0}
Node Q|Q|r1|xbrrc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|Q|r1|xx|b: {'c': 0.71, 'f': 0.0, 'r': 0.29}
Node Q|Q|r1|xx|brr: {'c': 1.0, 'f': 0.0}
Node Q|Q|r1|xx|x: {'b': 1.0, 'x': 0.0}
Node Q|Q|r1|xx|xbr: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|K|r1|bc|b: {'c': 0.23, 'f': 0.69, 'r': 0.09}
Node Q|K|r1|bc|brr: {'c': 0.02, 'f': 0.98}
Node Q|K|r1|bc|x: {'b': 0.18, 'x': 0.82}
Node Q|K|r1|bc|xbr: {'c': 0.0, 'f': 0.92, 'r': 0.08}
Node Q|K|r1|brc|b: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|K|r1|brc|brr: {'c': 0.5, 'f': 0.5}
Node Q|K|r1|brc|x: {'b': 0.0, 'x': 1.0}
Node Q|K|r1|brc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|K|r1|brrc|b: {'c': 0.44, 'f': 0.52, 'r': 0.04}
Node Q|K|r1|brrc|brr: {'c': 0.03, 'f': 0.97}
Node Q|K|r1|brrc|x: {'b': 0.14, 'x': 0.86}
Node Q|K|r1|brrc|xbr: {'c': 0.01, 'f': 0.95, 'r': 0.04}
Node Q|K|r1|xbc|b: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node Q|K|r1|xbc|brr: {'c': 0.5, 'f': 0.5}
Node Q|K|r1|xbc|x: {'b': 0.0, 'x': 1.0}
Node Q|K|r1|xbc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|K|r1|xbrc|b: {'c': 0.0, 'f': 0.99, 'r': 0.0}
Node Q|K|r1|xbrc|brr: {'c': 1.0, 'f': 0.0}
Node Q|K|r1|xbrc|x: {'b': 0.01, 'x': 0.99}
Node Q|K|r1|xbrc|xbr: {'c': 0.03, 'f': 0.58, 'r': 0.39}
Node Q|K|r1|xbrrc|b: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node Q|K|r1|xbrrc|brr: {'c': 0.5, 'f': 0.5}
Node Q|K|r1|xbrrc|x: {'b': 0.0, 'x': 1.0}
Node Q|K|r1|xbrrc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|K|r1|xx|b: {'c': 0.49, 'f': 0.5, 'r': 0.0}
Node Q|K|r1|xx|brr: {'c': 0.43, 'f': 0.57}
Node Q|K|r1|xx|x: {'b': 0.19, 'x': 0.81}
Node Q|K|r1|xx|xbr: {'c': 0.48, 'f': 0.0, 'r': 0.52}
Node K|None|r0|b|: {'c': 0.55, 'f': 0.0, 'r': 0.45}
Node K|J|r1|bc|b: {'c': 0.78, 'f': 0.22, 'r': 0.0}
Node K|J|r1|bc|brr: {'c': 0.99, 'f': 0.01}
Node K|J|r1|bc|x: {'b': 0.45, 'x': 0.55}
Node K|J|r1|bc|xbr: {'c': 0.04, 'f': 0.36, 'r': 0.6}
Node K|J|r1|brc|b: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|J|r1|brc|brr: {'c': 0.5, 'f': 0.5}
Node K|J|r1|brc|x: {'b': 0.0, 'x': 1.0}
Node K|J|r1|brc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|None|r0|brr|: {'c': 1.0, 'f': 0.0}
Node K|J|r1|brrc|b: {'c': 0.96, 'f': 0.04, 'r': 0.01}
Node K|J|r1|brrc|brr: {'c': 0.96, 'f': 0.04}
Node K|J|r1|brrc|x: {'b': 0.18, 'x': 0.82}
Node K|J|r1|brrc|xbr: {'c': 0.43, 'f': 0.0, 'r': 0.57}
Node K|None|r0|x|: {'b': 0.96, 'x': 0.04}
Node K|J|r1|xbc|b: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node K|J|r1|xbc|brr: {'c': 0.5, 'f': 0.5}
Node K|J|r1|xbc|x: {'b': 0.0, 'x': 1.0}
Node K|J|r1|xbc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|None|r0|xbr|: {'c': 0.25, 'f': 0.0, 'r': 0.75}
Node K|J|r1|xbrc|b: {'c': 0.46, 'f': 0.0, 'r': 0.53}
Node K|J|r1|xbrc|brr: {'c': 1.0, 'f': 0.0}
Node K|J|r1|xbrc|x: {'b': 0.45, 'x': 0.55}
Node K|J|r1|xbrc|xbr: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node K|J|r1|xbrrc|b: {'c': 0.42, 'f': 0.42, 'r': 0.15}
Node K|J|r1|xbrrc|brr: {'c': 0.5, 'f': 0.5}
Node K|J|r1|xbrrc|x: {'b': 0.0, 'x': 1.0}
Node K|J|r1|xbrrc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|J|r1|xx|b: {'c': 0.01, 'f': 0.99, 'r': 0.0}
Node K|J|r1|xx|brr: {'c': 0.5, 'f': 0.5}
Node K|J|r1|xx|x: {'b': 0.0, 'x': 1.0}
Node K|J|r1|xx|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|Q|r1|bc|b: {'c': 0.33, 'f': 0.58, 'r': 0.09}
Node K|Q|r1|bc|brr: {'c': 0.01, 'f': 0.99}
Node K|Q|r1|bc|x: {'b': 0.1, 'x': 0.9}
Node K|Q|r1|bc|xbr: {'c': 0.01, 'f': 0.97, 'r': 0.01}
Node K|Q|r1|brc|b: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|Q|r1|brc|brr: {'c': 0.5, 'f': 0.5}
Node K|Q|r1|brc|x: {'b': 0.0, 'x': 1.0}
Node K|Q|r1|brc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|Q|r1|brrc|b: {'c': 0.69, 'f': 0.29, 'r': 0.02}
Node K|Q|r1|brrc|brr: {'c': 0.14, 'f': 0.86}
Node K|Q|r1|brrc|x: {'b': 0.47, 'x': 0.53}
Node K|Q|r1|brrc|xbr: {'c': 0.22, 'f': 0.34, 'r': 0.44}
Node K|Q|r1|xbc|b: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node K|Q|r1|xbc|brr: {'c': 0.5, 'f': 0.5}
Node K|Q|r1|xbc|x: {'b': 0.0, 'x': 1.0}
Node K|Q|r1|xbc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|Q|r1|xbrc|b: {'c': 1.0, 'f': 0.0, 'r': 0.0}
Node K|Q|r1|xbrc|brr: {'c': 1.0, 'f': 0.0}
Node K|Q|r1|xbrc|x: {'b': 0.98, 'x': 0.02}
Node K|Q|r1|xbrc|xbr: {'c': 0.09, 'f': 0.3, 'r': 0.61}
Node K|Q|r1|xbrrc|b: {'c': 0.48, 'f': 0.48, 'r': 0.04}
Node K|Q|r1|xbrrc|brr: {'c': 0.5, 'f': 0.5}
Node K|Q|r1|xbrrc|x: {'b': 0.0, 'x': 1.0}
Node K|Q|r1|xbrrc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|Q|r1|xx|b: {'c': 0.0, 'f': 0.99, 'r': 0.0}
Node K|Q|r1|xx|brr: {'c': 0.5, 'f': 0.5}
Node K|Q|r1|xx|x: {'b': 0.01, 'x': 0.99}
Node K|Q|r1|xx|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|K|r1|bc|b: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node K|K|r1|bc|brr: {'c': 1.0, 'f': 0.0}
Node K|K|r1|bc|x: {'b': 1.0, 'x': 0.0}
Node K|K|r1|bc|xbr: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node K|K|r1|brc|b: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|K|r1|brc|brr: {'c': 0.5, 'f': 0.5}
Node K|K|r1|brc|x: {'b': 0.0, 'x': 1.0}
Node K|K|r1|brc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|K|r1|brrc|b: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node K|K|r1|brrc|brr: {'c': 1.0, 'f': 0.0}
Node K|K|r1|brrc|x: {'b': 1.0, 'x': 0.0}
Node K|K|r1|brrc|xbr: {'c': 0.21, 'f': 0.0, 'r': 0.79}
Node K|K|r1|xbc|b: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|K|r1|xbc|brr: {'c': 0.5, 'f': 0.5}
Node K|K|r1|xbc|x: {'b': 0.0, 'x': 1.0}
Node K|K|r1|xbc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|K|r1|xbrc|b: {'c': 0.32, 'f': 0.0, 'r': 0.68}
Node K|K|r1|xbrc|brr: {'c': 1.0, 'f': 0.0}
Node K|K|r1|xbrc|x: {'b': 1.0, 'x': 0.0}
Node K|K|r1|xbrc|xbr: {'c': 0.28, 'f': 0.0, 'r': 0.72}
Node K|K|r1|xbrrc|b: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|K|r1|xbrrc|brr: {'c': 0.5, 'f': 0.5}
Node K|K|r1|xbrrc|x: {'b': 0.0, 'x': 1.0}
Node K|K|r1|xbrrc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|K|r1|xx|b: {'c': 0.01, 'f': 0.01, 'r': 0.99}
Node K|K|r1|xx|brr: {'c': 1.0, 'f': 0.0}
Node K|K|r1|xx|x: {'b': 1.0, 'x': 0.0}
Node K|K|r1|xx|xbr: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|None|r0||: {'b': 0.34, 'x': 0.66}
Node Q|J|r1|bc|: {'b': 0.01, 'x': 0.99}
Node J|J|r1|bc|b: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|J|r1|bc|br: {'c': 0.0, 'f': 0.9, 'r': 0.09}
Node J|J|r1|bc|brr: {'c': 1.0, 'f': 0.0}
Node J|J|r1|bc|x: {'b': 1.0, 'x': 0.0}
Node Q|J|r1|bc|xb: {'c': 0.0, 'f': 0.98, 'r': 0.02}
Node J|J|r1|bc|xbr: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|J|r1|bc|xbrr: {'c': 0.0, 'f': 1.0}
Node Q|None|r0|br|: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|J|r1|brc|: {'b': 0.01, 'x': 0.99}
Node J|J|r1|brc|b: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node Q|J|r1|brc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node J|J|r1|brc|brr: {'c': 0.5, 'f': 0.5}
Node J|J|r1|brc|x: {'b': 0.0, 'x': 1.0}
Node Q|J|r1|brc|xb: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node J|J|r1|brc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|J|r1|brc|xbrr: {'c': 0.5, 'f': 0.5}
Node Q|J|r1|brrc|: {'b': 0.0, 'x': 1.0}
Node J|J|r1|brrc|b: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|J|r1|brrc|br: {'c': 0.02, 'f': 0.59, 'r': 0.39}
Node J|J|r1|brrc|brr: {'c': 1.0, 'f': 0.0}
Node J|J|r1|brrc|x: {'b': 1.0, 'x': 0.0}
Node Q|J|r1|brrc|xb: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|J|r1|brrc|xbr: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|J|r1|brrc|xbrr: {'c': 0.8, 'f': 0.2}
Node Q|None|r0|xb|: {'c': 0.39, 'f': 0.53, 'r': 0.09}
Node Q|J|r1|xbc|: {'b': 0.0, 'x': 1.0}
Node J|J|r1|xbc|b: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node Q|J|r1|xbc|br: {'c': 0.12, 'f': 0.76, 'r': 0.12}
Node J|J|r1|xbc|brr: {'c': 0.5, 'f': 0.5}
Node J|J|r1|xbc|x: {'b': 0.0, 'x': 1.0}
Node Q|J|r1|xbc|xb: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node J|J|r1|xbc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|J|r1|xbc|xbrr: {'c': 0.5, 'f': 0.5}
Node Q|J|r1|xbrc|: {'b': 0.05, 'x': 0.95}
Node J|J|r1|xbrc|b: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|J|r1|xbrc|br: {'c': 0.07, 'f': 0.67, 'r': 0.27}
Node J|J|r1|xbrc|brr: {'c': 1.0, 'f': 0.0}
Node J|J|r1|xbrc|x: {'b': 1.0, 'x': 0.0}
Node Q|J|r1|xbrc|xb: {'c': 0.0, 'f': 0.99, 'r': 0.01}
Node J|J|r1|xbrc|xbr: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|J|r1|xbrc|xbrr: {'c': 0.28, 'f': 0.72}
Node Q|None|r0|xbrr|: {'c': 1.0, 'f': 0.0}
Node Q|J|r1|xbrrc|: {'b': 0.02, 'x': 0.98}
Node J|J|r1|xbrrc|b: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node Q|J|r1|xbrrc|br: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|J|r1|xbrrc|brr: {'c': 0.5, 'f': 0.5}
Node J|J|r1|xbrrc|x: {'b': 0.0, 'x': 1.0}
Node Q|J|r1|xbrrc|xb: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node J|J|r1|xbrrc|xbr: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|J|r1|xbrrc|xbrr: {'c': 0.5, 'f': 0.5}
Node Q|J|r1|xx|: {'b': 0.0, 'x': 1.0}
Node J|J|r1|xx|b: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|J|r1|xx|br: {'c': 0.03, 'f': 0.48, 'r': 0.5}
Node J|J|r1|xx|brr: {'c': 1.0, 'f': 0.0}
Node J|J|r1|xx|x: {'b': 1.0, 'x': 0.0}
Node Q|J|r1|xx|xb: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node J|J|r1|xx|xbr: {'c': 0.21, 'f': 0.0, 'r': 0.79}
Node Q|J|r1|xx|xbrr: {'c': 0.24, 'f': 0.76}
Node Q|Q|r1|bc|: {'b': 0.49, 'x': 0.51}
Node Q|Q|r1|bc|br: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|Q|r1|bc|xb: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|Q|r1|bc|xbrr: {'c': 1.0, 'f': 0.0}
Node Q|Q|r1|brc|: {'b': 0.0, 'x': 1.0}
Node Q|Q|r1|brc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|Q|r1|brc|xb: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node Q|Q|r1|brc|xbrr: {'c': 0.5, 'f': 0.5}
Node Q|Q|r1|brrc|: {'b': 0.88, 'x': 0.12}
Node Q|Q|r1|brrc|br: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|Q|r1|brrc|xb: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|Q|r1|brrc|xbrr: {'c': 1.0, 'f': 0.0}
Node Q|Q|r1|xbc|: {'b': 0.0, 'x': 1.0}
Node Q|Q|r1|xbc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|Q|r1|xbc|xb: {'c': 0.46, 'f': 0.46, 'r': 0.09}
Node Q|Q|r1|xbc|xbrr: {'c': 0.5, 'f': 0.5}
Node Q|Q|r1|xbrc|: {'b': 0.06, 'x': 0.94}
Node Q|Q|r1|xbrc|br: {'c': 0.03, 'f': 0.0, 'r': 0.97}
Node Q|Q|r1|xbrc|xb: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node Q|Q|r1|xbrc|xbrr: {'c': 1.0, 'f': 0.0}
Node Q|Q|r1|xbrrc|: {'b': 0.0, 'x': 1.0}
Node Q|Q|r1|xbrrc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|Q|r1|xbrrc|xb: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|Q|r1|xbrrc|xbrr: {'c': 0.5, 'f': 0.5}
Node Q|Q|r1|xx|: {'b': 0.0, 'x': 1.0}
Node Q|Q|r1|xx|br: {'c': 0.26, 'f': 0.05, 'r': 0.68}
Node Q|Q|r1|xx|xb: {'c': 0.57, 'f': 0.0, 'r': 0.43}
Node Q|Q|r1|xx|xbrr: {'c': 1.0, 'f': 0.0}
Node Q|K|r1|bc|: {'b': 0.24, 'x': 0.76}
Node Q|K|r1|bc|br: {'c': 0.0, 'f': 0.87, 'r': 0.13}
Node Q|K|r1|bc|xb: {'c': 0.52, 'f': 0.43, 'r': 0.05}
Node Q|K|r1|bc|xbrr: {'c': 0.21, 'f': 0.79}
Node Q|K|r1|brc|: {'b': 0.0, 'x': 1.0}
Node Q|K|r1|brc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|K|r1|brc|xb: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node Q|K|r1|brc|xbrr: {'c': 0.5, 'f': 0.5}
Node Q|K|r1|brrc|: {'b': 0.03, 'x': 0.97}
Node Q|K|r1|brrc|br: {'c': 0.0, 'f': 0.95, 'r': 0.05}
Node Q|K|r1|brrc|xb: {'c': 0.25, 'f': 0.7, 'r': 0.05}
Node Q|K|r1|brrc|xbrr: {'c': 0.03, 'f': 0.97}
Node Q|K|r1|xbc|: {'b': 0.0, 'x': 1.0}
Node Q|K|r1|xbc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|K|r1|xbc|xb: {'c': 0.46, 'f': 0.46, 'r': 0.08}
Node Q|K|r1|xbc|xbrr: {'c': 0.5, 'f': 0.5}
Node Q|K|r1|xbrc|: {'b': 0.84, 'x': 0.16}
Node Q|K|r1|xbrc|br: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node Q|K|r1|xbrc|xb: {'c': 0.31, 'f': 0.68, 'r': 0.0}
Node Q|K|r1|xbrc|xbrr: {'c': 0.5, 'f': 0.5}
Node Q|K|r1|xbrrc|: {'b': 0.0, 'x': 1.0}
Node Q|K|r1|xbrrc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node Q|K|r1|xbrrc|xb: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node Q|K|r1|xbrrc|xbrr: {'c': 0.5, 'f': 0.5}
Node Q|K|r1|xx|: {'b': 0.75, 'x': 0.25}
Node Q|K|r1|xx|br: {'c': 0.03, 'f': 0.51, 'r': 0.45}
Node Q|K|r1|xx|xb: {'c': 0.78, 'f': 0.16, 'r': 0.06}
Node Q|K|r1|xx|xbrr: {'c': 1.0, 'f': 0.0}
Node K|None|r0||: {'b': 0.57, 'x': 0.43}
Node K|J|r1|bc|: {'b': 0.02, 'x': 0.98}
Node K|J|r1|bc|br: {'c': 0.3, 'f': 0.09, 'r': 0.61}
Node K|J|r1|bc|xb: {'c': 0.78, 'f': 0.21, 'r': 0.01}
Node K|J|r1|bc|xbrr: {'c': 0.37, 'f': 0.63}
Node K|None|r0|br|: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node K|J|r1|brc|: {'b': 0.5, 'x': 0.5}
Node K|J|r1|brc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|J|r1|brc|xb: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|J|r1|brc|xbrr: {'c': 0.5, 'f': 0.5}
Node K|J|r1|brrc|: {'b': 0.1, 'x': 0.9}
Node K|J|r1|brrc|br: {'c': 0.22, 'f': 0.29, 'r': 0.49}
Node K|J|r1|brrc|xb: {'c': 1.0, 'f': 0.0, 'r': 0.0}
Node K|J|r1|brrc|xbrr: {'c': 0.99, 'f': 0.01}
Node K|None|r0|xb|: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node K|J|r1|xbc|: {'b': 0.5, 'x': 0.5}
Node K|J|r1|xbc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|J|r1|xbc|xb: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|J|r1|xbc|xbrr: {'c': 0.5, 'f': 0.5}
Node K|J|r1|xbrc|: {'b': 0.01, 'x': 0.99}
Node K|J|r1|xbrc|br: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node K|J|r1|xbrc|xb: {'c': 1.0, 'f': 0.0, 'r': 0.0}
Node K|J|r1|xbrc|xbrr: {'c': 0.99, 'f': 0.01}
Node K|None|r0|xbrr|: {'c': 1.0, 'f': 0.0}
Node K|J|r1|xbrrc|: {'b': 0.0, 'x': 1.0}
Node K|J|r1|xbrrc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|J|r1|xbrrc|xb: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node K|J|r1|xbrrc|xbrr: {'c': 0.5, 'f': 0.5}
Node K|J|r1|xx|: {'b': 0.0, 'x': 1.0}
Node K|J|r1|xx|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|J|r1|xx|xb: {'c': 0.0, 'f': 1.0, 'r': 0.0}
Node K|J|r1|xx|xbrr: {'c': 0.5, 'f': 0.5}
Node K|Q|r1|bc|: {'b': 0.0, 'x': 1.0}
Node K|Q|r1|bc|br: {'c': 0.42, 'f': 0.16, 'r': 0.42}
Node K|Q|r1|bc|xb: {'c': 0.51, 'f': 0.46, 'r': 0.03}
Node K|Q|r1|bc|xbrr: {'c': 0.04, 'f': 0.96}
Node K|Q|r1|brc|: {'b': 0.5, 'x': 0.5}
Node K|Q|r1|brc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|Q|r1|brc|xb: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|Q|r1|brc|xbrr: {'c': 0.5, 'f': 0.5}
Node K|Q|r1|brrc|: {'b': 0.43, 'x': 0.57}
Node K|Q|r1|brrc|br: {'c': 0.1, 'f': 0.3, 'r': 0.6}
Node K|Q|r1|brrc|xb: {'c': 0.86, 'f': 0.13, 'r': 0.01}
Node K|Q|r1|brrc|xbrr: {'c': 0.0, 'f': 1.0}
Node K|Q|r1|xbc|: {'b': 0.5, 'x': 0.5}
Node K|Q|r1|xbc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|Q|r1|xbc|xb: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|Q|r1|xbc|xbrr: {'c': 0.5, 'f': 0.5}
Node K|Q|r1|xbrc|: {'b': 0.0, 'x': 1.0}
Node K|Q|r1|xbrc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|Q|r1|xbrc|xb: {'c': 0.67, 'f': 0.31, 'r': 0.02}
Node K|Q|r1|xbrc|xbrr: {'c': 0.41, 'f': 0.59}
Node K|Q|r1|xbrrc|: {'b': 0.0, 'x': 1.0}
Node K|Q|r1|xbrrc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|Q|r1|xbrrc|xb: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node K|Q|r1|xbrrc|xbrr: {'c': 0.5, 'f': 0.5}
Node K|Q|r1|xx|: {'b': 0.0, 'x': 1.0}
Node K|Q|r1|xx|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|Q|r1|xx|xb: {'c': 0.01, 'f': 0.99, 'r': 0.0}
Node K|Q|r1|xx|xbrr: {'c': 1.0, 'f': 0.0}
Node K|K|r1|bc|: {'b': 0.86, 'x': 0.14}
Node K|K|r1|bc|br: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node K|K|r1|bc|xb: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node K|K|r1|bc|xbrr: {'c': 1.0, 'f': 0.0}
Node K|K|r1|brc|: {'b': 0.5, 'x': 0.5}
Node K|K|r1|brc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|K|r1|brc|xb: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|K|r1|brc|xbrr: {'c': 0.5, 'f': 0.5}
Node K|K|r1|brrc|: {'b': 0.54, 'x': 0.46}
Node K|K|r1|brrc|br: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node K|K|r1|brrc|xb: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node K|K|r1|brrc|xbrr: {'c': 1.0, 'f': 0.0}
Node K|K|r1|xbc|: {'b': 0.5, 'x': 0.5}
Node K|K|r1|xbc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|K|r1|xbc|xb: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|K|r1|xbc|xbrr: {'c': 0.5, 'f': 0.5}
Node K|K|r1|xbrc|: {'b': 0.82, 'x': 0.18}
Node K|K|r1|xbrc|br: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node K|K|r1|xbrc|xb: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node K|K|r1|xbrc|xbrr: {'c': 1.0, 'f': 0.0}
Node K|K|r1|xbrrc|: {'b': 0.0, 'x': 1.0}
Node K|K|r1|xbrrc|br: {'c': 0.33, 'f': 0.33, 'r': 0.33}
Node K|K|r1|xbrrc|xb: {'c': 0.5, 'f': 0.5, 'r': 0.0}
Node K|K|r1|xbrrc|xbrr: {'c': 0.5, 'f': 0.5}
Node K|K|r1|xx|: {'b': 0.97, 'x': 0.03}
Node K|K|r1|xx|br: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node K|K|r1|xx|xb: {'c': 0.0, 'f': 0.0, 'r': 1.0}
Node K|K|r1|xx|xbrr: {'c': 1.0, 'f': 0.0}
