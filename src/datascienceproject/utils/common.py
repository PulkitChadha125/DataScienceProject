import os,sys
import yaml
from src.datascienceproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

# ensure_annotations 


@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """
    read yaml file and returns
    Args:
        path_to_yaml(Path): path like input
    Raises:
        ValueError: if yaml file is not found
        e: any other error
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml,'r') as yaml_file:
            content=yaml.safe_load(yaml_file)
        logger.info(f"yaml file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """
    create list of directories
    Args:
        path_to_directories: list of path of directories
        verbose: if True print the message
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    """
    save json data
    Args:
        path: path to json file
        data: data to save
    """
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
    
    logger.info(f"json file: {path} saved successfully")

@ensure_annotations
def load_json(path:Path)->ConfigBox:
    """
    load json data
    Args:
        path: path to json file
    """
    with open(path) as f:
        content=json.load(f)
    logger.info(f"json file: {path} loaded successfully")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path:Path):
    """
    save binary data
    Args:
        data: data to save
        path: path to binary file
    """
    joblib.dump(data,path)
    logger.info(f"binary file: {path} saved successfully")

@ensure_annotations
def load_bin(path:Path)->Any:
    """
    load binary data
    Args:
        path: path to binary file
    """
    data=joblib.load(path)
    logger.info(f"binary file: {path} loaded successfully")
    return data
