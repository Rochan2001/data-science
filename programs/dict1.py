# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:06:40 2019

@author: rochan
"""

inventory ={
 'gold':500,
 'pouch':['flint','twine','gemstone'],
 'backpack':['xylophone','dagger','bedroll','bread loaf']
}

inventory.update({'pocket':['seashelf','strange berry','lint']})
sb=sorted(inventory.get('backpack'))
print(sb)
sb.remove('dagger')
print(sb)
inventory['gold']=inventory['gold']+50
print(inventory['gold'])
inventory.update({'gold':[50,500]})
print(inventory)