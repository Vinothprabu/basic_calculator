import streamlit as st

# Page config
st.set_page_config(page_title="🧮 Calculator", layout="centered")

# Better CSS
st.markdown(
    """
    <style>
    div[data-baseweb="input"] input {
        font-size: 36px !important;
        height: 45px !important;
        text-align: right !important;
        padding: 10px !important;
        box-shadow: inset 3px 3px 6px #aaa,
                    inset -3px -3px 6px #fff !important;
        color: #333 !important;
        font-weight: bold !important;
    }

    div.stButton > button {
        font-size: 28px !important;
        font-weight: bold !important;
        height: 70px !important;
        width: 100% !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 2px 2px 6px #aaa, -2px -2px 6px #fff !important;
        transition: 0.2s;
    }

    div.stButton > button:hover {
        background-color: #e0e0e0 !important;
        transform: scale(1.03);
    }

    div.stButton > button:active {
        transform: scale(0.97);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🧮 Basic Calculator")

# Session state initialization
st.session_state.expression = st.session_state.get("expression", "")
st.session_state.last_result = st.session_state.get("last_result", None)
st.session_state.after_equals = st.session_state.get("after_equals", False)

# Press function
def press(key):
    if key == "C":
        st.session_state.expression = ""
        st.session_state.last_result = None
        st.session_state.after_equals = False
    elif key == "⌫":
        st.session_state.expression = st.session_state.expression[:-1]
        st.session_state.after_equals = False
    elif key == "=":
        try:
            result = str(eval(st.session_state.expression))
            st.session_state.last_result = result
            st.session_state.expression = result
            st.session_state.after_equals = False
        except:
            st.session_state.expression = "Error"
            st.session_state.after_equals = True
    else:
        if st.session_state.after_equals and not any(op in st.session_state.expression for op in ['+', '-', '*', '÷']):
            st.session_state.expression = ""
            st.session_state.after_equals = False
        st.session_state.expression += str(key)

# Input display
st.text_input("Calculator Display",
              value=st.session_state.expression,
              key="display",
              disabled=True,
              label_visibility="hidden")

# Buttons with explicit labels
buttons = [
    ["7", "8", "9", "➕", "⌫"],
    ["4", "5", "6", "➖", "C"],
    ["1", "2", "3", "✖️", "("],
    ["0", ".", "=", "➗", ")"]
]

# Layout
for row_index, row in enumerate(buttons):
    cols = st.columns(len(row))
    for col_index, label in enumerate(row):
        key = label
        if label == "➕":
            op = "+"
        elif label == "➖":
            op = "-"
        elif label == "✖️":
            op = "*"
        elif label == "➗":
            op = "/"
        else:
            op = label

        with cols[col_index]:
            if st.button(label, key=f"btn_{row_index}_{col_index}_{key}", on_click=press, args=(op,)):
                pass