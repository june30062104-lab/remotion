# Thanh Hai 2D Studio — Codex edition

Chuyển từ plugin Thanh Hai Learn AI 2D Studio v0.2.0 do người dùng cung cấp. Giữ nguyên ghi công © Thanh Hai Learn AI. Gói gốc không kèm giấy phép sử dụng/phân phối rõ ràng; bản này không thêm quyền cấp phép cho mã gốc.

## Khởi động
```bash
npm ci
python -m venv .venv
.venv/bin/pip install -r requirements.txt
# Chọn Chromium có sẵn, hoặc: npx playwright install chromium
export CHROMIUM_PATH=/usr/bin/chromium
node render.mjs --project examples/reaction-time --sheet --scale 0.3
```
Chỉ cần requirements-whisper.txt khi muốn chép lời tự động. Khi đã có SRT, không cần tải Whisper.

Codex đọc AGENTS.md và .agents/skills/thanhhai-2d-video/SKILL.md. Mã dựng dùng Canvas/Three.js/FFmpeg, không cần Remotion hoặc Claude.

## Thay đổi
- Skill native cho Codex; bỏ slash command và yêu cầu hỏi lại ngôn ngữ đã biết.
- Server chỉ bind loopback; chặn đường dẫn vượt thư mục kể cả symlink.
- Cho chọn Chromium qua CHROMIUM_PATH; chờ server sẵn sàng trước khi render.
- Thiếu/lỗi cảnh và encoder lỗi làm render thất bại; chặn khoảng render rỗng.
- Chặn alignment dưới 90%, chặn slug thoát thư mục và ghi đè dự án.
- Công cụ kiểm tra MP4 qua ffprobe và giải mã đầy đủ.

Ví dụ upstream không kèm voice. Bản thử Codex dùng một đoạn voice tiếng Việt do người dùng đã cung cấp, với cảnh mới phù hợp nội dung; không ghép voice vào các cảnh upstream không liên quan.

Mức hỗ trợ 4K/Whisper là khả năng cấu hình; chỉ các trường hợp trong TEST-RESULTS.md được chạy thực tế.
