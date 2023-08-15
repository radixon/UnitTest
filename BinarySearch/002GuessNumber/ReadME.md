# Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:<br /><br />
I pick a number from 1 to n. You have to guess which number I picked.  Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API self.guess(num: int), which returns three possible results:
* -1: Your guess is higher than the number I picked (i.e. num > pick).
* 1: Your guess is lower than the number I picked (i.e. num < pick).
* 0: your guess is equal to the number I picked (i.e. num == pick). <br /><br />

Return the number that I picked.
