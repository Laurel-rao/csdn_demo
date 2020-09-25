from flask import request, make_response
from flask_restful import Resource

from project.models import Device


class Information(Resource):
    def __init__(self):
        self.GET = request.args.to_dict()
        self.POST = request.json
        self.FILE = request.files.to_dict()
        self.keywords = [i for i in Device.__dict__.keys() if not i.startswith("_") and i != "values"]

    def get(self):
        return "get"

    def post(self):
        return "post"

    def download_file(self, filename):
        with open(filename, 'rb') as ff:
            data = ff.read()
        response = make_response(data)
        mime_type = "text/xlsx"
        response.headers["Content-type"] = mime_type
        response.headers["Content-Disposition"] = "attachment; filename={}".format(filename)
        return response
