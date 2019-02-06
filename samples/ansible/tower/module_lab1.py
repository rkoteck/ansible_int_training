#!/usr/bin/python
#
# module_lab1
#
DOCUMENTATION = '''
---
module: custom_module 
short_description: a very simple module 
description: 
   - shows the structure of a module. 
version_added: "2.4" 
author: Phil LoVecchio 
options: 
  start: 
     description: 
          - first argument 
  finish: 
     description: 
          - second argument 
'''

EXAMPLES = '''
- name: descriptive string 
  custom_module:
    start: first-value 
    finish: second-value 
'''
from ansible.module_utils.basic import AnsibleModule 

def main():
    input = { 
         'start': {"required":False,"type":"str","default":""},
         'finish': {"required":False,"type":"str","default":""},
    } 
                  
    module = AnsibleModule(argument_spec=input)
#
#   python specific code here
#
    module.exit_json(changed=False,meta=module.params)

if __name__ == '__main__': main()
