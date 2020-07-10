Used Modules: pygame, random and time.

STEP 1: Start

STEP 2: Initialize all packages such as pygame , random , time.

STEP 3: Initialize all imported pygame modules using pygame.init().

STEP 4: Assigning screen size with pixels 1366 X 768.

STEP 5: Initialize a window or screen for display and update portions of the screen for software display using pygame.display.set_mode() and pygame.display.update() for updating.

STEP 6: Loading appropriate images and mixer using pygame.image.load ()and pygame.mixer.Sound() such as Snake_and_ladders_board, dice1, dice2, dice3, dice4, dice5, dice6,redcoin,bluecoin,greencoin,yellowcoin,home_background,play_background, intropic, intropic1, intropic2, intropic3, intropic4, intropic5, credits and music, snake ,win ,lose ,ladder.

STEP 7 : Setting the mouse cursor position , Getting the state of mouse button using pygame.mouse.get_pos() and pygame.mouse.get_pressed().

STEP 8 : buttontext_display() is a function defined for drawing the text font , text position , text size and rectangle in the current display section.

STEP 9: buttontext_object() is a function defined for creates new surface for the specified text rendered on it . There is no way to directly draw text on existing surface .

STEP 10: comments_display() is a function defined for adding text color for given the text font , text position , text size and rectangle in the current display section .

STEP 11: comment_objects() is similar to buttontext_object() function but it returns the size and object of the rendered text.

STEP 12: Assigning pixels of the small boxes in the board. Returning the pixels for the coin for perfect fiting where it moves using def coin(a) .

STEP 13: Assigning conditions for the ladders and snakes using def ladder() and def snake() function .

STEP 14: Using appropriate dice pictures for given value a .

STEP 15: Get the current time in millisecond and it is asssigned to time by time variable and creating a loop to display the dice picture while the given condition pygame.time.get_ticks() - time < 1000 becomes false.

STEP 16: The function def menu_button(), playscreen_button() set the mouse cursor position and get the state of the mouse button and it states the condition it draws the button like a rectangle for given width and height .

STEP 17: Assigning the function for play music, mute music, play, quit buttons.

STEP 18: It generating random numbers from 1 to 6 and it saves in the variable a if a == 6 it assigns six = True otherwise six = False p = dice(a) is a function call for selecting appropriate image and display the image.

STEP 19: Incrementing the score by score += a.

If the score is <=100 it makes a function ans returns the particular value and if given value is != score assigning l= true and plays the ladder sound like this snake function also created.

Otherwise it displays the message as can’t move when it has no space to move.

The message is displayed by a function call.

STEP 20: Creating a quit function using pygame.quit().

STEP 21: Calling the appropriate function call using the b value and it draws the rectangular button otherwise it gives a message by using a function call buttontext_display().

STEP 22: Function intro first assign a current time as time display the intro picture by while pygame.time.get_ticks() - time < 2500 becomes false and it shows the intro picture continuously when it satisfy the while pygame.time.get_ticks() - time < 500 the condition .

STEP 23: Creating a loop for get a events from queue and if event.type==pgame.KEYDOWN it returns the pygame.dispaly.update() .

STEP 24: Credit is a function is used for displaying credit image and returns the pygame.display.update() and assigning conditions for the graphics .

STEP 25: Main() is a function is used for playing game music and it is used for displaying the play , quit and play music , mute music and credits as a rectangular button and for selecting the particular buttons .

STEP 26: Options() is a function is used for displaying single player ,2 players ,3 players ,4 players as a rectangular button and also for selecting the particular buttons .

STEP 27: play() is a function which is used for moving the coin from the initial position and giving chance to play for other player when the player gets the number 5 or 6 then it gives another chance to roll the dice.  It throws a message when there is a ladder or snake like “there’s a ladder” or “there’s snake .

STEP 28: Finally it announces the winning player like player-x win .

STEP 29: End
