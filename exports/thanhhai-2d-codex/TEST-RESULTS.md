# Kết quả chạy thử — 2026-10-30

- Cài npm thành công: Playwright 1.56.0, Three.js 0.169.0 và ba bộ font.
- Dùng Chromium /usr/bin/chromium, FFmpeg, NumPy và SciPy có sẵn; không cài Whisper, không thử 4K.
- Render và kiểm tra bằng mắt contact sheet 14 cảnh upstream, gồm cảnh 3D.
- Bản thử mới: 10,4 giây, 1920×1080,24fps,H.264/AAC,3 cảnh người que có viền sáng, camera, chữ tiếng Việt, phụ đề, voice gốc, nhạc thuật toán và 3 SFX.
- Voice lấy nguyên đoạn đầu từ voice-1.mp3 người dùng đã cung cấp. Thời điểm từng từ ước lượng từ SRT. Không có đánh giá nghe độc lập.
- Render 250 khung hình trong khoảng 167 giây trên máy này; không phải cam kết tốc độ cho máy khác.
- ffprobe: có đủ video/audio, đúng kích thước và thời lượng 10,4 giây. Giải mã toàn file bằng ffmpeg -xerror thành công.
- Kiểm tra lỗi: thiếu cảnh, khoảng render sai, alignment dưới 90% đều bị chặn. Tra từ tiếng Việt có dấu đúng.
- Mã render cuối cùng được chạy thêm smoke test encoder và ảnh tĩnh. Python syntax hợp lệ.

Chưa kiểm tra thực tế: chuyển giọng Whisper, xuất4K, Windows/macOS và video dài. Bản này là port chạy được trong Codex, không phải plugin cài trực tiếp từ giao diện ChatGPT.
