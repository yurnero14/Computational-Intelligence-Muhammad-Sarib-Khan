# 'Taking inspiration from the puzzle problem and professor's code, defining class 'State'
import logging
from random import seed, choice
from typing import Callable
from gx_utils import *
import random


def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]


class State:
    def __init__(self, data: set):
        self._data = set(data)

    # 'hashing by Frozenset to avoid any mutation'

    def __hash__(self):
        return hash(frozenset(self._data))

    # since the length of lists will be important to find the solution

    def __len__(self):
        return len(self._data)

    def __eq__(self, other):
        return self._data == other._data

    def __lt__(self, other):
        return self._data < other._data

    def __or__(self, other):
        return State(self._data | other._data)

    def __and__(self, other):
        return State(self._data & other._data)

    def __sub__(self, other):
        return State(self._data - other._data)

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return repr(self._data)

    def data(self):
        return self._data

    def copy_data(self):
        return self._data.copy()


# 'Writing Search algorithm for subsequent searches to find the final solution'

def search(
        initial_state: State,
        goal_test: Callable,
        parent_state: dict,
        state_cost: dict,
        priority_function: Callable,
        unit_cost: Callable,
):
    frontier = PriorityQueue()
    parent_state.clear()
    state_cost.clear()

    state = initial_state
    parent_state[state] = None
    state_cost[state] = 0

    while state is not None and not goal_test(state):
        for a in possible_actions():
            new_state = result(state, a)
            cost = unit_cost(a)
            if new_state not in state_cost and new_state not in frontier:
                parent_state[new_state] = state
                state_cost[new_state] = state_cost[state] + cost
                frontier.push(new_state, p=priority_function(new_state))
                logging.debug(f"Added new node to frontier (cost={state_cost[new_state]})")
            elif new_state in frontier and state_cost[new_state] > state_cost[state] + cost:
                old_cost = state_cost[new_state]
                parent_state[new_state] = state
                state_cost[new_state] = state_cost[state] + cost
                logging.debug(f"Updated node cost in frontier: {old_cost} -> {state_cost[new_state]}")
        if frontier:
            state = frontier.pop()
        else:
            state = None

    path = list()
    s = state
    while s:
        path.append(s.copy_data())
        s = parent_state[s]

    logging.info(f"Found a solution in {len(path):,} steps; The number of visited states: {len(state_cost):,} ")
    return list(reversed(path))


def goal_test(state):
    return state == GOAL


def possible_actions():
    return (State(x) for x in P)


def result(state, action):
    return state | action

# 'Breadth First'
logging.getLogger().setLevel(logging.INFO)
for N in [5, 10, 20, 100, 500, 1000]:
    parent_state = dict()
    state_cost = dict()
    GOAL = State(set(range(N)))
    P = problem(N, seed=42)


    def h(state):
        return len(state)


    INITIAL_STATE = State(set())
    logging.info(f'N = {N}')
    final = search(
        INITIAL_STATE,
        goal_test=goal_test,
        parent_state=parent_state,
        state_cost=state_cost,
        priority_function=lambda s: h(s),
        unit_cost=lambda a: 1,
    )
    logging.debug(final)

# 'DEPTH FIRST
logging.getLogger().setLevel(logging.INFO)
for N in [5, 10, 20, 100, 500, 1000]:
    parent_state = dict()
    state_cost = dict()
    GOAL = State(set(range(N)))
    P = problem(N, seed=42)





    INITIAL_STATE = State(set())
    logging.info(f'N = {N}')
    final = search(
        INITIAL_STATE,
        goal_test=goal_test,
        parent_state=parent_state,
        state_cost=state_cost,
        priority_function=lambda s: -len(state_cost),
        unit_cost=lambda a:1
    )
    logging.debug(final)
