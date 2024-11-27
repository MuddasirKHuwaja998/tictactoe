import streamlit as st

# Initialize session states for game data
if "board" not in st.session_state:
    st.session_state.board = [""] * 9  # 3x3 empty board
    st.session_state.current_player = "Muddasir"
    st.session_state.wins_muddasir = 0
    st.session_state.wins_maryam = 0
    st.session_state.tie_games = 0

# Reset game function
def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.current_player = "Muddasir"

# Check winner function
def check_winner():
    b = st.session_state.board
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6],            # Diagonals
    ]
    for condition in win_conditions:
        if b[condition[0]] == b[condition[1]] == b[condition[2]] and b[condition[0]] != "":
            return b[condition[0]]
    if "" not in b:  # If no spaces are left, it's a tie
        return "Tie"
    return None

# Handle player's move
def make_move(index):
    if st.session_state.board[index] == "":
        st.session_state.board[index] = "X" if st.session_state.current_player == "Muddasir" else "O"
        winner = check_winner()
        if winner:
            if winner == "X":
                st.session_state.wins_muddasir += 1
                st.success("🎉 Muddasir wins!")
            elif winner == "O":
                st.session_state.wins_maryam += 1
                st.success("🎉 Maryam ❤️ wins!")
            else:
                st.session_state.tie_games += 1
                st.info("It's a tie!")
            reset_game()
        else:
            # Switch player
            st.session_state.current_player = "Maryam ❤️" if st.session_state.current_player == "Muddasir" else "Muddasir"

# App layout
st.title("Tic Tac Toe 🎮")
st.subheader("Play online: Muddasir vs Maryam ❤️")
st.write("**Current Player:**", st.session_state.current_player)

# Display scoreboard
st.sidebar.title("Scoreboard")
st.sidebar.write(f"**Muddasir:** {st.session_state.wins_muddasir}")
st.sidebar.write(f"**Maryam ❤️:** {st.session_state.wins_maryam}")
st.sidebar.write(f"**Ties:** {st.session_state.tie_games}")

# Custom styles for the game grid and buttons
grid_style = """
    <style>
        .tic-tac-toe-btn {
            width: 100px;
            height: 100px;
            font-size: 36px;
            border: 2px solid #000000;
            margin: 5px;
            background-color: #F8D7DA;  /* Light pink background */
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            text-align: center;
        }
        .tic-tac-toe-btn:hover {
            background-color: #F1B4C4;  /* Slightly darker pink on hover */
        }
        .tic-tac-toe-btn:focus {
            outline: none;
        }
        .tic-tac-toe-row {
            display: flex;
            justify-content: center;
            margin-bottom: 5px;
        }
    </style>
"""
st.markdown(grid_style, unsafe_allow_html=True)

# Create the Tic Tac Toe grid with color and borders
st.write("---")

# Display the board
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        index = i * 3 + j
        with cols[j]:
            button_label = st.session_state.board[index] if st.session_state.board[index] else " "
            if st.button(button_label, key=index, help="Click to make your move!", use_container_width=True, on_click=make_move, args=(index,)):
                pass
st.write("---")

# Reset button
if st.button("Restart Game"):
    reset_game()
