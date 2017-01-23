# rss_reader

In a Python virtualenv run

```
pip install -r requirements.txt
```

Normally you'd have [Dart](https://www.dartlang.org/) installed.  You would build the dart to js with the following

```
pub build
```

This will output the files to build, with the entry point being build/web/index.html.


Then from base project directory run

```
python bin/server.py
```

This should run a cherrpy web app, which serves the static files found in build, and also doubles as an API for the Angular2 web app developed in Dart, compiled to JS.