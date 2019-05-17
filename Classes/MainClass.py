#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import html5lib
import random
import requests
from requests_futures.sessions import FuturesSession
import threading
from tqdm import tqdm
import socket
import socks
import time
import urllib.request, urllib.error, urllib.parse
from urllib.request import urlopen

session = FuturesSession(max_workers=12)

blue = Fore.BLUE
red = Fore.RED
cyan = Fore.CYAN
green = Fore.GREEN
magenta = Fore.MAGENTA
RESET = Fore.RESET
DIM = Style.DIM
NORMAL = Style.NORMAL
BOLD = Style.BRIGHT
RESET_ALL = Style.RESET_ALL

class okadminfinder():
    """
    get_urls : get admin_panel links from text links_path
    create_link : create url using site & {admin_panel links}
    check_url : check url status 
    url : search for admin panel

    """
    def __init__(self):
            self.admin_count = 0
            self.admin_count1 = 0
            self.admin_count2 = 0
            self.__version__ = '2.6.0'
            self.__author__ = 'O.Koleda'
            self.__improver__= 'mIcHy AmRaNe'

    def getCredits(self):

        credit = print(green,BOLD,'''
     _______ _     _           _       _         ___ _           _             
    ( ______( )   | |         | |     (_)       / __(_)         | |            
    | |     | |___| |_____  __| |____  _ ____ _| |__ _ ____   __| |_____  ____ 
    | |   | |  _   _(____ |/ _  |    \| |  _ (_   __| |  _ \ / _  | ___ |/ ___)
    | |___| | |  \ \/ ___ ( (_| | | | | | | | || |  | | | | ( (_| | ____| |    
     \_____/|_|   \_\_____|\____|_|_|_|_|_| |_||_|  |_|_| |_|\____|_____|_|     
          version {} created by {} & rewrited by {}

        '''.format(self.__version__, self.__author__, self.__improver__,),RESET_ALL)
        return credit


    def get_agents():
        agents_path = 'LinkFile/user-agent.txt'
        with open(agents_path, 'r') as ua:
            for line in ua:
                rua = random.choice(list(ua))
                headers = {'user-agent': rua}
        return headers

    def proxy(self, prox):
        proxies ={
        'http': prox,
        'https': prox,
        }
        try:
            ht = prox.split(':')
            pr = int(ht[1])
            s = socks.socksocket()
            s.set_proxy(socks.HTTP, ht[0], pr)
            socket.socket = socks.socksocket
            urllib.request.urlopen
        except (IndexError, IndentationError):
            print('\n\tPlease check the format of your proxy | reminder: 127.0.0.1:8080 ')
            quit(0)
        try:
            print(blue, '\tChecking Http proxy...', end="\r")
            time.sleep(1)
            rp = session.get('http://testphp.vulnweb.com', proxies = proxies, timeout=10)
            print(blue,'\tChecking Http proxy...', green,RESET_ALL,BOLD, 'OK\n' ,RESET_ALL)
        except requests.exceptions.RequestException:
            print(blue, '\tChecking Http proxy...', red,RESET_ALL,BOLD, 'BAD\n' ,RESET_ALL)
            print('\n ╔═══[!] Connection Troubles')
            print(' ║')
            print(' ╚══►' ,blue, '[Note]' ,magenta, '╾╥──╸ Please check your connection, proxy or tor')
            print('            ╟──╸ ' ,magenta,RESET_ALL,BOLD, 'don\'t add' ,magenta,NORMAL, ' \'http://\' or \'https://\'')
            print('            ╙──╸ ' ,magenta,NORMAL, 'check that you have written the url correctly\n')
            quit(0)
        return proxies
    
    @staticmethod
    def get_urls(site):
        links_path = 'LinkFile/adminpanellinks.txt'
        links = []
        with open(links_path, 'r') as apl:
            for line in apl:
                links.append(line.replace('\n', ''))
                # Debug mode
                # print(line.format(site))
        return links
    
    @staticmethod
    def create_link(site, sub_link, proxies):
        if sub_link[0:3] == '{}/':
            req_link = sub_link .format(site)
        else:
            if site[0:4] == 'www.':
                site = site.replace('www.', '')
                req_link = 'www.' + sub_link .format(site)
            else:
                req_link = sub_link .format(site)
        return req_link

    def check_url(self, site, proxies):
        try:
            req = session.get('http://{}'.format(site), proxies = proxies)
            req.result().raise_for_status()
            # Debug mode
            return True
        except (requests.exceptions.RequestException, requests.HTTPError):
            #Debug mode
            # print('bad')
            return False

    def url(self, site, proxies, fast):
        if fast is False:
            urls = okadminfinder.get_urls(site)

            try:
                if okadminfinder.check_url(self, site, proxies):
                    print(blue, DIM, '{}'.format(site),RESET_ALL,green, 'is stable\n', RESET_ALL)
                else:
                    print('something wrong with url')
                    exit(SystemExit)
                total_count = len(urls)
                admin_count = 0
                pbar = tqdm(total=total_count, bar_format=('{l_bar}'+DIM+'{bar}'+RESET_ALL+'|{n_fmt}/{total_fmt}{postfix}'))

                for url in urls:
                    pbar.update()
                    req_link = okadminfinder.create_link(site, url, proxies)
                    bs = session.get('http://{}'.format(site), proxies = proxies)
                    try:
                        pff = session.get('http://' + req_link, proxies = proxies)
                        soup1 = BeautifulSoup(bs.result().content, 'html5lib').title.string
                        soup11 = BeautifulSoup(pff.result().content, 'html5lib').title.string
                        if okadminfinder.check_url(site, req_link, proxies) and soup1 != soup11:
                            admin_count += 1
                            print(BOLD,blue, '{:<54}'.format('\t[✔] http://' + req_link), RESET_ALL,BOLD,green, '{:>29}'.format('Admin page found\n'), RESET_ALL)
                        else:
                            continue                    
                    except AttributeError:
                        if okadminfinder.check_url(site, req_link, proxies):
                            admin_count += 1
                            print(BOLD,blue, '{:<54}'.format('\t[✔] http://' + req_link), RESET_ALL,BOLD,green, '{:>29}'.format('Admin page found\n'), RESET_ALL)
                        else:
                            continue

                print('\n\n\t╔═[✔️ ]',green,BOLD,' Completed',RESET_ALL)
                print('\t╟───╸📑️', str(admin_count), 'Admin pages found')
                print('\t╙───╸📚️', str(total_count), 'total pages scanned')

            except(KeyboardInterrupt, SystemExit):
                print('Session Canceled')

            except():
                print('Session Canceled')

        else:
            url_list = okadminfinder.get_urls(site)
            parts = []
            for start_index in range(0, len(url_list), len(url_list) // 3):
                end_index = start_index + len(url_list)//3
                parts.append(url_list[start_index:end_index])

            try:
                if okadminfinder.check_url(self, site, proxies):
                    print(blue, DIM, '{}'.format(site),RESET_ALL,green, 'is stable\n', RESET_ALL)
                else:
                    print('something wrong with url')
                    exit(SystemExit)
                total_count = len(parts[0] + parts[1] + parts[2])
                pbar = tqdm(total=total_count, bar_format=('{l_bar}'+DIM+'{bar}'+RESET_ALL+'|{n_fmt}/{total_fmt}{postfix}'))
                pbar.set_description('🌀️ Processing ...')

                def part():
                    for url in parts[0]:
                        pbar.update()
                        req_link = okadminfinder.create_link(site, url, proxies)
                        bs = session.get('http://{}'.format(site), proxies = proxies)
                        try:
                            pff = session.get('http://' + req_link, proxies = proxies)
                            soup1 = BeautifulSoup(bs.result().content, 'html5lib').title.string
                            soup11 = BeautifulSoup(pff.result().content, 'html5lib').title.string
                            if okadminfinder.check_url(site, req_link, proxies) and soup1 != soup11:
                                self.admin_count += 1
                                print(BOLD,blue, '{:<54}'.format('\t[✔] http://' + req_link), RESET_ALL,BOLD,green, '{:>29}'.format('Admin page found\n'), RESET_ALL)
                            else:
                                continue                    
                        except AttributeError:
                            if okadminfinder.check_url(site, req_link, proxies):
                                self.admin_count += 1
                                print(BOLD,blue, '{:<54}'.format('\t[✔] http://' + req_link), RESET_ALL,BOLD,green, '{:>29}'.format('Admin page found\n'), RESET_ALL)
                            else:
                                continue

                def part1():
                    for url in parts[1]:
                        pbar.update()
                        req_link = okadminfinder.create_link(site, url, proxies)
                        bs = session.get('http://{}'.format(site), proxies = proxies)
                        try:
                            pff = session.get('http://' + req_link, proxies = proxies)
                            soup2 = BeautifulSoup(bs.result().content, 'html5lib').title.string
                            soup22 = BeautifulSoup(pff.result().content, 'html5lib').title.string
                            if okadminfinder.check_url(site, req_link, proxies) and soup2 != soup22:
                                self.admin_count1 += 1
                                print(BOLD,blue, '{:<54}'.format('\t[✔] http://' + req_link), RESET_ALL,BOLD,green, '{:>29}'.format('Admin page found\n'), RESET_ALL)
                            else:
                                continue                    
                        except AttributeError:
                            if okadminfinder.check_url(site, req_link, proxies):
                                self.admin_count1 += 1
                                print(BOLD,blue, '{:<54}'.format('\t[✔] http://' + req_link), RESET_ALL,BOLD,green, '{:>29}'.format('Admin page found\n'), RESET_ALL)
                            else:
                                continue


                def part2():
                    for url in parts[2]:
                        pbar.update()
                        req_link = okadminfinder.create_link(site, url, proxies)
                        bs = session.get('http://{}'.format(site), proxies = proxies)
                        try:
                            pff = session.get('http://' + req_link, proxies = proxies)
                            soup3 = BeautifulSoup(bs.result().content, 'html5lib').title.string
                            soup33 = BeautifulSoup(pff.result().content, 'html5lib').title.string
                            if okadminfinder.check_url(site, req_link, proxies) and soup3 != soup33:
                                self.admin_count2 += 1
                                print(BOLD,blue, '{:<54}'.format('\t[✔] http://' + req_link), RESET_ALL,BOLD,green, '{:>29}'.format('Admin page found\n'), RESET_ALL)
                            else:
                                continue                    
                        except AttributeError:
                            if okadminfinder.check_url(site, req_link, proxies):
                                self.admin_count2 += 1
                                print(BOLD,blue, '{:<54}'.format('\t[✔] http://' + req_link), RESET_ALL,BOLD,green, '{:>29}'.format('Admin page found\n'), RESET_ALL)
                            else:
                                continue

                t = threading.Thread(target=part)
                t1 = threading.Thread(target=part1)
                t2 = threading.Thread(target=part2)
                t.start()
                t1.start()
                t2.start()
                t.join()
                t1.join()
                t2.join()

                admin_countT = self.admin_count + self.admin_count1 + self.admin_count2
                time.sleep(0.17)
                print('\n\n\t╔═[✔️ ]',green,BOLD,' Completed',RESET_ALL)
                print('\t╟───╸📑️', str(admin_countT), 'Admin pages found')
                print('\t╙───╸📚️', str(total_count), 'total pages scanned')
            except(KeyboardInterrupt, SystemExit):
                print('Session Canceled')

            except():
                print('Session Canceled')
