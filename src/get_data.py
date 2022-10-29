# read the params.yaml file
# process it
# copy the data to raw directory
import os
import yaml
import pandas as pd
import argparse

def read_params(config_path):
    with open(config_path) as yaml_file:
        config  = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    print(config)
    data_path = config["data_source"]["s3_source"]
    # print(data_path)# data_given/Advertising.csv
    df = pd.read_csv(data_path,sep=",")
    # print(df.head(5))
    return df



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    print(parsed_args)
    print(parsed_args.config)
    get_data(config_path=parsed_args.config)#passing params.yaml
    

