import datetime

import streamlit as st

from utils import get_popular, get_popular_list, make_clickable_article_title


st.set_page_config(
    page_title="NyNews",
    page_icon="🗞️",
    layout="centered",
    menu_items={
        "About": "Comment :crystal_ball: is free :smiling_imp:  \n _but facts_ :abacus: _are sacred_ :angel:"
    },
)


st.title("NyNews 🗽")
st.header("Liste des 20 articles les plus populaires ❤️‍🔥")
st.divider()

with st.form("popular_form"):
    metric_form = st.selectbox("Quel filtre ?", ("emailed",))
    date_form = st.date_input("Quel jour ?", datetime.date(2023, 4, 7))

    submit_btn = st.form_submit_button("Consultez", type="primary")

if submit_btn:
    pop_id = f"{metric_form}7d{date_form.month}{date_form.day}"
    pop_list = get_popular(pop_id)["data"][0]["Articles"]

    for a in pop_list:
        st.markdown(make_clickable_article_title(a["title"], a["url"]))
