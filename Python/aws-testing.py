#!/usr/bin/python

import boto.ec2
import argparse

region_id = "us-west-2"

conn = boto.ec2.connect_to_region(region_id)
reservations = conn.get_all_reservations()

def parseArgs():
	parser = argparse.ArgumentParser(description = "Manage AWS EC2 goodness")
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-v", "--verbose", action = "store_true")
	group.add_argument("-q", "--quiet", action = "store_true")
	parser.add_argument("-l", "--list", action = "store_true", help = "List instances in region")
	parser.add_argument("-r", "--region", metavar = "Region ID", help = "Connect to specific region")
	parser.add_argument("-st", "--start", action = "store_true", help = "Start an Instance")
	parser.add_argument("-sp", "--stop", action = "store_true", help = "Stop an Instance")
	return parser.parse_args()


def list_instances(reservations):
	for res in (reservations):
		for inst in res.instances:
			if 'Name' in inst.tags:    ## Pretty up the output just in case no name is set
				print "[%s] %s (%s)" % (inst.state, inst.tags['Name'], inst.id)
				print "Public DNS - %s \n" %(inst.public_dns_name)
			else:
				print "[%s] %s" % (inst.state, inst.id)
				print "Public DNS - %s \n" %(inst.public_dns_name)

def instance_select(reservations):
	count = 1;    ## Counter so we can associate all Instance IDs with a number
	allInstances = {}    ## Dictionary of all Instance IDs.  count will be the index
	instSelectRaw = []    ## The raw_input of the users selection
	instSelectIds = []    ## The final selection to be returned and actioned upon
	for res in (reservations):
		for inst in res.instances:
			if 'Name' in inst.tags:  ## Pretty up the output just in case no name is set
				print "%d - [%s] %s (%s)" % (count, inst.state, inst.tags['Name'], inst.id)
				allInstances[count] = inst.id
			else:
				print "%d - [%s] %s" % (count, inst.state, inst.id)
				allInstances[count] = inst.id
		count += 1
	instSelectRaw = raw_input("Select instance(s): ")
	instSelect = instSelectRaw.replace(',',' ')    ## Account for space or comma separated
	instSelect = map(int, instSelect.split())    ## Map the input into a list of integers
	instSelectIds = [allInstances[x] for x in instSelect]  ## Iterate over the selected instances and match to instance IDs 
	return instSelectIds

def test_instance(instance_id):
	for inst in (instance_id):
		print inst

def start_instance(instSelectIds):
	for inst in instSelectIds:
		print 'Starting %s' % (inst)
		conn.start_instances(inst)

def stop_instance(instSelectIds):
	for inst in (instSelectIds):
		print 'Stopping %s' % (inst)
		conn.stop_instances(inst)


def main():
	args = parseArgs()

	if args.verbose:
		print "Not Implemented yet"

	elif args.list:
		list_instances(reservations)

	elif args.start:
		instSelectIds = instance_select(reservations)
		start_instance(instSelectIds)

	elif args.stop:
		instSelect = instance_select(reservations)
		stop_instance(instSelect)
	else:
		print "Hold up, that's not an option yet!"


if __name__ == '__main__':
	main()