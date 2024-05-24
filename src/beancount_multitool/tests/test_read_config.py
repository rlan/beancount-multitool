from beancount_multitool.read_config import read_config

def test_read_config():
    try:
      config = read_config("no_file_error.toml")
    except Exception as e:
       print(e)
       assert True
    else:
       assert False
