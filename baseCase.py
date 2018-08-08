import yaml
import os


class baseCase():
    email = {}
    '''get file location'''
    def get_template_path(self, path):
        file_path = os.path.join(os.getcwd(), path)
        if not os.path.isfile(file_path):
            raise Exception('File Path Not Exist')
        else:
            return file_path

    '''read yaml file'''
    def read_yaml(self, file):
        file = self.get_template_path(file)
        with open(file, 'r') as stream:
            try:
                self.email = yaml.load(stream)
            except yaml.YAMLError as exc:
                raise Exception('File Not Found')
        return self.email
