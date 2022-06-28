<h1> Scripting-TicTacToe </h1>
<p> A simple python scripting program which implements the famous 'Tic Tac Toe' game. </p>

<h1> Step 1: Creating Blank Tables </h1>
<p>
  We start by creating a 2-D list, of 3X3 dimensions. Each value is set to "_". This represents our blank tic tac toe table. <br>
  Then we create another 2-D list with same dimensions where each value is set to False. This is used to tell if a certain position in blank table is occupied or not.
</p>

<h1> Step 2: Creating Players </h1>
<p>
  <ol>
    <li> Create two constants that will hold the the marks of the game. </li>
    <li> Use input() function two times to ask for user names. </li>
    <li> Create an interger variable with value set to 0. We will use this to identify which user's turn it is. </li>
    <li> Create 3 other variables, current_player and current_player_mark, and winning_player. All are empty strings. </li>
    <li> If identifier is even, its player1's turn, else player2's turn. Assign values to current_player and current_player_mark based on this check. </li>
  </ol>
</p>

<h1> Step 3: Mark the Table </h1>
<p>
  Ask user to enter the cell index he want to place his mark at. Replace it with the current player's mark, while showing which player's turn it is. <br>
  Then set the value to True for that index in the second 2-D List we created in step 2. <br>
  Before assinging the mark, check the value for that index in 2-D list of boolean values. 
  If it is False, only then the player can place his mark. If it is True, just increment identifier by 1. So that same player's turn remains.
  <br>
</p>

<h1> Step 4: Define the Loop </h1>
<p>
  Since step 3 activity needs to happen again and again, we run a while loop, based on a boolean, which will be set to false, only one on player wins. <br>
  The other condition for the loop to end is that table is completely filled. In the starting of this loop, we use increment identifier by 1.
</p>

<h1> Step 5: Checking the Winner </h1>
<p>
  We create a function where we need to check the winner. We iterate the tic tac toe table in four ways. <br>
  Row traversal, column traversal, first diagnol traversal and second diagnol traversal. 
  In each traversal we check if either mark appears 3 times. Then return 1 if player1 wins, otherwise return 2. If none won, we return "continue".
</p>

<h1> Step 6: End of Current Game Loop. Play Again </h1>
<p>
  Assign the winning_player variable a value based on the value returned from winner check function. Print the winner. 
  Nest everything except winner check function inside another while loop. At the end of it, ask to play again.
</p>

<h1> Step 7: Improve User Experience (Optional)</h1>
<p>
  When we are asking for user to play again, we can ask them if they want to continue with same players or new players, and use a boolean variable to keep track of it.
  <br>
  If it is true, we ask players for name in game loop, otherwise not. We can also create a separate function for printing our table. <br>
  Remember, at end of each game, i.e., in each new iteration of outer while loop, both 2-D lists need to be set to their default value.
</p>
