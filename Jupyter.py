#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
#   Word Sorter
#   Copyright (C) 2018  Hemanya Sharma

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

import time
from random import randint

class colors:
    green = '\033[32;1;2m'
    endc = '\033[m'
    red = '\033[31;1m'
    bgred = '\033[1;5;31;44m'


print('\n' * 100)
print( colors.red + '\n\n[-RWARS : by Hemanya : type help-]' , colors.endc)
print(colors.bgred + '\n\n\n                            ------------------------ ')
print('                                     RWARS           ')
print('                            ------------------------' , colors.endc)
print ( colors.green + '''                      *                        ¸·´¯¯¯`·¸
                                             <,=====,>
                 , ·······,         *           `·......·´
       \¯¯¯¯,'          '·,
        ''¯¯¯¯¯¯¯¯¯¯¯¯¯/
          ¯¯`·,______, · ´
                                            *            *

         *                            |º
                                    º\|/º            *
    *            *           .·´¯¯¯¯¯¯¯¯'`·.
                          .·´      Ñë§§        `·.    *       *
       *           __¸·´___        _________`·¸__
                   `---\-------\      '|-----------------/---´
                     '\¯'\¯¯¯¯\     |¯¯¯¯¯¯¯¯¯/'¯/
                       ¯¯\¯¯¯¯\__|¯¯¯¯¯¯¯¯/¯¯
                            `·.___________.·´
                                    /____\
                                      '|| ||
                                      '|| ||
                                      '|| ||Æ¨ ''' , colors.endc)
print('\n10.03.2245 : RoBoNiX inc.')
time.sleep(1)
print('\nCTRL866 Re-Boot Sequence....')
time.sleep(1)
print('\nInitalizing Control Jupyter 866....')
time.sleep(1)
print(colors.green + '....' , colors.endc)
time.sleep(1)
print(colors.green + '....' , colors.endc)
time.sleep(1)
print('Laser offline...')
time.sleep(1)
print('Motion Tracker offline...')
time.sleep(1)
print('\nService Port available...')
time.sleep(1)
print(colors.green + '....' , colors.endc)
time.sleep(1)
print(colors.green + '....' , colors.endc)
print('\nControl Jupyter Active.')
time.sleep(1)
print('''\n\nYou are the 866 Control Jupyter aboard
the Jupyter Shuttle 'KERNEL'. Enemy Jupyters have boarded
and have taken over flight path. You are damaged & have been
re-initialized but your laser and motion tracker are offline.''')

def start(inventory):
	print('\n----------')
	print('\nJupyter mobile..')
	time.sleep(1)
	print(colors.green + '....' , colors.endc)
	time.sleep(1)
	print( colors.red + '\n[-MAIN ELEVATOR-]' , colors.endc)
	print('\n1.) deck 1 - Security')
	print('2.) deck 2 - Maintenance')
	print('3.) deck 3 - Cargo Hold - AirLock')
	print('4.) deck 4 - Jupyter Hangar')
	print('5.) deck 5 - Shuttle Control')
	print('6.) deck 6 - Observation\n')

	cmdlist = ['1', '2', '3', '4', '5', '6',]
	cmd = getcmd(cmdlist)

	if cmd == '1':
		security(inventory)
	elif cmd == '2':
		if 'Jupyter hack' in inventory:
			print( colors.red + '\n- DECK 2 - MAINTENANCE LOCKED -' , colors.endc)
			time.sleep(2)
			start(inventory)
		else:
			maintenance(inventory)
	elif cmd == '3':
		cargo_hold(inventory)
	elif cmd == '4':
		if 'laser' in inventory:
			print( colors.red + '\n- DECK 4 - Jupyter HANGAR LOCKED -' , colors.endc)
			time.sleep(2)
			start(inventory)
		else:
			Jupyter_hangar(inventory)
	elif cmd == '5':
		shuttle_control(inventory)
	elif cmd == '6':
		if 'motion tracker' in inventory:
			print( colors.red + '\n- DECK 6 - OBSERVATION LOCKED -' , colors.endc)
			time.sleep(2)
			start(inventory)
		else:
			observation(inventory)

def maintenance(inventory):
	print('\n----------')
	print('\nJupyter mobile..')
	time.sleep(1)
	print(colors.green + '....' , colors.endc)
	time.sleep(1)
	print('''\nThis is the maintenance deck and it appears deserted.
You can see a terminated crew Jupyter, it has sustained
severe laser fire.''')
	print( colors.red + '\n[-MAINTENANCE-]\n' , colors.endc)
	print('1.) 716 Crew Jupyter')
	print('2.) Return to Main Elevator\n')

	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)
	if cmd == '1':
		crew_Jupyter(inventory)
	elif cmd == '2':
		start(inventory)

def crew_Jupyter(inventory, items=['Jupyter hack']):
	print('\n----------')
	print('''\n716 has a Jupyter hack program and it's connection
outlet is still intact. You can connect to this Jupyter with service
port and download the program.''')
	if len(items) > 0:
		for item in items:
			print('\n--> %s' % (item))
			print('\n\n1.) Exit.')
	cmdlist = ['service port', '1']
	cmd = getcmd(cmdlist)
	if cmd == 'service port':
			inventory.append('Jupyter hack')
			items = ['Jupyter hack']
			print('\nservice port connected.')
			time.sleep(1)
			print('accessing file..')
			time.sleep(1)
			print('downloading..')
			time.sleep(1)
			print(colors.green + '....' , colors.endc)
			time.sleep(1)
			print('\ndownload complete.')
			print('\nYou have the Jupyter hack program and return to the Main Elevator.')
			time.sleep(2)
			start(inventory)
	elif cmd == '1':
			maintenance(inventory)
	else:
		print('\n ERROR: invalid command')

def cargo_hold(inventory):
	print('\n----------')
	print('\nJupyter mobile..')
	time.sleep(1)
	print(colors.green + '....' , colors.endc)
	time.sleep(1)
	print('''\nYou enter the Cargo Hold, two Enemy Combat Jupyters
unload a barrage of laser fire at you. Their fire is very accurate
and you take a direct hit in your main CPU.''')
	print('\n[-CARGO HOLD - AIRLOCK-]')
	print(colors.green + '....' , colors.endc)
	time.sleep(1)
	print(colors.green + '....' , colors.endc)
	time.sleep(1)
	print('\nshutdown imminent...')
	time.sleep(1)
	print('CTRL866 offline.')
	time.sleep(1)
	print('Jupyter terminated.')
	print('\nGAME OVER\n')
	exit(0)

def Jupyter_hangar(inventory):
	print('\n----------')
	print('\nJupyter mobile..')
	time.sleep(1)
	print(colors.green + '....' , colors.endc)
	time.sleep(1)
	print('''\nThe Jupyter Hangar is filled with debri. There
is laser scoring everywhere and all Jupyters are terminated.
In the corner there is one inactive repair Jupyter still in his security
cylinder. You can initialise the Jupyter to repair your laser but you will
require a 3 digit access code.\n''')
	print( colors.red + '[-Jupyter HANGAR-]' , colors.endc)
	print('\n1.) Repair Jupyter 3 digit code')
	print('2.) Return to Main Elevator')

	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)

	if cmd == '1':
		access_code(inventory)
	elif cmd == '2':
		start(inventory)

def access_code(inventory):
	code = '%d%d%d' % (randint(0,9), randint(0,9), randint(0,9))
	guess = input('\n[KEYPAD]> ')
	guesses = 0

	while guess != code and guess != 'yu8xxj3' and guesses <4:
		print('\n* ACCESS - DENIED *')
		guesses += 1
		guess = input('\n[KEYPAD]> ')

	if guess == code or guess == 'yu8xxj3':
		repair_Jupyter(inventory)
	else:
		print('\n....')
		time.sleep(1)
		print('\n....')
		time.sleep(1)
		print('\nKEYPAD - LOCKED')
		time.sleep(1)
		print('\ncode randomizing..')
		time.sleep(1)
		print('\nKEYPAD - OPEN')
		time.sleep(1)
		Jupyter_hangar(inventory)

def repair_Jupyter(inventory, items=['laser']):
	print('\n\n----------')
	print('\nREP323 boot sequence....')
	time.sleep(1)
	print('Initalizing Repair Jupyter 323....')
	time.sleep(1)
	print(colors.green + '....' , colors.endc)
	time.sleep(1)
	print(colors.green + '....' , colors.endc)
	time.sleep(1)
	print('Repair Jupyter Active.')
	time.sleep(1)
	print('''\nThe Repair Jupyter is now active. You MUST connect to
this Jupyter with service port to repair laser.''')

	if len(items) > 0:
		for item in items:
			print('\n--> %s' % (item))
	cmdlist = ['service port']
	cmd = getcmd(cmdlist)
	if cmd == 'service port':
			inventory.append('laser')
			items = ['laser']
			print('\nservice port connected.')
			time.sleep(1)
			print('Repairing Laser...')
			time.sleep(1)
			print('Auto alignment...')
			time.sleep(1)
			print(colors.green + '....' , colors.endc)
			time.sleep(1)
			print('\nLASER ONLINE.')
			print('''\nYour laser is now online. You de-activate the Repair
Jupyter and return to the Main Elevator.''')
			time.sleep(2)
			start(inventory)
	else:
		print('\n ERROR invalid command-')

def security(inventory):
	print('\n----------')
	print('\nJupyter mobile..')
	time.sleep(1)
	print(colors.green + '....' , colors.endc)
	time.sleep(1)
	print('''\nYou are on the Security Deck. This is where all
surveillance aboard the shuttle is done. Sentry Jupyter 343 has been
terminated. You MUST access the Sentry Jupyter's logs but you
will have to hack the data recorder.\n''')
	print( colors.red + '[-SECURITY-]\n' , colors.endc)
	print('1.) View Surveillance monitors on other decks')
	print('2.) Hack Sentry Jupyter 343')
	print('3.) Return to main elevator')

	cmdlist =['1', '2', '3']
	cmd = getcmd(cmdlist)

	if cmd == '1':
		print('\n----------')
		print('\nBooting Computers....')
		time.sleep(1)
		print(colors.green + '....' , colors.endc)
		time.sleep(1)
		print('...')
		time.sleep(1)
		print('Monitors active.')
		time.sleep(1)
		print( colors.red + '\n[-SURVEILLANCE FEED-]' , colors.endc)
		print('''\n-The Hangar monitor is offline you have no live feed.
\n-In the Cargo hold there are two Enemy Combat Jupyters patroling.
\n-The Maintenance deck looks clear except for a few terminated Jupyters.
\n-An Elite Enemy Command Jupyter is posted on the Shuttle Control deck.
\n-Observation shows a Enemy Sentry Jupyter.''')
		time.sleep(2)
		security(inventory)

	elif cmd == '2':
		if 'Jupyter hack' in inventory:
			print('\nloading Jupyter hack....')
			time.sleep(2)
			print(colors.green + '....' , colors.endc)
			time.sleep(2)
			print('10000101010101010101010' * 1000)
			time.sleep(1)
			print(colors.green + '....' , colors.endc)
			time.sleep(1)
			print('Accessing encrypted files...')
			time.sleep(2)
			print('Decrypting....')
			time.sleep(2)
			print('\n\n[-SEN343 LOG-]')
			time.sleep(1)
			print('\n\nDAILY OVER-RIDE CODES- HANGAR JupyterS')
			time.sleep(1)
			print('\n\n-Combat Jupyters - szb41ee')
			time.sleep(1)
			print('\n\n-Sentry Jupyters - qr66mop')
			time.sleep(1)
			print('\n\n-Repair Jupyters - yu8xxj3')
			time.sleep(1)
			print('\n\nCODES WILL BE RESET EVERY 24 HOURS')
			security(inventory)
		else:
			print('\n- ACCESS TO DATA RECORDER DENIED -')
			time.sleep(2)
			security(inventory)

	elif cmd == '3':
		start(inventory)

def observation(inventory):
	print('\n----------')
	print('\nJupyter mobile..')
	time.sleep(1)
	print(colors.green + '....' , colors.endc)
	time.sleep(1)
	print('''\nYou enter the Observation deck and are confronted
with a Enemy Sentry Jupyter beside a disabled crew Jupyter.
His laser is almost charged and will be active in seconds.\n''')
	print( colors.red + '[-OBSERVATION-]\n' , colors.endc)
	print('1.) Terminate Sentry Jupyter')
	print('2.) Retreat to Main Elevator.')

	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)

	if cmd == '1':
		if 'laser' in inventory:
			print('\nlaser active...')
			time.sleep(1)
			print('target locked...')
			time.sleep(1)
			print('...')
			time.sleep(1)
			print('\nTARGET TERMINATED\n')
			enemy_sentry(inventory)
		else:
			print('\n- WARNING LASER OFFLINE -')
			time.sleep(2)
			print('''\nThe Sentry Jupyters laser is now active and has you locked
on. You try to initiate self-destruct but its to late..''')
			print(colors.green + '....' , colors.endc)
			time.sleep(1)
			print(colors.green + '....' , colors.endc)
			time.sleep(1)
			print('\nshutdown imminent...')
			time.sleep(1)
			print('CTRL866 offline.')
			time.sleep(1)
			print('Jupyter terminated.')
			print( colors.red + '\nGAME OVER\n' , colors.endc)
			exit(0)

	elif cmd == '2':
			print('''\nThe Sentry Jupyters laser is now active and has you locked
on. You try to retreat back to the elevator but its to late..''')
			print(colors.green + '....' , colors.endc)
			time.sleep(1)
			print(colors.green + '....' , colors.endc)
			time.sleep(1)
			print('\nshutdown imminent...')
			time.sleep(1)
			print('CTRL866 offline.')
			time.sleep(1)
			print('Jupyter terminated.')
			print( colors.red + '\nGAME OVER\n' , colors.endc)
			exit(0)

def enemy_sentry(inventory, items=['motion tracker']):
	print('\n----------')
	time.sleep(1)
	print('''\nThe Enemy Sentry Jupyter has been terminated.
Judging by the model you know he has a
motion tracker repair program installed. You MUST connect
to this Jupyter with service port and download the program.''')
	if len(items) > 0:
		for item in items:
			print('\n--> %s' % (item))
	cmdlist = ['service port']
	cmd = getcmd(cmdlist)
	if cmd == 'service port':
			inventory.append('motion tracker')
			items = ['motion tracker']
			print('\nservice port connected.')
			time.sleep(1)
			print('accessing file..')
			time.sleep(1)
			print('downloading..')
			time.sleep(1)
			print(colors.green + '....' , colors.endc)
			time.sleep(1)
			print('Repairing Motion Tracker...')
			time.sleep(1)
			print('Auto alignment...')
			time.sleep(1)
			print(colors.green + '....' , colors.endc)
			time.sleep(2)
			print('\nMOTION TRACKER ONLINE.')
			time.sleep(2)
			print('''\nYour Motion Tracker is now online.
You return to the main elevator''')
			start(inventory)

def shuttle_control(inventory):
	print('\n----------')
	print('\nJupyter mobile..')
	time.sleep(1)
	print(colors.green + '....' , colors.endc)
	time.sleep(1)
	print('''\nYou enter Shuttle Control where all navigation takes place.
A 999 Elite Enemy Command Jupyter is posted here.
This Jupyter is extremely powerfull.''')
	print( colors.red + '\n[-SHUTTLE CONTROL-]' , colors.endc)
	print('\n1.) Terminate the 999 Elite Enemy Command Jupyter')
	print('2.) Retreat to Main Elevator')
	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)

	if cmd == '1':
		if 'laser' in inventory and 'motion tracker' in inventory and 'Jupyter hack' in inventory:
			print('\n....')
			time.sleep(1)
			print('\n....')
			command_Jupyter(inventory)
		else:
			time.sleep(1)
			print('\nEECD999:>')
			print('\n100101010101010101010101010101010' * 10)
			time.sleep(1)
			print('''\nThe Elite Enemy Command Jupyter laughs in machine language
at your pathetic attempt. The last thing your data recorder gets is the
deafing sound of a Target Lock.''')
			print(colors.green + '....' , colors.endc)
			time.sleep(1)
			print(colors.green + '....' , colors.endc)
			time.sleep(1)
			print('\nshutdown imminent...')
			time.sleep(1)
			print('CTRL866 offline.')
			time.sleep(1)
			print('Jupyter terminated.')
			print('\nGAME OVER\n')
			exit(0)
	elif cmd == '2':
		start(inventory)

def command_Jupyter(inventory):
	print('\nRunning Jupyter hack...')
	time.sleep(1)
	print('\njamming EECD999 Target Lock...')
	time.sleep(1)
	print('\n......')
	time.sleep(1)
	print('\nMotion Tracker active...')
	time.sleep(1)
	print('\nTrack motion of EECD999...')
	time.sleep(1)
	print('\n......')
	time.sleep(1)
	print('\nLaser active...')
	time.sleep(1)
	print('\nTargeting EECD999...')
	time.sleep(1)
	print('\nTarget Locked...')
	time.sleep(1)
	print('\n......')
	time.sleep(2)
	print('\n\nTARGET TERMINATED \n')
	time.sleep(2)
	print('''\n\nYou have defeated the EECD999 Jupyter and taken back control
of the 'KERNEL'. The flight path has been restored and
a distress signal sent to Jupyter Command. Reinforcements are inbound.
\n - GAME OVER -\n''')

def getcmd(cmdlist):
	cmd = input('\nCTRL866:> ')
	if cmd in cmdlist:
		return cmd
	elif cmd == 'help':
		print('\nTYPE: inventory to view items')
		print('or quit to self-destruct')
		return getcmd(cmdlist)
	elif cmd == 'inventory':
		print('\ninventory contains:\n')
		for item in inventory:
			print('-- %s' % (item))
		return getcmd(cmdlist)
	elif cmd == 'secret':
		print('\n........')
		time.sleep(1)
		print('\n[--ParaJupyter -- published by Hemanya 2018--]')
		time.sleep(1)
		print('\n[--written by Hemanya Sharma for Pine64 computer--]')
		time.sleep(1)
		print('\n[--play this game or program this game--]')
		time.sleep(1)
		print('\n........\n')
		return getcmd(cmdlist)
	elif cmd == 'quit':
		print('\n----------')
		time.sleep(1)
		print('\nself-destruct sequence initiated...')
		time.sleep(1)
		print('shutdown imminent...')
		time.sleep(1)
		print('\nCTRL866 offline.')
		time.sleep(1)
		print('Jupyter terminated.\n')
		exit(0)
	else:
		print('\n   error. invalid command-\n')
		return getcmd(cmdlist)

if __name__ == '__main__':
	inventory = ['service port']
	start(inventory)
