#!/usr/bin/env python
import zarafa
import mailbox
import os
import shutil
from zarafa import Folder

ignored_folders = [ 'Suggested Contacts',
                    'Quick Step Settings',
                    'Conversation Action Settings',
                    'RSS Feeds',
                    'Junk E-mail',
                    'Tasks',
                    'Notes',
                    'Journal',
                    'Calendar',
                    'Contacts',
                    'Deleted Items',
                    'Outbox' ]

def mymbox(self, location):
    maildir = location.add_folder(self.name)
    maildir.lock()
    for item in self.items():
        maildir.add(item.eml())
    maildir.unlock()

Folder.mbox = mymbox

def format():
	wp = os.getcwd()
	for folder in os.listdir(wp):
	    wd = wp
	    wd = wd +'/'+ folder
	    os.mkdir(wd + '/Maildir')
	    
	    #Remove this if you do not want to mark mails as read
	    for dirname, dirnames, filenames in os.walk(wd):
	        for subdirname in dirnames:
	            if 'new' in subdirname:
	                for file in os.listdir(os.path.join(dirname, subdirname)):
	                    shutil.move(os.path.join(dirname, subdirname) + '/' + file, os.path.join(dirname, 'cur'))
	        
	
	    for folder in os.listdir(wd):
	        if (folder == ".Sent Items"):
	            shutil.move (wd + '/' + folder, wd + '/Maildir/Sent')
	        elif (folder == '.Inbox'):
	            for file in os.listdir(wd + '/' + folder):
	                shutil.move(wd + '/' + folder + '/' + file, wd + '/Maildir/')
	        elif (folder != 'cur' and folder != 'new' and folder != 'tmp' and folder != 'Maildir'):
                    shutil.move (wd + '/' + folder, wd + '/Maildir/' + folder)
def main():
    
    s = zarafa.Server()
    for user in s.users(remote=False):
        print 'user:', user.name
        if user.store:
            maildir = mailbox.Maildir(user.name)
            for folder in user.store.folders(recurse=True, parse=True):
                if folder.name in ignored_folders:
                    continue
                print '  folder: count=%s size=%s %s%s' % (str(folder.count).ljust(8), str(folder.size).ljust(10), folder.depth*'    ', folder.name)
                folder.mbox(maildir)
if __name__ == '__main__':
    main()
    format()
