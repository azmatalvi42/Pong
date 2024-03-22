# Pong
Dive into the nostalgia of arcade gaming with our Classic Pong Game, a modern rendition of the iconic table tennis simulation that took the world by storm. Crafted with the powerful Pygame library, this game brings to life the simple yet addictive gameplay that has captivated players for generations.

Key Features:

Display Setup: Initializes a Pygame window with dimensions 600x400 pixels and sets its title to "Pong".

Color and Speed Constants: Defines colors for drawing (white for the paddles and ball, black for the background) and sets the initial speed for the ball and the paddles.

Paddle and Ball Mechanics: Implements paddle controls for two players using the W and S keys for the left paddle and the Up and Down arrow keys for the right paddle. The paddles can move vertically within the bounds of the screen.

Ball Dynamics: The ball moves continuously, bouncing off the top and bottom edges of the window and the paddles. If the ball passes a paddle and hits the left or right edge of the window, the opposing player scores a point.

Scoring System: Keeps track of each player's score, displayed at the top of the window. The game resets the ball to the center whenever a point is scored.

Graphics: Utilizes Pygame's drawing functions to render the paddles, the ball, and the score in the game window.
