import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

# Add a CSS style to center the title and make it bigger
st.markdown(
    """
    <style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
    }

    .bigger-title {
        font-size: 56px; /* You can adjust the font size as needed */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a container div with the center class to center the title
st.markdown('<div class="center"><h1 class="bigger-title">Time Classification</h1></div>', unsafe_allow_html=True)

st.sidebar.success("Select page above.")
