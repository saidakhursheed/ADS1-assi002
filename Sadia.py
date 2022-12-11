import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:\\Users\\RajaI\\Desktop\\climate change\\GDP.csv')


def file(df):
    """
    Function to read data and return data (countries as columns and years as
    columns)
    """
    MyYearsData = df
    MyCountriesData = MyYearsData.set_index('Country Name').T

    return MyYearsData, MyCountriesData


print(file(df))


def pieplot(data, labels, title=""):
    """
    Produces a piechart of data.
    data: list of data values
    labels: list of labels of same length
    title: string for the title, defaulted to ""
    No plt.show() is given at the end to allow plotting to continue

    You were not required to make your functions flexible, but it is a
    good attitude and allows to recycle function for other data. Scoping
    (drawing the data from the calling unit) is the least flexible way.
    The variable name must be an exact match. A new function is required
    for a variable with a different name.
    """

    plt.pie(data, labels=labels)
    plt.title(title)

    return


def lineplot(df, x, columns, xlabel, ylabel, file):
    """
    Produces a line plot from a dataframe. x-limits are adjusted to remove
    empty spaces at the edges.
    df: name of the dataframe
    x: 1D array or dataseries with the x-values
    columns: names of the columns in df to be plotted. Also used for the
            legend.
    xlabel, ylabels: labels for x and y axis.
    file: file name to store the plot as png file
    """

    plt.figure()

    # loop over the columns
    for c in columns:
        plt.plot(x, df[c], label=c)

    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # set x-limits
    plt.xlim(min(x), max(x))

    plt.savefig(file)
    plt.show()


def GDPPlot1(df):
    '''
    Function to comapre different countries on the basis of GDP
    '''
    # extract 1990 column, more than one column can be extracted by using a
# list containing column names
    df_1990 = df[["Country Name", "1990"]]
# extract countries of interest
    df_1990 = df_1990[(df_1990["Country Name"] == "United States")
                      | (df_1990["Country Name"] == "Brazil")
                      | (df_1990["Country Name"] == "Russian Federation")
                      | (df_1990["Country Name"] == "India")
                      | (df_1990["Country Name"] == "China")
                      | (df_1990["Country Name"] == "South Africa")]
# convert GDP column to numeric (non-numeric type before because NaN)
# not that the column name is still a string
    df_1990["1990"] = pd.to_numeric(df_1990["1990"])
# print(df_1990)

    pieplot(df_1990["1990"], labels=df_1990["Country Name"], title="GDP 1990")
    plt.savefig("GDP_pie.png")
    plt.show()


df = pd.read_csv('C:\\Users\\RajaI\\Desktop\\climate change\\GDP.csv')
GDPPlot1(df)


def PopPlot1(df):
    '''
    Function to comapre different countries on the basis of Population
    '''
    # extract 2015 column, more than one column can be extracted by using a
# list containing column names
    df_2015 = df[["Country Name", "2015"]]
# extract countries of interest
    df_2015 = df_2015[(df_2015["Country Name"] == "United States")
                      | (df_2015["Country Name"] == "Brazil")
                      | (df_2015["Country Name"] == "Russian Federation")
                      | (df_2015["Country Name"] == "India")
                      | (df_2015["Country Name"] == "China")
                      | (df_2015["Country Name"] == "South Africa")]
# convert GDP column to numeric (non-numeric type before because NaN)
# not that the column name is still a string
    df_2015["2015"] = pd.to_numeric(df_2015["2015"])
# print(df_1990)
    labels = ["United States", "Brazil", "Russia", "India", "China",
              "South Africa"]
    pieplot(df_2015["2015"], labels=labels, title="Population"
            "2015")
    plt.savefig("Pop.png")
    plt.show()


df = pd.read_csv('C:\\Users\\RajaI\\Desktop\\climate change\\Population.csv')
PopPlot1(df)


def Heatmap(df):
    '''
    Function to comapre different countries on the basis of C02 emission
    '''
    # extract 2015 column, more than one column can be extracted by using a
# list containing column names
    df = df[["Country Name", "Indicator Code", "2015", "2016", "2017"]]
# extract countries of interest
    df = df[((df['Indicator Code'] == "SP.URB.TOTL")) &
            ((df["Country Name"] == "United States")
            | (df["Country Name"] == "Brazil")
            | (df["Country Name"] == "Russian Federation")
            | (df["Country Name"] == "India")
            | (df["Country Name"] == "China")
            | (df["Country Name"] == "South Africa"))]

    x = df.pivot("Country Name", "Indicator Code", ["2015", "2016", "2017"])

    ax = plt.axes()
    sns.heatmap(x.corr(), annot=True, cmap="crest", ax=ax)
    ax.set_title('Heatmap of Urban Population of Countries')
    plt.show()


df = pd.read_csv('C:\\Users\\RajaI\\Desktop\\climate change\\data.csv')
Heatmap(df)


def COSPlot2(df):
    '''
    Function to comapre different countries on the basis of C02 Emission
    '''
    df = df.transpose()
    # clean up to be done: make the first row of the table the column headers
    df.columns = df.iloc[0]

# print(df_cap)

# clean up to be done: make the first row of the table the column headers
    df.columns = df.iloc[0]
# print(df_cap)
# Now remove the first 4 lines not containing data. I simple way is to
# extract all lines staarting with 4 (python count)
    df = df.iloc[4:]
# print(df_cap)
# The Russian column will contain NaNs before 1990
# drop rows with NaNs in this column
    df = df[df["Russian Federation"].notna()]
# print(df_cap)
# NaNs caused index and columns to be non-numeric types. Conversion for the
# index and the columns of interest
    df.index = pd.to_numeric(df.index)

# index and the columns of interest
    df.index = pd.to_numeric(df.index)
    df["China"] = pd.to_numeric(df["China"])
    df["India"] = pd.to_numeric(df["India"])
    df["Brazil"] = pd.to_numeric(df["Brazil"])
    df["Russian Federation"] = pd.to_numeric(df["Russian Federation"])
    df["South Africa"] = pd.to_numeric(df["South Africa"])


# call the line plot function
    lineplot(df, df.index, ["Brazil", "China", "India", "South Africa",
                            "United States"], "year", "C02 Emission",
             'C02 Emission.png')


df = pd.read_csv('C:\\Users\\RajaI\\Desktop\\climate change\\C02emission.csv')
COSPlot2(df)


def ExpensesPlot2(df):
    '''
    Function to comapre different countries on the basis of Expenses
    of countries
    '''
    df = df.transpose()
    # clean up to be done: make the first row of the table the column headers
    df.columns = df.iloc[0]

# print(df_cap)

# clean up to be done: make the first row of the table the column headers
    df.columns = df.iloc[0]
# print(df_cap)
# Now remove the first 4 lines not containing data. I simple way is to
# extract all lines staarting with 4 (python count)
    df = df.iloc[4:]
# print(df_cap)
# The Russian column will contain NaNs before 1990
# drop rows with NaNs in this column
    df = df[df["Russian Federation"].notna()]
# print(df_cap)
# NaNs caused index and columns to be non-numeric types. Conversion for the
# index and the columns of interest
    df.index = pd.to_numeric(df.index)

# index and the columns of interest
    df.index = pd.to_numeric(df.index)
    df["China"] = pd.to_numeric(df["China"])
    df["India"] = pd.to_numeric(df["India"])
    df["Brazil"] = pd.to_numeric(df["Brazil"])
    df["Russian Federation"] = pd.to_numeric(df["Russian Federation"])
    df["South Africa"] = pd.to_numeric(df["South Africa"])


# call the line plot function
    lineplot(df, df.index, ["Brazil", "China", "India", "South Africa",
                            "United States"], "year", "Labour Force of "
             "Countries", "Labour Force.png")


df = pd.read_csv('C:\\Users\\RajaI\\Desktop\\climate change\\GDP.csv')
ExpensesPlot2(df)
