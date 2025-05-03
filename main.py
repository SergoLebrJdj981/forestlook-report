
import os
import streamlit.web.bootstrap

filename = os.path.join(os.path.dirname(__file__), "app.py")
streamlit.web.bootstrap.run(filename, "", [], {})
