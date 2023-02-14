# Get numeric columns
import snowflake.snowpark as snowpark
import streamlit as st
# import snowflake.snowpark.functions as F
import snowflake.snowpark.types as T

def describeSnowparkDF(snowpark_df: snowpark.DataFrame):
    
    st.write("Here's some stats about the loaded data:")
    numeric_types = [T.DecimalType, T.LongType, T.DoubleType, T.FloatType, T.IntegerType]
    numeric_columns = [c.name for c in snowpark_df.schema.fields if type(c.datatype) in numeric_types]

    # Get categorical columns
    categorical_types = [T.StringType]
    categorical_columns = [c.name for c in snowpark_df.schema.fields if type(c.datatype) in categorical_types]

    col1, col2, = st.columns(2)

    with col1:
        st.write('Numeric columns:\t', numeric_columns)

    with col2:
        st.write('Categorical columns:\t', categorical_columns)
    

    # Calculte statistics for our dataset
    st.dataframe(snowpark_df.describe().sort('SUMMARY'), use_container_width=True)