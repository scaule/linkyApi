#!/usr/bin/env python
# Thx for
# -*- coding: utf-8 -*-

import base64
import requests

class Linky:

    def __init__(self, login, password):
        self.LOGIN_URI = "https://espace-client-connexion.enedis.fr/auth/UI/Login"
        self.API_URI = "https://espace-client-particuliers.enedis.fr/group/espace-particuliers/jeconsultetelechargemesdonneesdeconsommation"

        # Login to linky website and save session
        self.session = requests.Session()

        datas = {'IDToken1': login,
                               'IDToken2': password,
                               'SunQueryParamsString': base64.b64encode(b'realm=particuliers'),
                               'encoded': 'true',
                               'gx_charset': 'UTF-8'}
        req = self.session.post(self.LOGIN_URI, data=datas, allow_redirects=False)

        #it's not a hash but it's a wtf string :D
        self.hash = 'lincspartdisplaycdc_WAR_lincspartcdcportlet_INSTANCE_partlincspartcdcportlet'

    def getConsumptionPerYear(self):
        return self._callWebsite('urlCdcAn')

    def getConsumptionPerMonth(self, start, end):
        return self._callWebsite('urlCdcMois', start, end)

    def getConsumptionPerDay(self, start, end):
        return self._callWebsite('urlCdcJour', start, end)

    def getConsumptionPerHour(self, start, end):
        return self._callWebsite('urlCdcHeure', start, end)

    def _callWebsite(self, resource, start=None, end=None):
        #Set data array with start date and en date
        datas = {
            '_' + self.hash + '_dateDebut': start,
            '_' + self.hash + '_dateFin': end
        }

        #Set resource id on params
        params = {
            'p_p_id': self.hash,
            'p_p_resource_id': resource,
            'p_p_col_pos': 1,
            'p_p_lifecycle': 2,
            'p_p_col_count': 3,
            'p_p_state': 'normal',
            'p_p_mode': 'view',
            'p_p_cacheability': 'cacheLevelPage',
            'p_p_col_id': 'column-1'
        }

        req = self.session.post(self.API_URI, allow_redirects=False, data=datas, params=params)

        #While we don't have response we flood :)
        while req.status_code >= 300 and req.status_code < 400:
            req = self.session.post(self.API_URI, allow_redirects=False, data=datas, params=params)
        #Return date in json
        return req.json()