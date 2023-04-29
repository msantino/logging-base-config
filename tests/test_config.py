import os
import logging
from importlib import reload
import logging_basic_config

def test_logging_level():
    logger = logging_basic_config.config(logging_level="DEBUG")
    assert logger.level == logging.DEBUG

def test_libs_to_silence():
    libs_to_silence = ['botocore', 'boto3']
    logger = logging_basic_config.config(libs_to_silence=libs_to_silence)
    for lib in libs_to_silence:
        assert logging.getLogger(lib).getEffectiveLevel() == logging.ERROR

def test_env_var_hide_timestamp():
    env_var_hide_timestamp = 'HIDE_TIMESTAMP'
    os.environ[env_var_hide_timestamp] = "somevalue"
    reload(logging)
    reload(logging_basic_config)
    logger = logging_basic_config.config(env_var_hide_timestamp=env_var_hide_timestamp)
    log_format = logger.handlers[0].formatter._fmt
    assert '%(asctime)s' not in log_format

def test_logging_output(capsys):
    logger = logging_basic_config.config(logging_level="INFO")
    logger.warning("Test warning")
    captured = capsys.readouterr()
    assert "Test warning" in captured.out