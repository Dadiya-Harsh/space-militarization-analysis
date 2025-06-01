# src/data_loader/fetch_tle.py

import requests
from pathlib import Path
from typing import Dict, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define TLE data sources
TLE_SOURCES = {
    'military': {
        'url': "https://celestrak.org/NORAD/elements/gp.php?GROUP=military&FORMAT=tle",
        'description': "Military satellites"
    },
    'starlink': {
        'url': "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle",
        'description': "Starlink satellites"
    },
    'oneweb': {
        'url': "https://celestrak.org/NORAD/elements/gp.php?GROUP=oneweb&FORMAT=tle",
        'description': "OneWeb satellites"
    },
    'geo': {
        'url': "https://celestrak.org/NORAD/elements/gp.php?GROUP=geo&FORMAT=tle",
        'description': "Geosynchronous satellites"
    },
    'intelligence': {
        'url': "https://celestrak.org/NORAD/elements/gp.php?GROUP=intelsat&FORMAT=tle",
        'description': "Intelligence satellites"
    }
}

def download_tle_data(url: str, save_path: str) -> bool:
    """
    Download TLE data from a given URL and save it to the specified path.
    
    Args:
        url (str): URL to fetch TLE data from
        save_path (str): Path where the TLE data should be saved
        
    Returns:
        bool: True if download was successful, False otherwise
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Create directory if it doesn't exist
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Save the data
        with open(save_path, 'w') as f:
            f.write(response.text)
            
        logger.info(f"Successfully downloaded TLE data to: {save_path}")
        return True
        
    except requests.RequestException as e:
        logger.error(f"Failed to fetch TLE data from {url}: {str(e)}")
        return False
    except IOError as e:
        logger.error(f"Failed to save TLE data to {save_path}: {str(e)}")
        return False

def download_all_tle_data(base_path: str = "data/raw") -> Dict[str, bool]:
    """
    Download TLE data from all configured sources.
    
    Args:
        base_path (str): Base directory to save TLE files
        
    Returns:
        Dict[str, bool]: Dictionary mapping source names to download success status
    """
    results = {}
    
    for source_name, source_info in TLE_SOURCES.items():
        save_path = f"{base_path}/{source_name}.tle"
        success = download_tle_data(source_info['url'], save_path)
        results[source_name] = success
        
    return results

if __name__ == "__main__":
    # Download all TLE data
    results = download_all_tle_data()
    
    # Print summary
    print("\nDownload Summary:")
    print("-" * 50)
    for source_name, success in results.items():
        status = "✓ Success" if success else "✗ Failed"
        print(f"{source_name}: {status}")
