env = "prd"

"""
1. prd production  environment
2. dev development environment
3. test  test environment
"""


class TestConfig:
    DBNAME = "xxx"


class PrdConfig:
    DBNAME = "xxx"


class DevConfig:
    DBNAME = "xxx"


class Config:
    myclass = {
        "test": TestConfig,
        "prd": PrdConfig,
        "dev": DevConfig
    }

    @classmethod
    def ini_app(cls, app):
        use_class = cls.myclass.get(env)
        if use_class is None:
            raise ValueError("env required prd, dev or test")
        for key, value in use_class.__dict__.items():
            if not key.startswith("_"):
                setattr(cls, key, value)

        for key in dir(cls):
            if key.isupper():
                app.config[key] = getattr(cls, key)
