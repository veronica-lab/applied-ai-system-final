# 🎮 Game Glitch Investigator — Applied AI System

## 🧠 Overview
This project is a Python-based number guessing game built with Streamlit.  
The goal was to investigate bugs in an AI-generated game, fix them, and improve reliability by refactoring the logic into modular components and adding tests.

The system demonstrates:
- Debugging and bug identification
- Modular design using `logic_utils.py`
- AI-assisted problem solving
- Reliability testing with pytest

---

## 🎯 Game Purpose
The user selects a difficulty level and guesses a number within a range.  
The game provides hints ("Too High" / "Too Low") and tracks score based on performance.

---

## 🐛 Bug Reproduction Evidence

Before fixes, the game had several issues:

- Score did not update correctly after guesses
- Secret number could change unexpectedly during gameplay
- Input validation failed for invalid or empty inputs

📸 Screenshots of these issues are included in the `/assets` folder.

---

## 🐞 Bugs Found (Expected vs Actual)

### Bug 1: Score not updating correctly
- **Expected:** Score increases when the player wins and decreases for wrong guesses  
- **Actual:** Score remained inconsistent or unchanged  
- **Cause:** Score logic was incorrectly implemented inside the main app loop  

---

### Bug 2: Secret number changing during gameplay
- **Expected:** Secret number stays the same during a game session  
- **Actual:** Secret number changed after each interaction  
- **Cause:** Streamlit reruns the script, and the secret number was not stored in `st.session_state`  

---

### Bug 3: Invalid input not handled properly
- **Expected:** Game should reject non-numeric or empty input  
- **Actual:** Game crashed or behaved unpredictably  
- **Cause:** No proper input parsing or validation  

---

## 🔍 Code-Level Causes

- Game logic was tightly coupled with UI code in `app.py`
- No separation between logic and interface
- No structured validation for inputs
- Missing state management for persistent variables

---

## 🔧 Fixes Applied

### Fix 1: Refactored logic into `logic_utils.py`
- Moved core functions:
  - `parse_guess`
  - `check_guess`
  - `update_score`
  - `get_range_for_difficulty`
- This made the system modular and testable

---

### Fix 2: Implemented session state for secret number
- Used `st.session_state` to persist the secret value
- Prevented it from resetting on every interaction

---

### Fix 3: Added input validation
- Implemented parsing and range checks
- Prevented crashes from invalid input

---

## 🤖 AI Debugging Review

### ✅ Helpful AI Suggestion
AI correctly identified that the score was not updating due to missing logic inside the guess-handling flow.

### ❌ Incorrect AI Suggestion
AI suggested the issue was related to UI rendering rather than logic.  
This was incorrect because the bug was caused by missing or misplaced logic, not display issues.

---

## 🧪 Post-Fix Demo

After implementing fixes:
- Game runs without crashing  
- Score updates correctly  
- Input validation works as expected  
- Secret number remains consistent  

📸 Screenshots included in `/assets`

---

## 🧪 Pytest Results

Unit tests were added for:
- Guess checking
- Input parsing
- Range validation
- Score updates

All tests pass successfully.

📸 Screenshot of pytest results included in `/assets`

---

## ⭐ Stretch Features

- Modular architecture using `logic_utils.py`
- Automated testing with pytest
- Clean separation between logic and UI
- Improved reliability and input handling

---

## 🧠 Reflection

This project showed that AI can be helpful for identifying bugs quickly, but it is not always accurate.  
Some suggestions were useful, while others were misleading and required manual verification.

Breaking the code into smaller, testable components made debugging much easier and improved overall system reliability.

---

## 📂 Project Structure
applied-ai-system-final/
│
├── app.py
├── logic_utils.py
├── tests/
│ └── test_game_logic.py
├── assets/
├── README.md
└── reflection.md



---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python -m streamlit run app.py