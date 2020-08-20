README.md# Streaming Twitter Filter in Python
This is a streaming pipeline that downloads tweets, filters based on certain keywords and calculates 
sentiment scores. 

I use `tweepy` to get streaming data. To storage the data, I use Redis. One dashboard was created to present the results in real time.

## Usage

```python

redis-server

python stream_twitter.py

python twatcher.py

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)