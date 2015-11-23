import json
class Jsonable(object):
    def to_json(self,vars_list):
        fields = vars(self)
        returnable_fields = {}
        for field in fields:
            if field in vars_list:
                returnable_fields[field] = fields[field]
        return json.dumps(returnable_fields)
