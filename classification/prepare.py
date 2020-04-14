import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler


def prep_iris(iris):
    iris = iris.drop(columns = ['species_id', 'measurement_id'])
    iris = iris.rename(columns = {'species_name': 'species'})
    encoder = LabelEncoder()
    encoder.fit(iris.species)
    iris["species_encoded"]= encoder.transform(iris.species)
    train, test = train_test_split(iris, train_size = .8, random_state = 123)
    return train, test

def prep_titanic(titanic):
    #Handle the missing values in the embark_town and embarked columns.
    titanic.embark_town = titanic.embark_town.fillna('Southampton')
    titanic.embarked = titanic.embarked.fillna('S')
    
    #Remove the deck column.
    titanic = titanic.drop(columns = 'deck')
    
    #Use a label encoder to transform the embarked column.
    encoder = LabelEncoder()
    encoder.fit(titanic.embarked)
    titanic['embarked_encoded'] = encoder.transform(titanic.embarked)
    
    # split dataset
    train, test = train_test_split(titanic, train_size = .8, random_state = 123)
   
    #scale the age and fare columns using a min_max_scaler
    scaler = MinMaxScaler()
    train_scaled = pd.DataFrame(scaler.fit_transform(train[['age', 'fare']]), 
                                    columns = ['age_scaled', 'fare_scaled'],
                                    index = train.index)
    test_scaled = pd.DataFrame(scaler.transform(test[['age', 'fare']]), 
                                    columns = ['age_scaled', 'fare_scaled'],
                                    index = test.index)
    train = pd.concat([train, train_scaled], axis = 1)
    test = pd.concat([test, test_scaled], axis = 1)
    
    #Fill the missing values in age.
    imputer = SimpleImputer(strategy = 'mean')
    train.age = imputer.fit_transform(train[['age']])
    test.age = imputer.transform(test[['age']])
    return train, test