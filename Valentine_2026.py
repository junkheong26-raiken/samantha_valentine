#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

# Page configuration (mobile friendly)
st.set_page_config(
    page_title = "❤️ To my Beloved Samantha ❤️", 
    page_icon= "💕",
    layout="centered"
)

# Hearts at the Top
st.markdown(
    """
    <style>
    .petal {
        position: fixed;
        top: -10px;
        font-size: 22px;
        animation: fallDown 7s linear infinite;
        z-index: 9999;
    }

    @keyframes fallDown {
        0% {
            transform: translateY(0) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: translateY(110vh) rotate(360deg);
            opacity: 0;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Pink theme
st.markdown(
    """
    <style>
    /* Full app background */
    .stApp {
        background-color: #fff0f6;
    }

    /* Main content area */
    section.main {
        background-color: #fff0f6;
    }

    h1, h2, p {
        color: #7a1f5c;
        font-family: 'Trebuchet MS', sans-serif;
    }

    .stButton > button {
        background-color: #ff8fab;
        color: white;
        border-radius: 20px;
        height: 3em;
        width: 100%;
        font-size: 16px;
        border: none;
    }

    .stButton > button:hover {
        background-color: #ff5c8a;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Soft Background Music

# Music
st.markdown(
    "<p style='text-align:center; color: #7a1f5c; '>🎵 Tap play for music </p>",
    unsafe_allow_html=True
)

st.audio(
    "mirai_nikki.mp3",
    format="audio/mp3",
    loop=True
)

# Love letter

st.markdown(
    """
    <h1 style="text-align: center;" >Pookie~ 🌸🌸🌸 </h1>
    <p style ="text-align: center; font-size: 18px;">
    Days have been more fun, brighter and warmer being together with you~ 😳🥰 <br>
    I might sometimes be a little shy and slow to say how I feel... <br>
    but I hope you know you mean so so much to me~ 💜💜💜
    </p>
    """,
    unsafe_allow_html=True
)

# Centered Image

col_img_left, col_img_center, col_img_right = st.columns([1, 2, 1])

with col_img_center:
    st.image(
        "christmas_2025.jpg",
        caption="One of the best moments is to look at you smiling and laugh~ you were dazzling in the red bowtie dress~ 💜😘",
        width=300
    )

st.markdown("<br>", unsafe_allow_html=True)

# Question to Be Valentine

st.markdown(
    """
    <h2 style="text-align: center; ">Can I please ask... </h2>
    <h2 style="text-align: center; ">Will you be my Valentine? 💌 </h2>
    """,
    unsafe_allow_html=True
)


# Button Logic

if "answered" not in st.session_state:
    st.session_state.answered = False

col_left, col_yes, col_spacer, col_no, col_right = st.columns([1, 2, 0.5, 2, 1])

with col_yes:
    if st.button("Yes 💜❤️🩷💛💚🩵") and not st.session_state.answered:
        st.session_state.answered = True

        # Falling petals 🌸
        st.markdown(
            """
            <div class="petal" style="left:10%;">🌸</div>
            <div class="petal" style="left:25%;">🌷</div>
            <div class="petal" style="left:40%;">🌸</div>
            <div class="petal" style="left:55%;">🌷</div>
            <div class="petal" style="left:70%;">🌸</div>
            <div class="petal" style="left:85%;">🌷</div>
            """,
            unsafe_allow_html=True
        )

        st.success(
            "Yay~ Hehe I can’t wait to spend more time together with you 😘💜 "
            "I’m super happy you said yes 🌸~ Love you lots and lots 🩷"
        )

with col_no:
    if st.button("No~ 🥲🥹🥺") and not st.session_state.answered:
        st.session_state.answered = True
        st.balloons()
        st.info(
            "HAHAHA you naughty~ 😆💜 "
            "I’m still bringing you to many adventures in the future and yummy yummy food~ 😘"
            "Me love you 😳❤️~",
            icon="💌"
        )


# In[ ]:




