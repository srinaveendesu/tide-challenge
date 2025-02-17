import re
import validators

def validate_domain(doman_name):
    match = re.search(r'^http[s]?:',doman_name)
    if not match:
        doman_name = 'http://' + str(doman_name)
    domain = validators.url(doman_name)
    if isinstance(domain, validators.utils.ValidationFailure):
        return False
    return True

def validator(db, data):
    flag = False
    resp_data = ['name','domain']
    resp_lst =filter(lambda x:x not in resp_data,list(data.keys()))
    if len(list(resp_lst)) != 0:
        return 'Invalid request data', data, flag
    if data['name'].lower() in db.keys():
        return 'Company already exists in DB', data, flag
    val_domain = validate_domain(data['domain'])
    flag = val_domain
    if not val_domain:
        return 'Domain name is not valid', data, flag
    if flag:
        return 'Company is being added to DB', data, flag
    
def find_company(db,data):
    flag = False
    full_keys = list(db.keys())
    full_values = list(db.values())
    name_keys = list(zip(*full_keys))
    index = 0
    if data['name'].capitalize() in name_keys[0]:
        flag = True
        index = name_keys[0].index(data['name'].capitalize())
    for val in full_values:
        print('validator')
        print(val.name, val.domain)

    if flag:
        return full_keys[index], data, flag
    else:
        return None, data, flag
    