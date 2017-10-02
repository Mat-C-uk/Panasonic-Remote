#! /usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################
#   All modificiations are open source.
#	Written by Mat Carpenter
#	Based on various open source code found all over the internet
#	THANKS TO THOSE THAT HELPED ALPHA TEST - Colly, Coolcaper, rhanson, autolog and Albartros
################################################################################


################################################################################
#	TODO'S:
#
#	TODO:
################################################################################
#
#	ALPHA UPDATE DETAILS
#
#	ALPHA 0.0.1 TO 0.0.12 TESTING CODE SNIPPETS AND PROOF OF CONCEPT
#
#	ALPHA 0.0.13
#	ATTEMPTED TO RESOLVE MEMORY ISSUE - RESOLVED
#	SORTED GETS INTO ONE FUNCTION
#	ADDED MAC ADDRESS TO DEVICE SETUP
#	ENABLED WAKE ON LAN
#	AMENDED STATUS TO ON, OFF & STANDBY
#	
#	ALPHA 0.0.14
#	ADDED SET VOLUME AND REWORKED GETS CONTROL
#	ADDED HDMI1 HDMI2 HDMI3 HDMI4
#	ADDED APPS CODE BUT NOT WORKING - HTTP 412 ERROR
#
#	ALPHA 0.0.15
#	RESOLVED ISSUE WITH TRIGGERS DEVICE STATES
#	COPYRIGHT DETAILS ADDED
#
#	ALPHA 0.0.16
#	RESOLVED ISSUE WITH Apps - added Netflix, youtube, Recorded tv (not checked)
#
#	ALPHA 0.0.17
#	ADDED LOTS OF APPS - CANT FIND BBCIPLAYER CODE
#	CORRECTED PLAY BUTTON NOT WORKING
#
#	ALPHA 0.0.18
#	ADDED MORE APPS - ADDED BBC IPLAYER AND BBC NEWS
#	APPS CAN BE PACKET SNIFFED BY WIRESHARK AND PROXY ON PORT 55000 - OPENING PANASONIN APP2, THEN OPENING APPS DOWNLOADS ALL THE APP NUMBERS
#	GUIDE NOW BRINGS UP GUIDE AND EPG NOW BRINGS UP EPG - GUIDE IS AN APP
#
#	NOTE IP:PORT/nrc/app_icon/APP NUMBER GETS APP PNG IMAGE


#	VERSION 0.1.0
#	DEBUGGING ADDED WITH TOGGLE IN PLUGIN MENU
#
#	VERSION 0.1.1
#	ADDED DELAY IN MULTI DIGET CHANNEL SELECTION
#
#	VERSION 0.1.2
#	ADDED VOLUME FROM SELECTED VARIABLE
#

import os
import sys
import requests
import time

from awake import wol


################################################################################
class Plugin(indigo.PluginBase):
################################################################################

	def __init__(self, pluginId, pluginDisplayName, pluginVersion, pluginPrefs):
		indigo.PluginBase.__init__(self, pluginId, pluginDisplayName, pluginVersion, pluginPrefs)
		self.debug = False


	def __del__(self):
		indigo.PluginBase.__del__(self)


	def shutdown(self):
		self.debugLog(u"shutdown called")

	def toggleDebugEnabled(self):
#       TOGGLE DEBUG ON/OFF
		debug_level = self.pluginPrefs.get('showDebugLevel', 1)
		
		if not self.debug:
			self.pluginPrefs['showDebugInfo'] = True
			self.debug = True
			self.debugLog(u"Debugging on")
		else:
			self.debug = False
			self.pluginPrefs['showDebugInfo'] = False
			indigo.server.log(u"Debugging off.")

################################################################################
#------------------------------------------------------------------------------#
#		SENDS TO TV'S
#------------------------------------------------------------------------------#
################################################################################

#	TODO: CHECK WORKING AS NOT TESTED
	def poweron(self, instruction, devId):
		dev=indigo.devices[devId]
		macaddress = dev.pluginProps["macaddress"]
		self.debugLog(macaddress)
		wol.send_magic_packet(macaddress)

	def poweroff(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_POWER-ONOFF"
		self.remote_control(sendme, dev)

	def chnum(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		decnum = pluginAction.props.get("setting")
		for digit in str((decnum)):
			time.sleep(0.3)
			sendme='NRC_D%s-ONOFF' % digit
			self.remote_control(sendme, dev)
		sendme="NRC_ENTER-ONOFF"
		self.remote_control(sendme, dev)

	def num0(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_D0-ONOFF"
		self.remote_control(sendme, dev)
		
	def num1(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_D1-ONOFF"
		self.remote_control(sendme, dev)
		
	def num2(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_D2-ONOFF"
		self.remote_control(sendme, dev)
		
	def num3(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_D3-ONOFF"
		self.remote_control(sendme, dev)
		
	def num4(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_D4-ONOFF"
		self.remote_control(sendme, dev)
		
	def num5(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_D5-ONOFF"
		self.remote_control(sendme, dev)
		
	def num6(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_D6-ONOFF"
		self.remote_control(sendme, dev)
		
	def num7(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_D7-ONOFF"
		self.remote_control(sendme, dev)

	def num8(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_D8-ONOFF"
		self.remote_control(sendme, dev)
		
	def num9(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_D9-ONOFF"
		self.remote_control(sendme, dev)
		
	def chup(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_CH_UP-ONOFF"
		self.remote_control(sendme, dev)
		
	def chdown(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_CH_DOWN-ONOFF"
		self.remote_control(sendme, dev)
		
	def inputtv(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_TV-ONOFF"
		self.remote_control(sendme, dev)
		
	def hdmi1(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_HDMI1-ONOFF"
		self.remote_control(sendme, dev)
		
	def hdmi2(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_HDMI2-ONOFF"
		self.remote_control(sendme, dev)
		
	def hdmi3(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_HDMI3-ONOFF"
		self.remote_control(sendme, dev)
		
	def hdmi4(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_VOD-ONOFF"
		self.remote_control(sendme, dev)
		
	def inputav(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_CHG_INPUT-ONOFF"
		self.remote_control(sendme, dev)
		
	def volup(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_VOLUP-ONOFF"
		self.remote_control(sendme, dev)
		
	def voldown(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_VOLDOWN-ONOFF"
		self.remote_control(sendme, dev)
		
	def mute(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_MUTE-ONOFF"
		self.remote_control(sendme, dev)
		
	def surround(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_SURROUND-ONOFF"
		self.remote_control(sendme, dev)
		
	def threed(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_3D-ONOFF"
		self.remote_control(sendme, dev)
		
	def noisered(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_P_NR-ONOFF"
		self.remote_control(sendme, dev)
		
	def display(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_DISP_MODE-ONOFF"
		self.remote_control(sendme, dev)
		
	def hold(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_HOLD-ONOFF"
		self.remote_control(sendme, dev)
		
	def ok(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_ENTER-ONOFF"
		self.remote_control(sendme, dev)
		
	def lastview(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_R_TUNE-ONOFF"
		self.remote_control(sendme, dev)
		
	def up(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_UP-ONOFF"
		self.remote_control(sendme, dev)
		
	def right(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_RIGHT-ONOFF"
		self.remote_control(sendme, dev)
		
	def down(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_DOWN-ONOFF"
		self.remote_control(sendme, dev)
		
	def left(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_LEFT-ONOFF"
		self.remote_control(sendme, dev)
		
	def home(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_HOME-ONOFF"
		self.remote_control(sendme, dev)
		
	def subs(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_STTL-ONOFF"
		self.remote_control(sendme, dev)

#		guide using app code		
	def guide(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0387878700000003" 
		self.remote_apps(sendme, dev)
		
	def menu(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_MENU-ONOFF"
		self.remote_control(sendme, dev)
		
	def info(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_INFO-ONOFF"
		self.remote_control(sendme, dev)
		
	def option(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_SUBMENU-ONOFF"
		self.remote_control(sendme, dev)
		
	def epg(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_EPG-ONOFF"
		self.remote_control(sendme, dev)
		
	def exit1(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_RETURN-ONOFF"
		self.remote_control(sendme, dev)
		
	def backto(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_CANCEL-ONOFF"
		self.remote_control(sendme, dev)
		
	def apps(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_APPS-ONOFF"
		self.remote_control(sendme, dev)
		
	def play(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_PLAY-ONOFF"
		self.remote_control(sendme, dev)
		
	def pause(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_PAUSE-ONOFF"
		self.remote_control(sendme, dev)
		
	def stop(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_STOP-ONOFF"
		self.remote_control(sendme, dev)
		
	def record(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_REC-ONOFF"
		self.remote_control(sendme, dev)
		
	def fforward(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_FF-ONOFF"
		self.remote_control(sendme, dev)
		
	def rewind(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_REW-ONOFF"
		self.remote_control(sendme, dev)
		
	def skipf(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_SKIP_NEXT-ONOFF"
		self.remote_control(sendme, dev)
		
	def skipb(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_SKIP_PREV-ONOFF"
		self.remote_control(sendme, dev)
		
	def red(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_RED-ONOFF"
		self.remote_control(sendme, dev)
		
	def green(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_GREEN-ONOFF"
		self.remote_control(sendme, dev)
		
	def yellow(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_YELLOW-ONOFF"
		self.remote_control(sendme, dev)
		
	def blue(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_BLUE-ONOFF"
		self.remote_control(sendme, dev)
		
	def none(self, instruction, devId):
		dev=indigo.devices[devId]
		sendme="NRC_EZ_SYNC-ONOFF"
		self.remote_control(sendme, dev)
		
################################################################################
#       GETS/SETS FROM/TO TV
################################################################################
		
	def get_vol(self, instruction, devId):
		dev=indigo.devices[devId]
		action="Get"
		sendme="Volume"
		prams = ""
		self.remote_get(sendme, action, prams, dev)
		
	def get_mute(self, instruction, devId):
		dev=indigo.devices[devId]
		action="Get"
		sendme="Mute"
		prams=""
		self.remote_get(sendme, action, prams, dev)
		
	def volnum(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		action="Set"
		sendme="Volume"
		setvolume = pluginAction.props.get("setvol")
		prams="<DesiredVolume>"+ setvolume + "</DesiredVolume>" 
		self.remote_get(sendme, action, prams, dev)
		
	def volvar(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		action="Set"
		sendme="Volume"
		tempy = int(pluginAction.props.get("setvar"))
		vargy = indigo.variables[tempy]
		setvolume=str(vargy.value)
		indigo.server.log ("volume change to " + setvolume)
		prams="<DesiredVolume>"+ setvolume + "</DesiredVolume>" 
		self.remote_get(sendme, action, prams, dev)
		
################################################################################
#       APPS
################################################################################

	def netflix(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0010000200000001" 
		self.remote_apps(sendme, dev)
		
	def youtube(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0070000200000001" 
		self.remote_apps(sendme, dev)

	def recordedtv(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0387878700000013" 
		self.remote_apps(sendme, dev)
		
	def mediaplayer(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0387878700000032" 
		self.remote_apps(sendme, dev)
		
	def dlnaplayer(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0387878700000014" 
		self.remote_apps(sendme, dev)

	def vieralink(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0387878700000016" 
		self.remote_apps(sendme, dev)
		
	def apptv(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0387878700000001" 
		self.remote_apps(sendme, dev)
		
		
	def web(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0077777700000002" 
		self.remote_apps(sendme, dev)
		
	def skype(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0070000600000001" 
		self.remote_apps(sendme, dev)
		
	def amazon(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0010000100000001" 
		self.remote_apps(sendme, dev)
		
	def hulu(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0010000F00000001" 
		self.remote_apps(sendme, dev)
		
	def accuweather(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0070000C00000001" 
		self.remote_apps(sendme, dev)
		
	def wsjlive(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0010001200000001" 
		self.remote_apps(sendme, dev)
		
	def mirroring(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0387878700000049" 
		self.remote_apps(sendme, dev)

	def touch(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0387878700000038" 
		self.remote_apps(sendme, dev)
		
	def reversi(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0387878700000037" 
		self.remote_apps(sendme, dev)

	def putthree(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0387878700000036" 
		self.remote_apps(sendme, dev)

	def jotter(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0387878700000022" 
		self.remote_apps(sendme, dev)

	def paint(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0387878700000026" 
		self.remote_apps(sendme, dev)	

	def rossiatv(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0020004000000001" 
		self.remote_apps(sendme, dev)	

	def pandora(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0010000600000001" 
		self.remote_apps(sendme, dev)
		
	def match(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0070001406000008" 
		self.remote_apps(sendme, dev)	

	def weather(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0070000900000001" 
		self.remote_apps(sendme, dev)	
		
	def vudo(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0010001300000001" 
		self.remote_apps(sendme, dev)
		
	def wuaki(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0020002A00000001" 
		self.remote_apps(sendme, dev)
		
	def bbcnews(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0020000A00000006" 
		self.remote_apps(sendme, dev)
		
	def bbciplayer(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0020000A00000005" 
		self.remote_apps(sendme, dev)
		
	def cinemanow(self, pluginAction):
		dev = indigo.devices[pluginAction.deviceId]
		devProps = dev.pluginProps
		sendme="0010000300000001"
		self.remote_apps(sendme, dev)	


################################################################################		
#------------------------------------------------------------------------------#
#       REMOTES
#------------------------------------------------------------------------------#
################################################################################

################################################################################
#       REMOTES - SEND COMMANDS
################################################################################

	def remote_control(self, sendme, dev):
		self.debugLog("Remote control send")
		self.debugLog(sendme)
		self.debugLog(dev)		
		url = "http://%s:55000/nrc/control_0" % dev.pluginProps["address"]
		payload = '<?xml version="1.0"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body><m:X_SendKey xmlns:m=\"urn:panasonic-com:service:p00NetworkControl:1\"><X_KeyEvent>%s</X_KeyEvent></m:X_SendKey></SOAP-ENV:Body></SOAP-ENV:Envelope>' % sendme
		headers = {
    		'SOAPaction': "\"urn:panasonic-com:service:p00NetworkControl:1#X_SendKey\"",
    		'Host':u"%s" % dev.pluginProps["address"],
    		'Content-Type': "text/xml",
    		'Content-Length': len(payload)
    		}
		try:	
			res=requests.post(url, data=payload, headers=headers, timeout= 3)
			self.debugLog("Resquests sending url, payload and headers")
			self.debugLog(url)
			self.debugLog(payload)
			self.debugLog(headers)
			self.debugLog(str(res.text))
			return res
		except:
			indigo.server.log("Panasonic TV remote failed - check TV is on and that IP address is correct.")

			
################################################################################
#       REMOTES - APPS 
################################################################################

	def remote_apps(self, sendme, dev):
		url = "http://%s:55000/nrc/control_0" % dev.pluginProps["address"]
		payload = '<?xml version="1.0"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body><m:X_LaunchApp xmlns:m=\"urn:panasonic-com:service:p00NetworkControl:1\"><X_AppType>vc_app</X_AppType><X_LaunchKeyword>product_id=%s</X_LaunchKeyword></m:X_LaunchApp></SOAP-ENV:Body></SOAP-ENV:Envelope>' % sendme
		headers = {
    		'SOAPaction': "\"urn:panasonic-com:service:p00NetworkControl:1#X_LaunchApp\"",
    		'Host':u"%s" % dev.pluginProps["address"],
    		'Content-Type': "text/xml",
    		'Content-Length': len(payload)
    		}
		try:	
			res=requests.post(url, data=payload, headers=headers, timeout= 3)
			self.debugLog(str(res.text))
			return res
		except:
			indigo.server.log("APP requested not functioning - check TV is on and that IP address is correct.")


################################################################################
#       REMOTES - GET/SETS INFORMATION
################################################################################

	def remote_get(self, sendme, action, prams, dev):
		url2 = "http://%s:55000/dmr/control_0" % dev.pluginProps["address"] 
		body = '<?xml version=\"1.0"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body>"<m:%s%s xmlns:m=\"urn:schemas-upnp-org:service:RenderingControl:1\"><InstanceID>0</InstanceID><Channel>Master</Channel>%s<%s></%s></m:%s%s></SOAP-ENV:Body></SOAP-ENV:Envelope>' % (action, sendme, prams, sendme, sendme, action, sendme)
		head = {
			'SOAPaction': "\"urn:schemas-upnp-org:service:RenderingControl:1#"+ action+sendme+"\"",
			'Host': u"%s" % dev.pluginProps["address"],
			'Content-Type': "text/xml",
			'Content-Length':  len(body)
			}
		try:
			res=requests.post(url2, data=body, headers=head, timeout = 1)
#			self.debugLog("Polling TV") 			
#			self.debugLog(str(res.text)) 

			if sendme=="Volume":
				if "200" in str(res):
					a=(res.text).find('<CurrentVolume>')
					b=(res.text)[a+15:a+18]
					c=int(b.strip("</"))
					dev.updateStateOnServer ("state", "on")
					dev.updateStateOnServer ("volume", c)
				if "400" in str(res):
					dev.updateStateOnServer ("state", "standby")
#				self.debugLog(str(res.text))
				return res
	
			if sendme=="Mute":
				if "200" in str(res):
					a=(res.text).find('<CurrentMute>')
					b =(res.text)[a+13:a+14]
					if b == "0":
						dev.updateStateOnServer ("mute", "off")
					else:
						dev.updateStateOnServer ("mute", "on")
				return res
				
			

		except:
			dev.updateStateOnServer ("state", "off")

	
################################################################################
#		runConcurrentThread() 
# 
#		Checks volume and mute every x seconds and updates respective status
################################################################################

	def runConcurrentThread(self):
		try:
			while True:
				for dev in indigo.devices.iter("self"):
					if not dev.enabled or not dev.configured:
						continue
					self.get_vol(self, dev)
					if dev.states["state"] == "on":
						self.get_mute(self, dev)
				self.sleep(1)
#				indigo.server.log ("LOG loop")  #DEBUG LEVEL NEEDS SETTING
		except self.StopThread:
			pass