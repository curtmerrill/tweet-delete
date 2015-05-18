Delete your tweets
------------------

This python script cleans up after you.

Why? I'll let [others explain it better](http://fusion.net/story/50322/meet-the-tweet-deleters-people-who-are-making-their-twitter-histories-self-destruct/) than I can.

**Note: This is not about security.** Deleting a Tweet doesn't not erase
it from everywhere for all time. Tweets are being archived by the Library
of Congress, for example.

Requrements
===========

In order to use this script, you need:

 *  Python3
 *  requests and requests-oathlib
 *  Twitter credentials
 *  A way to schedule the script (eg. cron)

Step-by-step
============

Clone repo:

    $ git clone ...
    $ cd ...

Install Python3:

    # MacOS X (with Homebrew)
    $ brew install python3

    # Ubuntu (you may need sudo)
    $ apt-get install python3 python3-setuptools

Optional, but recommended, use [virtualenv](https://virtualenv.pypa.io/en/latest/#)

    $ virtualenv --python=python3 env
    $ source env/bin/activate

Install Python libs:

    (env)$ pip install -r requirements.txt

Copy the `auth-template.py` file to `auth.py`:
    
    (env)$ cp auth-template.py auth.py

**DO NOT PUT AUTH.PY UNDER SOURCE CONTROL.** It's already in the
.gitignore file, so you shouldn't have to worry about it, but be
careful.

Get Twitter credentials:

  * Login to Twitter.
  * Visit [http://apps.twitter.com](https://apps.twitter.com).
  * Click "Create New App".
  * Give it a name, like "Delete my tweets," a description and URL.
    Then agree to the terms and conditions.
  * Click on the "Keys and Access Tokens" tab.
  * Copy the `Consumer Key` and `Consumer Secret` strings into the
    `auth.py` file.
  * Click on the "Create my access token" button.
  * Copy the `Access Token` and `Access Token Secret` strings into
    the `auth.py` file.

Edit the variables near the top of `delete-tweets.py`

    ### SETTINGS ###

    screen_name = 'cmerrill'

    # Time between delete requests, in seconds
    # Minimum value is 5 in order to keep within Twitter API rate limits
    rate_delay = 6

    # Maximum age, in days, of tweets to keep
    max_age_in_days = 30

    # Minimum number of tweets to keep, regardless of age
    min_tweets_to_keep = 10

    # IDs of specific Tweets to keep
    protected_tweets = [600437773242359808, ] 

Run the script:
    
    # From within the virtualenv
    (env)$ python delete_tweets.py

    # Without the virtualenv (in cron, for example)
    # Assumes your virtualenv binaries are in the repository directory
    $ /path/to/repo/env/bin/python /path/to/repo/delete_tweets.py

License
=======

The MIT License (MIT)

Copyright (c) 2015 Curt Merrill

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

