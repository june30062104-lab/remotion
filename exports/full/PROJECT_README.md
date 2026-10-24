# Những lựa chọn nhỏ — bản đầy đủ

37 phút 20 giây · 1920×1080 · 30 fps · H.264 + AAC · phụ đề tiếng Việt và chương.

## Nội dung dự án
- 58 ảnh riêng, mỗi ảnh là một cảnh độc lập; không cắt ô từ contact sheet.
- 246 shot có mốc theo ý lời thoại, pan trái/phải, giữ khung, push-in/pull-out nhẹ.
- Chữ, phụ đề và nhãn giải thích là lớp riêng, không phụ thuộc chữ trong ảnh AI.
- 245 SFX tại điểm chuyển cảnh, gồm swish, lật trang, soft tick và chime đổi chương. Đây là SFX tổng hợp thủ tục, không dùng thư viện âm thanh bên ngoài.
- Voice ghép nối 1.MP3 và 2.MP3 theo thứ tự, không tăng tốc. SRT có 602 câu, trục thời gian gốc được giữ.

Ảnh nguồn được tạo bằng AI, phần lớn ở kích thước native khoảng 1672×941; kích thước thực của từng file nằm trong assets-manifest.json. Bản xuất là 1080p với mức phóng vừa phải và camera khoảng 1,5–5,5%; không gọi file ảnh nguồn là 4K hay native1080p. Hình là minh họa, không phải tư liệu quay hoặc chân dung hoàn toàn chính xác. Không mô phỏng khẩu hình/tay chân bằng ảnh phẳng.

## Mở trong Remotion
```
npm ci
npm run dev
```
Entry: src/index.tsx. Sửa shots.json để đổi thứ tự, timing, camera và asset; sửa src/captions.json cho phụ đề. src/callouts.json chứa các nhãn nhấn ý. Preview Remotion dùng cùng ảnh, timing và bản mix; FFmpeg renderer dùng libass để kiểm soát chữ và xuất toàn bộ video hiệu quả hơn.

## Xuất video
Cần Python3, numpy, FFmpeg có libx264 và libass. Ảnh, voice và SFX đều có sẵn trong public/.
```
python work/render_segments.py
python work/assemble.py
```
Có thể xuất bằng Remotion thuần bằng `npm run render:remotion` (cần Chromium ở /usr/bin/chromium hoặc chỉnh đường dẫn); bản bàn giao được xuất theo pipeline FFmpeg với cùng timeline, ảnh, camera và overlay, có khác biệt nhỏ giữa hai hệ hiển thị chữ.

Khi sửa một shot, xóa đúng MP4 tương ứng trong work/segments/ trước khi xuất lại; pipeline giữ lại các clip đã có để tiếp tục sau gián đoạn. Muốn dựng toàn bộ lại, dùng một thư mục work/segments/ mới. Không xóa asset gốc.

## Sửa âm thanh
Bản mix đã sẵn tại public/audio/full-mix.m4a. Đổi cường độ/envelope SFX trong work/make_sfx.py, sau đó chạy `python work/mix_audio.py` và assemble lại. File voice gốc đã được kèm theo. Không cần khóa API hoặc dịch vụ bên ngoài để chạy dự án đã đóng gói.

## Kiểm tra và giới hạn
Các khoảng ngắt được đối chiếu với SRT; công cụ không nghe/phiên âm kiểm chứng từng từ. Đo loudness/true peak, kiểm tra metadata, số frame của từng shot, khả năng giải mã toàn bộ và các khung mẫu. Không khẳng định đã nghe duyệt toàn bộ hoặc kiểm chứng độc lập các dữ kiện về người nổi tiếng trong kịch bản.

Bản mix trước mã hóa đo được khoảng -16,18 LUFS integrated, true peak -1,50 dBTP; SFX ngắn nằm dưới voice và không kéo dài timeline. Xem validation.json để biết kết quả cuối cùng.
