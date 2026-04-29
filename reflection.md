# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  -The "press enter to apply" message was misleading as the program didn't take the action
  - it's not recording attemps after the 1st one
  - not accepting new game option
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  "for this program, when submitting an answer, it is supposed to work the click button to submit guess, It doesnt do it. Make the program accept the user to click enter button to submit a guess"
   - Replace st.text_input with st.form so pressing Enter triggers submission:
  I tested this by in all three levels test the button was actually working

  "the "new play button" is not working make it accept new requests
  "change, we have only three difficulty modes. get_range_for_difficulty to:  "easy" still return 1,20; "normal" to return 1,50; and hard to return 1,100"
   -get_range_for_difficulty — Normal now returns 1,50, Hard returns 1,100
New Game button — now picks a secret using the correct low/high for the current difficulty, and also resets status, score, and history so the game fully restarts
Info banner — now shows the actual range ({low} and {high}) instead of the hardcoded 1 and 100
I tested this multiple amount of times in all three levels by playing the actual game




- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

--- "in developer tools, the secret is giving a number that is incoherent with the rank of each level, make the secret an actual clue to the numbers" 
  the goal with this suggestion was to make "Secret" give a coherent clue based on the level you were at, not a number higher or lower than what level you were playing, instead what AI did was to give the right number. I fixed this by adding a "show right number" button which can be activated after 3 wrong answers in a row and then by explaining how it is supposed to work " in the section Developer Debug info, also hide the answer and ONLY make it a clue, from the correct number the Secret should be a random number 5 number before or after the right number. make this for each game. Secret shouldn't give the right number never"

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
after testing it different times with different cases 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
a test i ran manually was checking if Secret was giving the right number or a clue, I did this by playing the game and all its levels to check.
- Did AI help you design or understand any tests? How?
x


---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing because Streamlit reruns the script after user interactions. If the secret number is created with random.randint() outside session state, it can reset every time the user submits a guess. I fixed this by storing the secret number inside st.session_state so it stays stable until the user starts a new game. 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns your app every interaction 
- What change did you make that finally gave the game a stable secret number?
i implemented a button for the right answer and then I was very specific that it has to be a random number 5 numbers after or before the right answer, never the actually right answer. At some point Secret was changing to 5 numbers after the last number inputed so i had to delete that change 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Being very specific and have an idea of where the problem is coming from

- What is one thing you would do differently next time you work with AI on a coding task?
not knowing what the program does and how its being changed while im working on it 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I used to think it could either be really good or really bad as many people use it without knowing what they're building which can save some time but create a big mess if you don't know what is going on. This project showed me that there is a possibility to be in between and help your code with ai without relying on it entirely 
