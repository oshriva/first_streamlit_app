import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


streamlit.title('My new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥑 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🥗 🐔 🍞 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')  

my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

# Display the table on the page.

fruits_to_show = my_fruit_list.loc[fruits_selected]


streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
#streamlit.text(fruityvice_response.json())

def get_fruity_vice_data(this_fruit_choice):
    fruit_choice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruit_choice_response.json())
    return fruityvice_normalized

try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please input choice of fruit")
    else:
        back_from_function=get_fruity_vice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
        
except URLError as e:
  streamlit.error()
  
    
    
  

#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)

# write your own comment -what does the next line do? 

# write your own comment - what does this do?

def insert_snowflake_rows(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')")
        return "Thanks for adding" + new_fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button ('Add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlist.secrets["snowflake"])
    back_from_function = insert_snowflake_rows(add_my_fruit)
    streamlit.text(back_from_function)

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)
fruit_choice2 = streamlit.text_input('What fruit would you like information about?','Jackfruit')
streamlit.write('Thanks for chooseing ', fruit_choice2)

my_cur.execute ("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values('From Streamlit')" )
