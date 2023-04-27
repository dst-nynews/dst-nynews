import datetime

import streamlit as st

from utils import get_popular, get_popular_list, make_clickable_article_title

# Page Metadata
st.set_page_config(
    page_title="NyNews",
    page_icon="🗞️",
    layout="centered",
    menu_items={
        "About": "Comment :crystal_ball: is free :smiling_imp:  \n _but facts_ :abacus: _are sacred_ :angel:"
    },
)


# MAIN AREA #
st.title("NyNews 🗽")
st.header("Liste des 20 articles les plus populaires ❤️‍🔥")
st.divider()


popular_form = st.form("popular_form")
hyperlink_list = st.empty()

with popular_form:
    # st.write("Sélectionner le jour et le filtre")
    metric_form = st.selectbox(
        "Quel filtre ?",
        ("emailed",),
        # label_visibility="hidden",
    )
    date_form = st.date_input(
        "Quel jour ?",
        datetime.date(2023, 4, 7),
        # label_visibility="hidden",
    )

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        pop_id = f"{metric_form}7d{date_form.month}{date_form.day}"
        pop_list = get_popular(pop_id)["data"][0]["Articles"]
        for a in pop_list:
            st.markdown(make_clickable_article_title(a["title"], a["url"]))
