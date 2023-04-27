import datetime

import streamlit as st

# Local imports
from utils import get_popular, make_clickable_article_title

# Page metadata
st.set_page_config(
    page_title="NyNews",
    page_icon="🗞️",
    layout="centered",
    menu_items={
        "About": "Comment is free :smiling_imp: :crystal_ball:  \n_but facts are sacred_ :angel: :abacus:"
    },
)


# Page title
st.title("NyNews 🗽")
st.header("Liste des 20 articles les plus populaires ❤️‍🔥")
st.divider()


# Input form
with st.form("popular_form"):
    metric_form = st.selectbox("Quel filtre ?", ("emailed",))
    date_form = st.date_input("Quel jour ?", datetime.date(2023, 4, 7))

    # Button to request data from the backend
    submit_btn = st.form_submit_button("Consultez", type="primary")


# Output display
if submit_btn:
    pop_id = f"{metric_form}7d{date_form.month}{date_form.day}"
    pop_list = get_popular(pop_id)["data"][0]["Articles"]

    # Display each article after reformating it as an hyperlink
    for a in pop_list:
        st.markdown(make_clickable_article_title(a["title"], a["url"]))
