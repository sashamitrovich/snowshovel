# Snowshovel
A Streamlit app for loading data into Snowflake ❄️ that any kindergartener :baby: can use 

This 25 line short Stramlit app does the following:

* Accepts a CSV file via the File Uploader component
* Creates a Pandas DataFrame from this file
* Uses Snowpark to create and load a table on Snowflake from this DataFrame

## Setup:
* Setup your Streamlit environment, as described here: https://quickstarts.snowflake.com/guide/getting_started_with_snowpark_for_python_streamlit/index.html?index=..%2F..index#1
* Configure your Snowflake Snowpark credentials in the creds-sample.json file.
* Run the app with Streamlit run app.py
* After uploading a file, look for the new table in Snowflake in the database and schema you configured in the credentials



![GitHubQuickDemo](https://user-images.githubusercontent.com/15609655/236762568-a62c37bf-b86b-4024-abbf-d66566f4c1fe.gif)
