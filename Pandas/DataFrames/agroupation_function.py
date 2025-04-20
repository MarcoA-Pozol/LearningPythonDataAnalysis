def group_data_by(dataset_path:str, index:str, values:str, ag_funct:str, title:str, ascending_order:bool=True):
    """ 
        Custom function to group by the provided columns and values.
        Easy to execute and build with only passing parameters up direct to the function.
        Add aggregation functions like mean, count, max, less, etc.
    """
    import pandas as pd
    import os # Dataset path extension checking and validation

    # Load dataset validating its extension
    # Extract file extension
    file_extension = os.path.splitext(dataset_path)[1].lower()

    # Load CSV or Excel accordingly
    if file_extension == '.csv':
        df = pd.read_csv(dataset_path)
    elif file_extension in {'.xls', '.xlsx'}:
        df = pd.read_excel(dataset_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}. Supported formats: CSV, XLS, XLSX")
    

    # Clean non numeric values in column
    df[values] = df[values].replace('-', pd.NA).apply(pd.to_numeric, errors='coerce')
    
    # Define aggregation function dynamically
    aggregation_functions = {
        'mean': 'mean',
        'count': 'count',
        'max': 'max',
        'min': 'min'
    }

    if ag_funct not in aggregation_functions:
        raise ValueError("Invalid aggregation function. Use 'mean', 'count', 'max', or 'min'.")


    # Grouping
    df = df.groupby(index)[values].agg(aggregation_functions[ag_funct])

    # Convert Series to DataFrame and rename columns
    df = df.reset_index()
    df.columns = [index, values]

    # Sort by desc order
    df = df.sort_values(by=values, ascending=ascending_order)

    
    # Set title
    title = f'#### {title} ####'.upper()
    title_separator_line = '-' * len(title)

    # Print dataframe
    print(f'\n{title}\n{title_separator_line}\n{df}')

    # Result
    return df

""" Function usage """
group_data_by('./DataSets/flights_details.xls', index='Airline', values='Passengers', ag_funct='count', ascending_order=False, title='Passengers count by airline')