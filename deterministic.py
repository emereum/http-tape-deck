import re
import hashlib
import base64
import time
import os

file_path = os.path.dirname(os.path.realpath(__file__))

class Deterministic:
    def load(self, loader):
        with open(file_path + '/deterministic.js', 'r') as file:
            self.js = file.read().replace('`WPR_TIME_SEED_TIMESTAMP`', str(int(time.time()*1000)))
            sha256 = hashlib.sha256()
            sha256.update(self.js.encode('utf-8'))
            self.js_csp = '; script-src \'sha256-' + base64.b64encode(sha256.digest()).decode('utf-8') + '\''

    def response(self, flow):
        response = flow.response
        if not response:
            return
        if not response.content:
            return
        if 'text/html' not in response.headers.get('content-type'):
            return
        if b'<head' not in response.content:
            return
        
        headers = flow.response.headers
        for csp_header in ['content-security-policy', 'content-security-policy-report-only']:
            if not headers.get(csp_header):
                continue
            headers[csp_header] = re.sub(
                '(;\s*)?script-src|$',
                self.js_csp,
                headers[csp_header],
                1
            )
        
        script = '<script type="text/javascript">' + self.js + '</script>'
        response.content = re.sub(
            b'<head[^>]*>',
            lambda match: match.group(0) + script.encode('utf-8'),
            response.content
        )

addons = [Deterministic()]
