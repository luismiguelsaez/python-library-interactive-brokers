## Description

Python library for Interactive Brokers flex query data import

## Testing

### Create python virtualenv

```
$ virtualenv -p $(which python) .venv
$ . .venv/bin/activate
$ pip install -r requirements.txt
```
### Test library

```
$ python test.py <ib_token> <flex_query_id>
```
