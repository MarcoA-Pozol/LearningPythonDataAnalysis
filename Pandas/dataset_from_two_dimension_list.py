import pandas as pd

"""Define examples"""
def example_one():
    # Defining list of data
    two_dimensions_list = [
        [101, 'Electronics', 125950],
        [102, 'Bakery & Bread', 68469],
        [103, 'Veggetables & Fruits', 97207],
        [104, 'Pharmacy & Health', 116422],
        [105, 'Pets', 32945],
        [106, 'Clothing & Apparel', 116705]
    ] # List of lists with three items inside for each list
    # Using three columns for data
    columns = ['department_id', 'name', 'total_profits'] # Must match the number of items per list in two_dimensions_list

    def dataframe_from_two_dimension_list(two_dimensions_list:list[list[str|int|float]], columns:list[str]) -> pd.DataFrame:
        df = pd.DataFrame(data=two_dimensions_list, columns=columns)
        # Setting 'department_id' provided column to be the index of the dataframe
        df = df.set_index('department_id')
        return df

    df = dataframe_from_two_dimension_list(two_dimensions_list, columns)
    print(df)

def example_two():
    # Set data and columns
    customers_data = [
        [22026, 'John', 'Hudson', 43, 'Houston'],
        [33590, 'Linda', 'Campbell', 27, 'Florida'],
        [34971, 'Helen', 'Lewis', 36, 'New York'],
        [38162, 'Tony', 'Handman', 42, 'Detroit'],
        [41438, 'Carlos', 'Montana', 38, 'San Diego'],
    ]
    columns = ['id', 'firstname', 'lastname', 'age', 'city']

    # define dataframe
    df = pd.DataFrame(data=customers_data, columns=columns)
    df = df.set_index('id')
    print(df)

def example_three():
    flights = [
        [237, 'Florida', 'Los Angeles', 92, 180, 93*250],
        [328, 'New York', 'Chicago', 150, 120, 150*250],
        [415, 'Texas', 'Miami', 85, 160, 85*250],
        [522, 'California', 'Seattle', 200, 140, 200*250],
        [678, 'Nevada', 'Denver', 110, 130, 110*250],
        [789, 'Arizona', 'Houston', 95, 175, 95*250],
        [843, 'Boston', 'San Francisco', 134, 300, 134*250],
        [910, 'Atlanta', 'Orlando', 125, 95, 125*250],
        [112, 'Seattle', 'Dallas', 180, 210, 180*250],
        [265, 'Philadelphia', 'Phoenix', 143, 250, 143*250]
    ]
    columns = ['flight_id', 'origin', 'destination', 'passengers(Count)', 'time(Minutes)', 'revenue(USD)']
    print(flights)

    df = pd.DataFrame(data=flights, columns=columns)
    df = df.reset_index(drop=True)
    print(df.describe()) # count, mean, str, min, 25, 50, 75, max of numeric columns
    print(df)


"""Usage"""
example_one()
example_two()
example_three()