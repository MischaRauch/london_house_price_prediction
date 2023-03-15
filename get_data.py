import pandas as pd

areas = ['City of London', 'Barking and Dagenham', 'Barnet', 'Bexley', 'Brent', 'Bromley', 'Camden', 'Croydon', 'Ealing',
         'Enfield', 'Greenwich', 'Hackney', 'Hammersmith and Fulham', 'Haringey', 'Harrow', 'Havering', 'Hillingdon',
         'Hounslow', 'Islington', 'Kensington and Chelsea', 'Kingston upon Thames', 'Lambeth', 'Lewisham', 'Merton',
         'Newham', 'Redbridge', 'Richmond upon Thames', 'Southwark', 'Sutton', 'Tower Hamlets', 'Waltham Forest',
         'Wandsworth','Westminster']

def get_housing_density():
    housing_density = pd.read_excel('data/housing density.xlsx', sheet_name= 'Number of dwellings')
    housing_density = housing_density.drop(index=0)
    for area_london in housing_density['Area name']:
        if area_london not in areas:
            housing_density = housing_density[housing_density['Area name'] != area_london]
    housing_density.rename(columns={'Area name', 'Area'}, inplace=True)
    housing_density.rename(columns={'ONS code', 'Code'}, inplace=True)
    return housing_density.dropna()

# NO CITY OF LONDON
def get_crime():
    crime = pd.read_csv('data/crime.csv')
    crime = crime.drop(crime.columns[[0,1]], axis=1)
    crime = crime.reset_index(drop=True)
    for col in crime.columns[1:]:
        if '04' in col:
            continue
        else:
            crime = crime.drop(col, axis=1)

    crime = crime.groupby('LookUp_BoroughName').agg('sum').reset_index()

    for area_london in crime['LookUp_BoroughName']:
        if area_london not in areas:
            crime = crime[crime['LookUp_BoroughName'] != area_london]

    new_name = {}
    for col in crime.columns[1:]:
        new_name[col] = col[:4]

    crime.rename(columns={'LookUp_BoroughName', 'Area'}, inplace=True)
    return crime.rename(columns=new_name).dropna()

def get_waste():
    waste = pd.read_excel('data/recycle.xlsx', sheet_name='Household Recycling Rates')
    waste = waste.drop(index=0)
    waste = waste.drop('Code', axis=1)
    for area_london in waste['Area']:
        if area_london not in areas:
            waste = waste[waste['Area'] != area_london]
    new_name = {}
    for col in waste.columns[2:]:
        new_name[col] = col[:4]

    waste.rename(columns={'New Code', 'Code'}, inplace=True)
    return waste.rename(columns=new_name).dropna()


