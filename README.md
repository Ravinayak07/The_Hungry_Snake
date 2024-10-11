# The_Hungry_Snake

- It is snake game made with python prgramming language with the help of pygame module.
- It has two different gaming mode.One is single player mode and another one is 2 players mode.
- It also has a settings tab where you can stop/play the background music.
- The rule of this game is that the snake has to eat the foods without collasping with the wall otherwise the game will be over.
- It also has twilio API integration which sends the score of the user in their whatsapp number.For this the user has to generate their own ID and authToken in the Twilio Console and write those credentilas in the x and y variables in the twiliox function mentioned in the code.

# Things to do before running the code to avoid error:-

> 1.Install pygame and twilio in your IDE.
> 2.For API integration:-

- a)ADD the values of account_sid and auth_token in your enviromental variable which are stored in variables x and y inside the twiliox() function in the code
- b)If you want to enter your own whatsapp number as input from the user,then
  you have to create a connection between the twilio sandbox and your number before running the code.

> 3.How to create conncetion between the twilio sandbox and your number?

- step-1: Save this number(+14155238886) as "Twilio sandbox" in your whatsapp contacts.
- step-2: send a text message("Join two-cowboy") to the above number from your whatsapp number.
- step-3: You will receive a message as "You are all set!......".
- step-4: You have successfully created the connection.Now proceed to run the code.

## Note:If u want to make any changes in the code, use the demo_for_testing.py file.
