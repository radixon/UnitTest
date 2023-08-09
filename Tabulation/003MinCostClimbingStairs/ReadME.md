# Minimum Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1. Return the minimum cost to reach the top of the floor.
![minCost](https://github.com/radixon/UnitTest/assets/59415488/a6031955-fb5f-4a2e-98fc-02e9222eb5ec)

# Loop Invariant

## Initialization

Before entering the loop, the variables oneStepBehind and twoStepsBehind are intialized to 0.  There is no cost until a step is taken.  Thus the the algorithm is true prior to the first iteration of the loop.
* cost[i-2] is represented by the variable twoStepsBehind.  twoStepsBehind means two steps behind i.
* cost[i-1] is represented by the variable oneStepBehind.  oneStepBehind means one step behind i.

## Maintenance

At each iteration the minimum cost has to be calculated.  There are two possible cost:
* cost[i] + cost[i-2]
* cost[i+1] + cost[i-1]

Thus the decision is the minimum(cost[i]+twoStepsBehind, cost[i+1]+oneStepBehind).  Due to this being solved iteratively, save twoStepsBehind in a temp variable before updating.

## Termination

After iterating through, the results is stored in oneStepBehine
