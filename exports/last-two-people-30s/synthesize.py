"""Synthesize the user-authorized Vietnamese script on the GitHub runner."""
import asyncio,json,pathlib,subprocess,wave,zipfile,urllib.request,sys
root=pathlib.Path(__file__).resolve().parent
out=root/'voice-assets';out.mkdir(exist_ok=True)
lines=json.loads((root/'lines.json').read_text())
async def edge_all():
 import edge_tts
 for i,line in enumerate(lines):
  voice='vi-VN-HoaiMyNeural' if line['speaker']=='a' else 'vi-VN-NamMinhNeural'
  boundaries=[]
  comm=edge_tts.Communicate(line['text'],voice,rate='+18%',pitch='+12Hz',boundary='WordBoundary',connect_timeout=10,receive_timeout=20)
  with (out/f'{i:02d}.mp3').open('wb') as f:
   async for chunk in comm.stream():
    if chunk['type']=='audio':f.write(chunk['data'])
    elif chunk['type']=='WordBoundary':boundaries.append({'word':chunk['text'],'start':chunk['offset']/1e7,'end':(chunk['offset']+chunk['duration'])/1e7})
  (out/f'{i:02d}.words.json').write_text(json.dumps(boundaries,ensure_ascii=False))
  print('Synthesized',i,flush=True)
try:
 asyncio.run(asyncio.wait_for(edge_all(),timeout=150));engine='Microsoft Edge TTS';timing='word boundaries from TTS'
except Exception as e:
 print('Edge unavailable:',type(e).__name__,flush=True)
 subprocess.run([sys.executable,'-m','pip','install','piper-tts==1.4.1'],check=True)
 from piper import PiperVoice,SynthesisConfig
 model=root/'vi_VN-vais1000-medium.onnx'
 for ext in ['', '.json']:
  urllib.request.urlretrieve('https://huggingface.co/rhasspy/piper-voices/resolve/main/vi/vi_VN/vais1000/medium/vi_VN-vais1000-medium.onnx'+ext,str(model)+ext)
 v=PiperVoice.load(str(model))
 for i,line in enumerate(lines):
  with wave.open(str(out/f'{i:02d}.wav'),'wb') as f:v.synthesize_wav(line['text'],f,syn_config=SynthesisConfig(length_scale=1.05))
  subprocess.run(['ffmpeg','-y','-v','error','-i',str(out/f'{i:02d}.wav'),str(out/f'{i:02d}.mp3')],check=True)
  (out/f'{i:02d}.words.json').write_text('[]')
 engine='Piper vi_VN-vais1000-medium';timing='word estimates needed'
(out/'provenance.json').write_text(json.dumps({'engine':engine,'timing':timing,'language':'vi','lines':len(lines)},indent=2))
with zipfile.ZipFile(root/'last-two-people-30s-voice.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(out.iterdir()):
  if p.suffix in {'.mp3','.json'}:z.write(p,p.name)
print('Voice package ready',flush=True)
