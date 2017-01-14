# QuizBuzz

### Setup

Create a virtualenv and activate it

```sh
$ virtualenv quizbuzz-env --no-site-packages
$ cd quizbuzz-env
$ source bin/activate
```

Clone the repo and install requirements

```sh
$ git clone git@github.com:MBifolco/quizbuzz.git
$ cd quizbuzz
$ pip install -r requirements.txt
```

Create database

```sh
$ sqlite3 quizbuzz
$ ^C
$ python models.py
```
