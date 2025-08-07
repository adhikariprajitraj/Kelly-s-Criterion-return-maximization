"""
Kelly's Criterion for Multiple Discrete Outcomes

"""

import numpy as np
import pandas as pd
from scipy.optimize import minimize
import warnings
from typing import List, Dict, Tuple, Optional


class MultiOutcomeKelly:
    """
    Kelly Criterion calculator for multple discrete outcomes.

    Handles both binary outcomes and ternary outcomes (Draw).
    """


    def __init__(self, max_fraction: float = 0.25, min_edge: float = 0.01):
        """
        The arguments here are
        - max_fraction is the max money we bet on a single outcome
        - min_edge is the minimum edge required to place the bet
        """
        self.max_fraction = max_fraction
        self.min_edge = min_edge

    
    def odds_to_prob(self, odds:float) -> float:
        """
        We are convertingg the odds to probability here from the data.
        """
        return 1.0 / odds if odds > 0 else 0.0
    
    def calculate_market_prob(self, odds_dict: Dict[str, float]) -> Dict[str, float]:
        """
        We are calculating the implied probability of the market for the betting odds,
        the odds_dict is the dictionary of the odds for each outcome.

    
        """
        probs = {}
        for outcome, odds in odds_dict.items():
            if odds is not None and odds>0:
                probs[outcome] = self.odds_to_prob(odds)
                
            else:
                probs[outcome] = 0.0

        total_prob = sum(probs.values())
        if total_prob> 0:
            probs = {k: v/total_prob for k,v in probs.items()}
        
        return probs
    

    def calculate_kelly_fractions(self,
                                  odds_dict: Dict[str:float],
                                  true_probs: Dict[str, float]) -> Dict[str,float]:
        """
        Main logic now. To calculate the optimal fractions for the bets.
        """
        outcomes = list(odds_dict.keys())
        n_outcomes = len(outcomes)

        return "Not implemented yet" # TODO: I need to do some theory here.