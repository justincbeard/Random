#!/usr/bin/python
"""Allows users to control AWS EC2 instances.
So far it allows for listing, starting and stopping"""

import boto.ec2
import argparse

def args_parse():
    """Sort through the various arguments for controlling instances"""
    parser = argparse.ArgumentParser(description="Manage AWS EC2 goodness")
    # group = parser.add_mutually_exclusive_group()
    # group.add_argument("-v", "--verbose", action = "store_true")
    # group.add_argument("-q", "--quiet", action = "store_true")
    parser.add_argument("-l", "--list", action="store_true", help="List instances in region")
    parser.add_argument("-r", "--region", metavar="Region ID", default="us-west-2", \
        help="Connect to specific region")
    parser.add_argument("-st", "--start", action="store_true", help="Start an Instance")
    parser.add_argument("-sp", "--stop", action="store_true", help="Stop an Instance")
    return parser.parse_args()


def list_instances(reservations):
    """Return a list of instances and their current state"""
    for res in reservations:
        for inst in res.instances:
            if 'Name' in inst.tags: # Pretty up the output just in case no name is set
                print "[%s] %s (%s)" % (inst.state, inst.tags['Name'], inst.id)
                print "Public DNS - %s \n" %(inst.public_dns_name)
            else:
                print "[%s] %s" % (inst.state, inst.id)
                print "Public DNS - %s \n" %(inst.public_dns_name)

def instance_select(reservations):
    """Build a list of instances to pass to an action (like start or stop)"""
    count = 1
    all_instances = {}
    inst_select_raw = []
    inst_select_ids = []
    for res in reservations:
        for inst in res.instances:
            if 'Name' in inst.tags: # Pretty up the output just in case no name is set
                print "%d - [%s] %s (%s)" % (count, inst.state, inst.tags['Name'], inst.id)
                all_instances[count] = inst.id
            else:
                print "%d - [%s] %s" % (count, inst.state, inst.id)
                all_instances[count] = inst.id
        count += 1
    inst_select_raw = raw_input("Select instance(s): ")
    inst_select = inst_select_raw.replace(',', ' ')
    inst_select = [int(x) for x in inst_select.split()]
    inst_select_ids = [all_instances[y] for y in inst_select]
    return inst_select_ids

def start_instance(inst_select_ids, conn):
    """Used for starting selected instances"""
    for inst in inst_select_ids:
        print 'Starting %s' % (inst)
        conn.start_instances(inst)

def stop_instance(inst_select_ids, conn):
    """Used for stopping selected instances"""
    for inst in inst_select_ids:
        print 'Stopping %s' % (inst)
        conn.stop_instances(inst)


def main():
    """Parse user's arguments and select desired function"""
    args = args_parse()
    region_id = args.region
    conn = boto.ec2.connect_to_region(region_id)
    reservations = conn.get_all_reservations()

    # if args.verbose:
    #   print "Not Implemented yet"

    if args.list:
        list_instances(reservations)

    elif args.start:
        inst_select_ids = instance_select(reservations)
        start_instance(inst_select_ids, conn)

    elif args.stop:
        inst_select_ids = instance_select(reservations)
        stop_instance(inst_select_ids, conn)
    else:
        print "Hold up, that's not an option yet!"


if __name__ == '__main__':
    main()
