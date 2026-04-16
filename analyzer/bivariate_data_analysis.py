from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


""" Abstract Base Class for Bivariate Analysis Strategy """
class BivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        Perform bivariate analysis on two features of the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature1 (str): The name of the first feature/column.
        feature2 (str): The name of the second feature/column.

        Returns:
        None: This method visualizes the relationship between the two features.
        """
        pass


"""
    Analyzes the relationship between two numerical features using a scatter plot.
"""
class NumericalVsNumericalAnalysis(BivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        Plots a scatter plot to visualize the relationship between two numerical features.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature1 (str): The name of the first numerical feature (x-axis).
        feature2 (str): The name of the second numerical feature (y-axis).

        Returns:
        None: Displays a scatter plot.
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=feature1, y=feature2, data=df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()


"""
    Analyzes the relationship between a categorical and a numerical feature using a box plot.
"""
class CategoricalVsNumericalAnalysis(BivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        Plots a box plot to visualize how a numerical feature varies across categories.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature1 (str): The name of the categorical feature (x-axis).
        feature2 (str): The name of the numerical feature (y-axis).

        Returns:
        None: Displays a box plot.
        """
        plt.figure(figsize=(12, 6))
        sns.boxplot(x=feature1, y=feature2, data=df, palette="muted")
        plt.title(f"{feature2} by {feature1}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.xticks(rotation=45)
        plt.show()


"""
    Analyzes the correlation between numerical features using a heatmap.
"""
class CorrelationHeatmapAnalysis(BivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature1: str = None, feature2: str = None):
        """
        Plots a correlation heatmap for all numerical features in the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature1 (str): Not used. Kept for interface consistency.
        feature2 (str): Not used. Kept for interface consistency.

        Returns:
        None: Displays a correlation heatmap.
        """
        plt.figure(figsize=(14, 10))
        numerical_df = df.select_dtypes(include=["number"])
        correlation_matrix = numerical_df.corr()
        sns.heatmap(correlation_matrix, annot=False, fmt=".2f", cmap="coolwarm", linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.show()


"""
Context Class that uses a BivariateAnalysisStrategy
"""
class BivariateAnalyzer:
    def __init__(self, strategy: BivariateAnalysisStrategy):
        """
        Initializes the BivariateAnalyzer with a specific analysis strategy.

        Parameters:
        strategy (BivariateAnalysisStrategy): The strategy to be used for bivariate analysis.

        Returns:
        None
        """
        self._strategy = strategy

    def set_strategy(self, strategy: BivariateAnalysisStrategy):
        """
        Sets a new strategy for the BivariateAnalyzer.

        Parameters:
        strategy (BivariateAnalysisStrategy): The new strategy to be used for bivariate analysis.

        Returns:
        None
        """
        self._strategy = strategy

    def execute_analysis(self, df: pd.DataFrame, feature1: str = None, feature2: str = None):
        """
        Executes the bivariate analysis using the current strategy.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature1 (str): The name of the first feature/column.
        feature2 (str): The name of the second feature/column.

        Returns:
        None: Executes the strategy's analysis method and visualizes the results.
        """
        self._strategy.analyze(df, feature1, feature2)
