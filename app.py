import random
import streamlit as st
#broken here
def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 50


def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

#new function to validate guess is within range
def validate_range(value: int, low: int, high: int):
    if value < low:
        return False, f"Number must be at least {low}."
    if value > high:
        return False, f"Number must be no more than {high}."
    return True, None


def check_guess(guess, secret):
    try:
        secret_int = int(secret)
    except (ValueError, TypeError):
        secret_int = secret

    if guess == secret_int:
        return "Win", "🎉 Correct!"
    if guess > secret_int:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# Initialize session state variables if not already set
if "difficulty" not in st.session_state:
    st.session_state.difficulty = difficulty

if st.session_state.difficulty != difficulty:
    st.session_state.difficulty = difficulty
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.summary = []
    st.session_state.wrong_streak = 0
    st.session_state.secret_revealed = False
    candidates = [n for n in range(st.session_state.secret - 5, st.session_state.secret + 6)
                  if n != st.session_state.secret and low <= n <= high]
    st.session_state.fake_secret = random.choice(candidates) if candidates else None

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "summary" not in st.session_state:
    st.session_state.summary = []

if "wrong_streak" not in st.session_state:
    st.session_state.wrong_streak = 0

if "secret_revealed" not in st.session_state:
    st.session_state.secret_revealed = False

if "fake_secret" not in st.session_state:
    candidates = [n for n in range(st.session_state.secret - 5, st.session_state.secret + 6)
                  if n != st.session_state.secret and low <= n <= high]
    st.session_state.fake_secret = random.choice(candidates) if candidates else None

st.subheader("Make a guess")

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", f"{st.session_state.fake_secret} (valid range: {low}–{high})")
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

with st.form("guess_form"):
    raw_guess = st.text_input(
        "Enter your guess:",
        key=f"guess_input_{difficulty}"
    )
    col1, col2 = st.columns(2)
    with col1:
        submit = st.form_submit_button("Submit Guess 🚀")

col_ng, col_hint, col_reveal = st.columns(3)
with col_ng:
    new_game = st.button("New Game 🔁")
with col_hint:
    show_hint = st.checkbox("Show hint", value=True)
with col_reveal:
    reveal_enabled = st.session_state.wrong_streak >= 3
    reveal_secret = st.button("Reveal Secret 🔍", disabled=not reveal_enabled)
    if not reveal_enabled:
        st.caption(f"{3 - st.session_state.wrong_streak} wrong answer(s) needed to unlock")

if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.summary = []
    st.session_state.wrong_streak = 0
    st.session_state.secret_revealed = False
    candidates = [n for n in range(st.session_state.secret - 5, st.session_state.secret + 6)
                  if n != st.session_state.secret and low <= n <= high]
    st.session_state.fake_secret = random.choice(candidates) if candidates else None
    st.rerun()

if reveal_secret:
    st.session_state.score -= 3
    st.session_state.secret_revealed = True

if st.session_state.secret_revealed:
    st.warning(f"The secret number is **{st.session_state.secret}** (-3 points penalty).")

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
        st.stop()

    in_range, range_err = validate_range(guess_int, low, high)
    if not in_range:
        st.session_state.attempts -= 1
        st.error(range_err)
        st.stop()

    st.session_state.history.append(guess_int)

    if st.session_state.attempts % 2 == 0:
        secret = str(st.session_state.secret)
    else:
        secret = st.session_state.secret

    outcome, message = check_guess(guess_int, secret)

    if show_hint:
        st.warning(message)

    st.session_state.score = update_score(
        current_score=st.session_state.score,
        outcome=outcome,
        attempt_number=st.session_state.attempts,
    )

    st.session_state.summary.append({
        "Attempt": st.session_state.attempts,
        "Guess": guess_int,
        "Result": message,
        "Score After": st.session_state.score,
    })

    if outcome == "Win":
        st.session_state.wrong_streak = 0
        st.balloons()
        st.session_state.status = "won"
        st.success(
            f"You won! The secret was {st.session_state.secret}. "
            f"Final score: {st.session_state.score}"
        )
    else:
        st.session_state.wrong_streak += 1
        if st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"
            st.error(
                f"Out of attempts! "
                f"The secret was {st.session_state.secret}. "
                f"Score: {st.session_state.score}"
            )

if st.session_state.summary:
    st.divider()
    st.subheader("Session Summary")
    st.caption(f"Difficulty: {difficulty} | Range: {low}–{high} | Attempts allowed: {attempt_limit}")
    st.table(st.session_state.summary)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")