import configparser

class Config:

    @classmethod
    def read_config_data(section, key):
        config = configparser.ConfigParser()
        config.read("../Configurations/Config.cfg")
        return config.get(section, key)


    @classmethod
    def fetch_elements_locators(section, key):
        config = configparser.ConfigParser()
        config.read("../Configurations/Elements.cfg")
        return config.get(section, key)
