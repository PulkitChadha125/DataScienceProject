from dataclasses import dataclass
from pathlib import Path

# only difference in data class and normal class is in normal class we need self keyword to 
# assign value here we dont need it 

@dataclass()
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    

@dataclass()
class DataValidataionConfig:
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: str
    all_schema: dict