import random
from functools import wraps
import time

from undetected_chromedriver import Chrome, ChromeOptions


def randomize(
                _option_,
                _length_
            ):

    if _length_ > 0 :

        # Options:
        #       -p      for letters, numbers and symbols
        #       -s      for letters and numbers
        #       -l      for letters only
        #       -n      for numbers only
        #       -m      for month selection
        #       -d      for day selection
        #       -y      for year selection

        if _option_ == '-p':
            chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
        elif _option_ == '-s':
            chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        elif _option_ == '-l':
            chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif _option_ == '-n':
            chars='1234567890'
        elif _option_ == '-m':
            chars='JFMASOND'

        if _option_ == '-d':
            _generated_info_=random.randint(1,28)
        elif _option_ == '-y':
            _generated_info_=random.randint(1950,2000)
        else:
            _generated_info_=''
            for _ in range(0,_length_) :
                _generated_info_= _generated_info_ + random.choice([*chars])

        return _generated_info_

    else:
        return 'error'

def max_tries(max_tries: int = 3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_tries):
                try:
                    time.sleep(i*8)
                    return func(*args, **kwargs)
                except Exception:
                    pass
        return wrapper
    return decorator

def get_driver(log_performance=False, headless = False) -> Chrome:
    TIMEOUT = 15
    options = ChromeOptions()
    options.page_load_strategy = "eager"
    options.add_argument("--start-maximized")
    # options.add_argument("--disable-gpu")

    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    capabilities = options.capabilities
    if log_performance:
        capabilities["goog:loggingPrefs"] = {"performance": "ALL"}  # type: ignore

    driver = Chrome(
        headless=headless,
        options=options,
        desired_capabilities=capabilities,
    )
    driver.implicitly_wait(TIMEOUT)
    return driver
