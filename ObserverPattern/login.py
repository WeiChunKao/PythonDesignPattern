import time
from abc import ABCMeta, abstractmethod
from observer import Observer, Observalbe


class Account(Observalbe):
    def __init__(self):
        super().__init__()
        self._lastIP = {}
        self._lastRegion = {}

    def login(self, name, ip, time):
        region = self._getRegion(ip)
        if self._isLongDistance(name, region):
            self.notifyObserver({
                "name": name,
                "ip": ip,
                "region": region,
                "time": time
            })
        self._lastRegion = region
        self._lastIP = ip

    def _getRegion(self, ip):
        ipRegion = {
            "127.0.0.1": "localHost",
            "0.0.0.0": "localHost iPv4"
        }
        region = ipRegion.get(ip)
        return "" if region is None else region

    def _isLongDistance(self, name, region):
        return self._lastRegion is not None and self._lastRegion != region


class SmsSender(Observer):
    def update(self, observalbe, object):
        print(f"[Message]: {object['name']} Abnormal Situation Region:{object['region']} IP:{object['ip']} Time:{ time.strftime('%Y-%m-%d, %H:%M:%S',time.gmtime(object['time']))}")

class MailSender(Observer):
    def update(self, observalbe, object):
        print(f"[Mail]: {object['name']} Abnormal Situation Region:{object['region']} IP:{object['ip']} Time:{ time.strftime('%Y-%m-%d, %H:%M:%S',time.gmtime(object['time']))}")

if __name__ == '__main__':
    account = Account()
    account.addObserver(SmsSender())
    account.addObserver(MailSender())
    account.login("Awei","127.0.0.1",time.time())
    account.login("John","0.0.0.0",time.time())