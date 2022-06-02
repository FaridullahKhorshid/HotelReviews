def load():
    # 2. horizontal menu with custom style
    from streamlit_option_menu import option_menu
    import streamlit as st

    # 1. as sidebar menu
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", "Prediction"], icons=["house", "gear"], menu_icon="cast", default_index=1)

    if selected == "Home":
        # home.load_view()
        from views import home

        home.load_view()

    if selected == "Prediction":

        from views import prediction

        prediction.load_view()
