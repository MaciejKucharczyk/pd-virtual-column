import pandas as pd 

def add_virtual_column(df: pd.DataFrame, rule: str, new_column: str) -> pd.DataFrame:
    # Check if new_column is a valid column name (alphanumeric and underscores only)
    name = new_column.replace('_', 'C')
    if not name.isalpha() or new_column in df.columns:
        print("Invalid new column name")
        return pd.DataFrame()  # Return empty DataFrame for invalid new_column

    # Remove extra spaces from the rule
    rule = rule.strip()

    # Allowed operators
    allowed_operators = {'+', '-', '*'}

    components = rule.split()
    
    if len(components) != 3:
        print("Invalid rule format")
        return pd.DataFrame()  # Invalid rule format

    col1, operator, col2 = components

    # Check if the operator is valid
    if operator not in allowed_operators:
        print("Invalid operator")
        return pd.DataFrame()  # Invalid operator

    # Check if both columns exist in the df
    if col1 not in df.columns or col2 not in df.columns:
        print("One of the columns does not exist")
        return pd.DataFrame()  # One of the columns does not exist

    # Perform the operation and create the new column
    try:
        if operator == '+':
            df[new_column] = df[col1] + df[col2]
        elif operator == '-':
            df[new_column] = df[col1] - df[col2]
        elif operator == '*':
            df[new_column] = df[col1] * df[col2]
    except Exception as e:
        return pd.DataFrame()  # Return empty df on any error during operation

    return df

if __name__ == "__main__":
    # Example usage
    df = pd.DataFrame([[1, 2], [3, 4]], columns=["A", "B"])
    print(add_virtual_column(df, "A * B", "AB")) 