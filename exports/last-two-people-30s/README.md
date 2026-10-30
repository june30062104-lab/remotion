# Nếu chỉ còn hai người — bản vui30giây

Dựng lại theo video1030(1).mp4 người dùng gửi làm tham chiếu: ánh sáng tím–vàng, khung hình có chiều sâu, macro tay,qua vai,top-down,tracking và nhân vật diễn hành động. Không có phụ đề hay title card;chỉ giữ chữ trong đồng hồ và tờ kế hoạch.

30giây,1920×1080,24fps,18cảnh. Nhạc tổng hợp vui124BPM,19SFX,voice nam/nữ Việt tạo mới với tốc độ+18%,pitch+12Hz, rồi tăng tốc1.04x. Kịch bản rút gọn được ghi trong projects/last-two-30s/input/lines.json.

## Dựng lại
Cần Node≥18,Python≥3.9,FFmpeg/ffprobe và Chromium.
```bash
npm ci
python -m venv .venv
.venv/bin/pip install -r requirements.txt
export CHROMIUM_PATH=/usr/bin/chromium
.venv/bin/python projects/last-two-30s/build_project.py
.venv/bin/python projects/last-two-30s/make_music.py
node render.mjs --project projects/last-two-30s --sheet --scale 0.4 --capture canvas
node render.mjs --project projects/last-two-30s --workers 3 --capture canvas --format jpeg --preset fast
.venv/bin/python audio/mix.py --project projects/last-two-30s
.venv/bin/python tools/validate_output.py projects/last-two-30s/out/Neu-chi-con-hai-nguoi-30s.mp4 --duration 30 --width 1920 --height 1080
```
Có thể cài Chromium bằng `npx playwright install chromium` rồi bỏ CHROMIUM_PATH. Voice và nhạc được đóng gói, không cần dịch vụ online để dựng lại. Sửa scene trong scenes/shots/action.js; sửa nhân vật trong scenes/cast.js. Không bật captions khi dựng lại vì người dùng đã yêu cầu bỏ.

Giữ ghi công © Thanh Hai Learn AI,bộ engine gốc v0.2.0 do người dùng cung cấp đã được chuyển cho Codex. Mã gốc không có giấy phép phân phối riêng. Khung hình vẽ bằng mã ở độ phân giải xuất; không dùng ảnh storyboard phóng to. Không sao chép khung hình từ video tham chiếu vào thành phẩm.

Kiểm tra hình bằng storyboard,preview diễn xuất và frame trích xuất;âm thanh kiểm tra bằng phép đo tín hiệu,chưa nghe kiểm tra độc lập toàn bộ.
