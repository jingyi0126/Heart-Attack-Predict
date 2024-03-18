#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023-08-20
# @Author  : JIngyi Zhang
# @Site    : https://github.com/Wangzhaoze/BNFPL
# @File    : base_model.py
# @IDE     : vscode


import pandas as pd
import numpy as np
import copy
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

class CSVDataPreProcessor:
    '''
        Attributes:
        raw_data (pd.DataFrame): The raw dataset.
        processed_data (pd.DataFrame): The processed dataset.
    '''

    def __init__(self, file_path: str) -> None:
        '''
        Initializes the CSVDataPreProcessor class.

        Args:
            file_path (str): The file path to the CSV file.

        Raises:
            ValueError: If file path is not a string or if path does not exist.
        '''
        if not isinstance(file_path, str):
            raise ValueError('Input file_path should be string.')

        if not os.path.exists(file_path):
            raise ValueError('Input path not exists')
        
        self.raw_data: pd.DataFrame = pd.read_csv(file_path)
        self.processed_data: pd.DataFrame = copy.deepcopy(self.raw_data)

        

    def drop(self, col_name: str):
        '''
        Drops the specified column from the dataset.

        Args:
            col_name (str): The name of the column to drop.
        '''
        self.processed_data = self.processed_data.drop(columns=col_name)

    def fill_na(self):
        '''
        Fills missing values.

        Uses different filling strategies based on column data types:
        - For object and boolean types, fills with mode.
        - For numeric types, fills with mean.
        - For other types, replaces with NaN.
        '''
        if self.processed_data.isnull().any().any():
            columns_with_na = self.processed_data[self.processed_data.isnull().any()].tolist()

            for column in columns_with_na:
                dtype = self.processed_data[column].dtype
                if dtype in ['object', 'bool']:
                    mode_value = self.processed_data[column].mode()[0]
                    self.processed_data[column].fillna(mode_value, inplace=True)

                elif dtype in ['int64', 'float64']:
                    mean_value = self.processed_data[column].mean()
                    self.processed_data[column].fillna(mean_value, inplace=True)
                else:
                    self.processed_data[column].fillna(np.na, inplace=True)



    def one_hot(self, col_name: str):
        '''
        Performs one-hot encoding on the specified column and concatenates the result with the original dataset.

        Args:
            col_name (str): The name of the column to one-hot encode.
        '''
        one_hot_code_df = pd.get_dummies(self.processed_data[col_name], prefix= col_name)
        self.processed_data = pd.concat(self.processed_data, one_hot_code_df)
        self.drop(col_name)
        
        
    def scale(self):
        '''
        Scales the dataset using standardization.
        '''
        scale = StandardScaler()
        self.processed_data = scale.fit_transform(self.processed_data)

    def Datasplit(feature: pd.DataFrame, target: pd.DataFrame, test_size: float):
        '''
        Splits the dataset into training and testing sets.

        Args:
            feature (pd.DataFrame): The feature dataset.
            target (pd.DataFrame): The target dataset.
            test_size (float): The proportion of the dataset to include in the test split.

        Returns:
            tuple: A tuple containing the training feature, testing feature, training target, and testing target datasets.
        '''
        X_train, X_test, y_train, y_test = train_test_split(feature, target, test_size=test_size)





