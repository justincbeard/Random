###############
# Notes
###############
## http://codingstyleguide.com/style/180/python-pythonic-way-to-implement-switchcase-statements
## Swtich Statement for python.  
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