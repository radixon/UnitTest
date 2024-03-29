# Minimum Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of i<sup>th</sup> step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.  Return the minimum cost to reach the top of the floor.
![MinCost](https://github.com/radixon/UnitTest/assets/59415488/80e7c720-6f9b-49ca-b88a-205aecbaa762)

# Intuition

There is a window of fixed size 2.  In each window, find the minimum cost to jump one step past the window.  If there is another cost at the new location, slide the window by an increment of one, and add the minimum cost to arrive at that location to the location cost to know the minimum cost to leave the location.  If there isn't a cost outside the window, return the minimum cost found to reach just outside the location.

![example](https://github.com/radixon/UnitTest/assets/59415488/f65cc9a2-bc70-4820-84b1-57c04cc7ae8b)

# Loop Invariant

## Initialization

Before entering the loop, the variables oneStepBehind and twoStepsBehind are intialized to 0.  There is no cost before entering the cost array.  Thus the the algorithm is true prior to the first iteration of the loop.

## Maintenance

At each iteration, determine if the cost is lower to get to i+2 from cost[i] or cost[i+1].  Add min(cost[i],cost[i+1]) to cost[i+2] while i+2 < cost.length.

## Termination

Once i+2 == cost.length, return min(cost[i],cost[i+1])
