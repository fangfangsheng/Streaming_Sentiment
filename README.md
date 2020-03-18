# Case Study of Analysis of Emoji Usage in Tweets at network level

This repository contains the scripts can collect tweets from the Twitter Streaming API using Python, save data in the local MongoDB
 database and data pre-processing for building a Co-mention Emoji Network.  

## Introduction
Twitter Emoji Co-mention Network.

This project begins to explore how the emoji network structure may compare to that of the accompanying text language network.


Process: 
- Streamline Twitter API calls for tweets containing keyword “art” 
- Save to MongoDB
- Extract and preprocess the data


## Setup instructions

1. Open terminal/command prompt.
2. Clone the repository to your local system in a dedicated folder.
3. CD to the repo directory.
4. Create and activate a virtual environment for this project.
    * On macOS or Linux:
       ```
       python3 -m venv env
       source env/bin/activate
       which python
       ```
      * On Windows:
       ```
       py -m venv env
       .\env\Scripts\activate
       where python
       ```
5. Install necessary packages
   ```
   pip install -r requirements.txt
   ```

## Run instructions
1. Set up your local database, run `python mongodb_setup.py`

2. Remeber to modify your own configure information at `config.py`.

3. Run `python stream_twitter.py` to collect tweets from the Twitter Streaming API

4. Run


## Quit instructions


## Usage


## Authors
   Fangfang Sheng