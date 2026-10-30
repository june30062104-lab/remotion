# Nếu chỉ còn hai người — dự án Codex

Video 66 giây,1920×1080,24fps,23 cảnh,17 đoạn lời kể/thoại tiếng Việt. Phong cách người que điện ảnh từ Thanh Hai Learn AI 2D Studio v0.2.0; đã chuyển sang Codex. Giữ nguyên ghi công © Thanh Hai Learn AI. Mã gốc được người dùng cung cấp, không kèm giấy phép phân phối riêng.

## Dựng lại
Cần Node.js≥18,Python≥3.9,FFmpeg/ffprobe và Chromium.
```bash
npm ci
python -m venv .venv
.venv/bin/pip install -r requirements.txt
# Đặt đường dẫn Chromium đúng với máy, hoặc cài bằng Playwright.
export CHROMIUM_PATH=/usr/bin/chromium
.venv/bin/python projects/last-two-people/build_project.py
node render.mjs --project projects/last-two-people --sheet --scale 0.35 --capture canvas
node render.mjs --project projects/last-two-people --workers 3 --capture canvas --format jpeg --preset fast
.venv/bin/python audio/mix.py --project projects/last-two-people
.venv/bin/python tools/validate_output.py projects/last-two-people/out/Neu-chi-con-hai-nguoi.mp4 --duration 66 --width 1920 --height 1080
```
Voice đã được đóng gói; không cần tạo lại giọng hoặc tải Whisper. Nếu không có Chromium cài sẵn, dùng `npx playwright install chromium` rồi bỏ CHROMIUM_PATH.

## Chỉnh sửa
- `input/lines.json`: bản kịch bản tiếng Việt đã biên tập trong cuộc trò chuyện. Nếu đổi lời, phải tạo lại audio và mốc từ tương ứng.
- `input/voice-assets/`: 17 MP3 tạo bằng Microsoft Edge TTS, NamMinh cho narrator/nhân vật B và HoaiMy cho nhân vật A; mốc từ lấy từ dịch vụ TTS, không phải Whisper.
- `build_project.py`: nối voice, đặt khoảng nghỉ, tạo timeline, SRT và shot list.
- `scenes/cast.js`: hai nhân vật áo cam/tóc đuôi ngựa và áo xanh/tóc nhọn.
- `scenes/sets/world.js`: phòng ngủ, phố, ô tô và địa cầu minh họa.
- `scenes/shots/film.js`:23 cảnh, camera, biểu cảm, hoạt họa 2D và phố3D.
- `story/shots.json`: nhạc mystery/playful/tension,23SFX và8đoạn ambience nhẹ.

Các cảnh được vẽ từ mã ở độ phân giải xuất; không dùng contact sheet để phóng to hình. Bản dựng theo giả định hư cấu của kịch bản, không phải kiểm chứng khả năng tái lập dân số từ hai người.

## Kiểm tra
Đã xem contact sheet23cảnh và bản preview6giây. Kết quả kiểm tra file xuất nằm trong validation.json kèm bản giao. Chỉ ghi nhận chất lượng âm thanh bằng phép đo tín hiệu, không tuyên bố đã nghe kiểm tra độc lập toàn video.
