# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

  When I first ran the game, it looked like a simple dashboard with an input textbox for me to enter in my guess. It also consisted of a sidebar for me to select the difficulty level of the game, and three UI buttons that controlled how I interacted with the game: the submission of my guess, starting a new game, or controlling the visibility of hints that would aid me in guessing. 

  List of Three Bugs:
  1) The hints provided were no longer specific to my guesses after the first guess. When I guessed a number, I expected the game to correctly tell me if I needed to guess higher and lower accordingly. However, it actually told me to guess higher when I should guess lower and lower when I should guess higher. Basically, the hints were swapped.
  
  2) When I pressed the button to start a new game, I expected for the game to be reset (both my number of attempts and my ability to guess a new number. However, a red error type message appeared saying my game had ended and I needed to start a new one. The number of attempts were reset, but the game itself, or rather my ability to interact with it, was not restored. 
  
  3) Not sure if this counts as an error, but I expected the game to tell me to re-guess if I entered a number outside of the [0,100] range. However, it accepted my guess of 200 and returned that frozen/unupdated hint saying to guess higher. 
---

## 2. How did you use AI as a teammate?
We were asked to use the Copilot Chat session for this project. One example of an AI suggestion that was correct was that the new game does not fully reset because the starter code only reset attempts and secret but nor status or history. I verified this result by looking over those relevant session variables and what their state would be after new game was pressed versus what they should be. I then manually updated those variables and ran the application again to see if the bug was fixed, or at least, the impact of it was reduced. One example of an AI suggestion that was incorrect was that it attempted to move the page configuration and sidebar into the logic_utils.py file. The logic_utils.py file is meant to store core logic for the app, not the UI components, so I immediately knew that suggestion was incorrect.
---

## 3. Debugging and testing your fixes
There were two ways in which I decided whether a bug was really fixed. I used Copilot to write tests for the three bugs I identified, and if those tests did not pass and the provided tests did not pass, the bug was not fixed. If they did pass, I then ran the actual app to see if the implementation worked as expected. If it did, then I knew the bug was really fixed. One test that I ran was def test_new_game_no_crash(): and it basically showed me whether all the session relevant variables were actually reset after the new game reactive button was pressed. AI helped me design the tests by giving me starter code for them that I then tweaked to either be more thorough (when I felt like obvious edge cases were not being checked) or less complex.
---

## 4. What did you learn about Streamlit and state?
Streamlit is a script that reruns the code from line one every time you interact with an app, through for example, button clicks. Since it restarts the whole file, all variables created are basically wiped from memory and reset to their original values. The app starts at a blank slate, meaning it has no recollection of past variable history. It has amnesia. A session state can be equated to short term memory. It's the only piece that survives the memory reset initiated by streamlit and it holds data from the app's last run for it to refer to. You could think of it as a notes sheet or tally record for the score of each team during an ongoing football game after each play.
---

## 5. Looking ahead: your developer habits
One habit from this project I want to reuse in future projects is not blindly accepting the suggestions given by AI. I want AI to support me in my projects but not write my project for me, otherwise I will not be able to understand or explain it or debug it. I want to carefully prompt it so that it will guide me, but not write all my fixes for me. If I do not build enough base knowledge to determine whether a suggestion AI provides is helpful or detrimental, then I may set back the progress of my project even more. 
One thing I would do differently with this project next time is ask AI to explain more of the code to me so that I can understand what it was meant to do. Additionally, I also want to remember to ask AI why it belives the changes it suggests are the best fixes. I think this project helped me see that not all AI generated is bad and that AI generated code has come a long way from when I first tried asking Chat GPT to help me back in 11th grade. However, the suggestions provided by AI are influenced by the prompts I give it, so knowing how to constructively prompt is a skill I need to develop.
