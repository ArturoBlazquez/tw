## Synopsis

Small script that saves all your twitter tl to an html file.
This file is located inside the html folder, has the date in the title, and sorts tweets from oldest at the top to newest at the bottom.

## Installation

You need to install tweepy, it should work with PyPI:
```
    pip install tweepy
```
if it doesn't work check their documentation:
    https://github.com/tweepy/tweepy

## Usage

```
python tw.py
```

To run the script on a server periodically you can run 
```
sudo crontab -e
```

and add:
```
00 2,8,14,20 * * * python <path_to_script>/tw.py
```

## Author

Arturo Blázquez
