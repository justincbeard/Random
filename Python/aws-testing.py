#!/usr/bin/python

import boto.ec2

region_id = "us-west-2"

conn = boto.ec2.connect_to_region(region_id)
reservations = conn.get_all_reservations()
#instance = reservations[0].instances[0]
#print instance.public_dns_name

## Need a switch statement and this seems to be the cleanest way
# class switch(object):
#     def __init__(self, value):
#         self.value = value
#         self.fall = False

#     def __iter__(self):
#         """Return the match method once, then stop"""
#         yield self.match
#         raise StopIteration
    
#     def match(self, *args):
#         """Indicate whether or not to enter a case suite"""
#         if self.fall or not args:
#             return True
#         elif self.value in args: 
#             self.fall = True
#             return True
#         else:
#             return False

def list_instances(reservations):
	for res in (reservations):
		for inst in res.instances:
			if 'Name' in inst.tags:
				print "[%s] %s (%s)" % (inst.state, inst.tags['Name'], inst.id)
				print "Public DNS - %s \n" %(inst.public_dns_name)
			else:
				print "[%s] %s" % (inst.id, inst.state)
				print "Public DNS - %s \n" %(inst.public_dns_name)

def test_instance(instance_id):
	for inst in (instance_id):
		print inst

def start_instance(instance_id):
	for inst in (instance_id):
		print inst
		conn.start_instances(inst)

def stop_instance(instance_id):
	for inst in (instance_id):
		print inst
		conn.stop_instances(inst)

# print "1) List all reservations"
# print "2) Start an instance"
# print "3) Stop an instance"

loop = 1
while loop == 1:
	action = raw_input("Selection: ")
	for case in switch(action):
		if case("1"):
			loop = 0
			list_instances(reservations)
		elif case("2"):
			loop = 0 
			instance_id_raw = raw_input("Instance ID: ")
			instance_id = instance_id_raw.replace(' ','').split(',')
			start_instance(instance_id)
		elif case("3"):
			loop = 0
			instance_id_raw = raw_input("Instance ID: ")
			instance_id = instance_id_raw.replace(' ','').split(',')
			stop_instance(instance_id)
		else:
			print "Select something different"


###############
# Notes
###############
#http://codingstyleguide.com/style/180/python-pythonic-way-to-implement-switchcase-statements

