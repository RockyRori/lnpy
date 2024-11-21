# Student Name: LUO Suhai
# Student ID: 3160708

# Assignment 4, Case Study
"""
Automatically fetch data from the Hong Kong government’s data portal and visualize the data into charts.
"""
import json
from io import StringIO
from typing import Literal
from urllib.parse import quote

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from pandas import DataFrame


def section_code(year: str) -> int:
    """
    transfer user input year into target year
    :param year: atmosphere data target year
    :return: section code
    """
    try:
        year = int(year)
        if 2 <= (section := year - 2012) <= 6:
            return section
        else:
            raise Exception("Please input a year between 2014-2018")
    except ValueError:
        raise Exception("Please input a number of year")


def fetch_website_data(data_section: int, data_format: Literal["csv", "json", "xml"]) -> str:
    """
    fetch data through official api

    Example:
        url = "https://api.data.gov.hk/v2/aggregate/hk-epd-past-record-of-aqhi-en?q=%7B%22section%22%3A2%2C%22format%22%3A%22json%22%2C%22filters%22%3A%5B%5B1%2C%22eq%22%2C%5B%222014-01-04%22%5D%5D%2C%5B2%2C%22bw%22%2C%5B%222%22%5D%5D%5D%7D"

    :param data_section: sharding storage number
    :param data_format: data restore format
    :return: binary data
    """
    website = "https://api.data.gov.hk/v2/aggregate/hk-epd-past-record-of-aqhi-en?q="
    query = f"{{\"section\":{data_section},\"format\":\"{data_format}\"}}"
    query = quote(query)
    url = website + query

    try:
        response = requests.get(url)
        response.raise_for_status()
        with open("original.json", 'w', encoding='utf-8') as file:
            file.write(response.text)
        return response.text
    except requests.RequestException as e:
        print(f"Error downloading webpage: {e}")
        return ""


def data_storage(data: str) -> str:
    """
    :param data: cleaned data need to be restored
    :return: data
    """
    with open("cleaning.json", 'w', encoding='utf-8') as file:
        file.write(data)
    return data


def data_cleaning(data: object) -> object:
    """
    emove *+ in the data and fill in blank space with default 0
    :param data: data
    :return: cleaned analysable data
    """
    if isinstance(data, (dict, list)):
        json_str = json.dumps(data)
        replaced_str = json_str.translate(str.maketrans('', '', '+*')).replace('""', '"0"')
        return json.loads(replaced_str)
    elif isinstance(data, str):
        return data.translate(str.maketrans('', '', '+*')).replace('""', '"0"')
    else:
        return data


def bar_chart(data: DataFrame):
    """
    draw a bar chart depicting average score of all districts separately by month
    :param data: pandas dataframe
    :return: a plot
    """
    data['Date'] = pd.to_datetime(data['Date'])
    data['Month'] = data['Date'].dt.to_period('M')

    long_data = data.melt(id_vars=['Date', 'Hour', 'Month'], var_name='District', value_name='Score')
    monthly_avg = long_data.groupby(['Month', 'District'])['Score'].mean().reset_index()
    months = monthly_avg['Month'].unique()

    fig, axes = plt.subplots(4, 3, figsize=(16, 12))
    axes = axes.flatten()  # 将子图矩阵展平成一维数组

    for i, month in enumerate(months):
        month_data = monthly_avg[monthly_avg['Month'] == month]
        ax = axes[i]
        ax.bar(month_data['District'], month_data['Score'])
        ax.set_title(f"{month}")
        ax.set_ylabel("Avg Score")
        ax.tick_params(axis='x', rotation=80)

    for j in range(len(months), len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.savefig("yearly_average.png")
    plt.show()


def line_chart(data: DataFrame):
    """
    draw a line chart depicting trend score of all districts separately by month
    :param data: pandas dataframe
    :return: a plot
    """
    data['Date'] = pd.to_datetime(data['Date'])
    data['Month'] = data['Date'].dt.to_period('M')
    data['Day'] = data['Date'].dt.day

    long_data = data.melt(id_vars=['Date', 'Hour', 'Month', 'Day'], var_name='District', value_name='Score')
    daily_avg = long_data.groupby(['Month', 'Day'])['Score'].mean().reset_index()
    months = daily_avg['Month'].unique()

    fig, axes = plt.subplots(4, 3, figsize=(16, 12))
    axes = axes.flatten()

    for i, month in enumerate(months):
        month_data = daily_avg[daily_avg['Month'] == month]
        ax = axes[i]
        ax.plot(month_data['Day'], month_data['Score'], marker='*')
        ax.set_title(f"{month}")
        ax.set_ylabel("Avg Score")
        ax.set_xticks(np.arange(0, 31, 5))

    for j in range(len(months), len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.savefig("monthly_trend.png")
    plt.show()


if __name__ == '__main__':
    target_year = input("Please input the target year: ")
    fetched_data = fetch_website_data(section_code(target_year), "json")
    cleaned_data = data_cleaning(fetched_data)
    stored_data = data_storage(str(cleaned_data))
    framed_data = pd.read_json(StringIO(stored_data))
    bar_chart(framed_data)
    line_chart(framed_data)
