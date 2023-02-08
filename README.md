# Snowshovel
A Streamlit app for loading data into Snowflake ❄️ that any grandma :older_woman: can use 

This 25 line short Stramlit app does the following:

* Accepts a CSV file via the File Uploader component
* Creates a Pandas DataFrame from this file
* Uses Snowpark to create and load a table on Snowflakefrom this DataFrame

## Setup:
* Setup your Streamlit environment, as described here: https://quickstarts.snowflake.com/guide/getting_started_with_snowpark_for_python_streamlit/index.html?index=..%2F..index#1
* Configure your Snowflake Snowpark credentials in the creds-sample.json file.
* Run the app with Streamlit run app.py
* After uploading a file, look for the new table in Snowflake in the database and schema you configured in the credentials


https://user-images.githubusercontent.com/73932533/217540301-6a7ec5f3-4fec-489c-b7eb-889143e857d1.mov

