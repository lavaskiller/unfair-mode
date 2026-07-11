#!/usr/bin/env python3
"""Static server plus optional OpenAI-compatible DigitalOcean AI proxy.
Set DO_AI_ENDPOINT, DO_AI_API_KEY, and DO_AI_MODEL from the official event guide.
Without them, the UI transparently uses its labeled saved demo analysis.
"""
import json, os, urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

SYSTEM="""You are an accessibility repair engine. The user message contains measured browser DOM evidence. Return JSON only with: issues (title, severity, detail, evidence) and repair (minTargetPx from 44-64, contrastBoost from 1-2, spacingPx from 8-20, plainLanguage boolean). Ground every issue in supplied measurements and avoid compliance guarantees."""
class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != '/api/analyze': self.send_error(404); return
        length=int(self.headers.get('content-length','0')); payload=json.loads(self.rfile.read(length) or b'{}')
        endpoint=os.getenv('DO_AI_ENDPOINT'); key=os.getenv('DO_AI_API_KEY'); model=os.getenv('DO_AI_MODEL')
        if not all((endpoint,key,model)):
            self.send_error(503,'DigitalOcean AI environment variables are not configured'); return
        body=json.dumps({'model':model,'messages':[{'role':'system','content':SYSTEM},{'role':'user','content':json.dumps(payload)}],'temperature':0.2,'response_format':{'type':'json_object'}}).encode()
        req=urllib.request.Request(endpoint,data=body,headers={'Authorization':f'Bearer {key}','Content-Type':'application/json'})
        try:
            with urllib.request.urlopen(req,timeout=20) as r: raw=json.load(r)
            result=json.loads(raw['choices'][0]['message']['content']); result['source']='digitalocean-ai'
            out=json.dumps(result).encode(); self.send_response(200); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(out))); self.end_headers(); self.wfile.write(out)
        except Exception as exc: self.send_error(502,f'AI request failed: {exc}')

if __name__=='__main__':
    port=int(os.getenv('PORT','8000')); print(f'UNFAIR MODE running at http://localhost:{port}'); ThreadingHTTPServer(('0.0.0.0',port),Handler).serve_forever()
