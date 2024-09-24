import pandas as pd

worldPopulationDF = pd.read_csv('C:/PS1_A/Python/world_population.csv')

def mostPopulated2022(df):
    df_2022 = df[['Country', '2022 Population']].sort_values(by='2022 Population', ascending=False)
    return df_2022.head(3)

def leastPopulated2022(df):
    df_2022 = df[['Country', '2022 Population']].sort_values(by='2022 Population', ascending=True)
    return df_2022.head(3)

def growthRate(df):
    df['New_Growth_Rate'] = (df['2022 Population'] - df['2000 Population']) / df['2000 Population']
    return df

def ContinentPopulation(df):
    ContinentDF = df.groupby('Continent')['2022 Population'].sum().reset_index()
    return ContinentDF.sort_values(by='2022 Population')

print(mostPopulated2022(worldPopulationDF))
print()
print(leastPopulated2022(worldPopulationDF))
print()
population_df = growthRate(worldPopulationDF)
print(population_df[['Country', 'New_Growth_Rate']].head())
print()
print(ContinentPopulation(population_df))
