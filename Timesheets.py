import pandas as pd

def adjust_quantity(dataframe, max_quantity):
    """
    Remove rows where 'Quantity Reg' is greater than the specified max_quantity.
    """
    return dataframe[dataframe['Quantity Reg'] <= max_quantity]

def select_and_rename_columns(dataframe, columns_to_keep, new_column_names):
    """
    Select specific columns, reorder them, and rename them as specified.
    
    :param dataframe: The original DataFrame.
    :param columns_to_keep: List of columns to keep in the desired order.
    :param new_column_names: Dictionary mapping old column names to new column names.
    :return: A new DataFrame with selected and renamed columns.
    """
    # Select the desired columns
    dataframe = dataframe[columns_to_keep]
    
    # Rename the columns
    dataframe = dataframe.rename(columns=new_column_names)
    
    return dataframe

# Load the CSV file
df = pd.read_csv('./data/MOCK_TIMESHEET_DATA.csv')

# Filter rows where 'Quantity Reg' is greater than 8
df_filtered = adjust_quantity(df, 8)

# Define the columns to keep and their new names
columns_to_keep = ['Original Entry Date', 'Task', 'Description', 'Employee Number', 'Employee Name', 'Quantity Reg']
new_column_names = {
    'Original Entry Date': 'Entry Date',
    'Task': 'Task',
    'Description': 'Description',
    'Employee Number': 'Emp Number',
    'Employee Name': 'Emp Name',
    'Quantity Reg': 'Qty Reg'
}

# Select and rename columns
df_final = select_and_rename_columns(df_filtered, columns_to_keep, new_column_names)

# Save the final DataFrame to a new CSV file
df_final.to_csv('./data/filtered_and_renamed.csv', index=False)
