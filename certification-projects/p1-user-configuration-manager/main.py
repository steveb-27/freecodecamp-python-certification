def add_setting(settings, new_setting):
    # new_setting should be touple
    # settings should be a dictionary

    key, value = new_setting
    key = key.lower()
    value = value.lower()
    print(key)
    if key in settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, new_setting):
    # new_setting should be touple
    # settings should be a dictionary

    key, value = new_setting
    key = key.lower()
    value = value.lower()

    if key not in settings.keys():
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    else:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

def delete_setting(settings, key):
    # key should be string
    # settings should be a dictionary

    key = key.lower()

    if key not in settings.keys():
        return "Setting not found!"
    else:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"

def view_settings(settings):
    # settings should be a dictionary
    if len(settings) == 0:
        return "No settings available."

    output = 'Current User Settings:\n'
    for key,value in settings.items():
        output += f"{key.title()}: {value.lower()}\n"
    return output

test_settings = {
    'theme': 'dark',
    'notifications':
    'enabled',
    'volume': 'high'}

update_setting(test_settings, ('theme','LIGHT'))
print(add_setting(test_settings, ('THEME','person')))
delete_setting(test_settings, 'notifications')

print(view_settings(test_settings))