
import streamlit as st
import templates
# import streamlit_authenticator as stauth
import sqlite3 as sql

import page_1
import page_2
import page_3
import page_4


page_names_to_funcs = {
    "Applicants": page_2,
    "Recruiters": page_1 ,
    "Companies": page_3,
    "Rate a Company": page_4,
}

con = sql.connect('database.db')
c = con.cursor()

# CREATE TABLE new_employee ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL, resume BLOB NOT NULL);

# functions
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS reviewtable(writer TEXT, title TEXT, book TEXT, author TEXT, article TEXT, date DATE, photo BLOB)')

def add_data(writer, title, book, author, article, date):
    c.execute('INSERT INTO reviewtable(writer, title, book, author, article, date) VALUES (?,?,?,?,?,?)',(writer, title, book, author, article, date))
    con.commit()

def view_all_reviews():
    c.execute('SELECT * FROM reviewtable')
    data = c.fetchall()
    return data

def view_all_titles():
    c.execute('SELECT DISTINCT title FROM reviewtable')
    data = c.fetchall()
    return data

def get_review_by_title(title):
    c.execute('SELECT * FROM reviewtable WHERE title="{}"'.format(title))
    data = c.fetchall()
    return data

def get_search(category, term):
    c.execute('SELECT * FROM reviewtable WHERE "{}" LIKE "%{}%"'.format(category, term))
    data = c.fetchall()
    return data

# st.image("images/brooke-cagle-g1Kr4Ozfoac-unsplash.jpg", use_column_width= True)
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(page_names_to_funcs.keys()))
page = page_names_to_funcs[selection]
page.app()

# with open('https://github.com/Olayile/Project_WW/blob/undefined/config.yaml#L1') as file:
#         config = yaml.load(file, Loader=SafeLoader)

#         authenticator = Authenticate(
#             config['credentials'],
#             config['cookie']['name'],
#             config['cookie']['key'],
#             config['cookie']['expiry_days'],
#             config['preauthorized']
#         )
# name, authentication_status, username = authenticator.login('Login', 'main')




############ file authenticators ####################


# import authlib

# data = authlib.auth()  # auth(sidebar=False) or auth(False) if you don't want the sidebar
# """This both displays authentication input in the sidebar, and then returns the credentials for use locally"""

# st.write(f"{'AUTHENTICATED!' if data else 'NOT authenticated'}")
# st.write(
#     f"Authentication data received = {data} (which is the username that has logged in)"
# )



# if __name__ == "__main__":
#     st.write(
#         "Warning, superuser mode\n\nUse this mode to initialise authentication database"
#     )
#     if st.checkbox("Check to continue"):
#         _superuser_mode()