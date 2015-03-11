#!/usr/bin/python

import boto.ec2

region_id = "us-west-2"

conn = boto.ec2.connect_to_region(region_id)
reservations = conn.get_all_reservations()
#instance = reservations[0].instances[0]
#print instance.public_dns_name

def list_instances(reservations):
	for res in (reservations):
		for inst in res.instances:
			if 'Name' in inst.tags:
				print "[%s] %s (%s)" % (inst.state, inst.tags['Name'], inst.id)
				print "Public DNS - %s \n" %(inst.public_dns_name)
			else:
				print "[%s] %s" % (inst.id, inst.state)
				print "Public DNS - %s \n" %(inst.public_dns_name)

def stop_instance(instance_id):
	for inst in instance_id:
		conn.stop_instances(inst)

def start_instance(instance_id):
	for inst in instance_id:
		conn.start_instances(inst)

"List all reservations"
"Start an instance"
"Stop an instance"

instance_id = "test"

avail_actions = {
	'1)': list_instances(reservations),
	'2)': start_instance(instance_id),
	'3)': stop_instance(instance_id)
}
action = raw_input("Selection: ")
instance_id = raw_input("Instance ID: ")

## Notes: http://codingstyleguide.com/style/180/python-pythonic-way-to-implement-switchcase-statements

