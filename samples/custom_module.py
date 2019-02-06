#!/usr/bin/python
#
# custom_module
#
from ansible.module_utils.basic import AnsibleModule 

def main():
    input = { 
         'start': {"required":False,"type":"str","default":"null"},
         'finish': {"required":False,"type":"str","default":"null"},
    } 
                  
    module = AnsibleModule(argument_spec=input)
#
# module specific Python code here....
#
    module.exit_json(changed=False,meta=module.params)

if __name__ == '__main__': main()
