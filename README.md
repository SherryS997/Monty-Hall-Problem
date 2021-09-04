# Monty Python Problem

## Introduction

The Monty Hall problem is a brain teaser, in the form of a probability puzzle, loosely based on the American television game show Let's Make a Deal and named after its original host, Monty Hall. The problem was originally posed (and solved) in a letter by Steve Selvin to the American Statistician in 1975. It became famous as a question from reader Craig F. Whitaker's letter quoted in Marilyn vos Savant's "Ask Marilyn" column in Parade magazine in 1990:

>Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

Vos Savant's response was that the contestant should switch to the other door. Under the standard assumptions, contestants who switch have a 2/3 chance of winning the car, while contestants who stick to their initial choice have only a 1/3 chance.

When the player first makes their choice, there is a 2/3 chance that the car is behind one of the doors not chosen. This probability does not change after the host opens one of the unchosen doors. When the host provides information about the 2 unchosen doors (revealing that one of them does not have the car behind it), the 2/3 chance that the car is behind one of the unchosen doors rests on the unchosen and unrevealed door, as opposed to the 1/3 chance that the car is behind the door the contestant chose initially.

-*From Wikipedia*

## My Implementation

In `simulation.py`, you can test out the game for any desired doors. The simulation puts you as the player and outputs the result based on your choices. The simulation also outputs the probability of winning if you had chosen to switch when asked.

In `multi_sim.py`, you can test out the game for any desired number of times. The required inputs are the number of simulations, number of doors, and whether the simulations should switch or not in the form of 1 and 0. The simulation will output the number of victories and the percentage of victories.
