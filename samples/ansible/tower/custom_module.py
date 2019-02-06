#!/usr/bin/python
#
# custom_module
#
from ansible.module_utils.basic import AnsibleModule 

def main():
    input = { 
         'start': {"required":False,"type":"str","default":""},
         'finish': {"required":False,"type":"str","default":""},
    } 
                  
    module = AnsibleModule(argument_spec=input)
#
#   python specific action code here
#
    module.exit_json(changed=False,meta=module.params)

if __name__ == '__main__': main()
