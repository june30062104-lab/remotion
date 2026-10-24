# Những lựa chọn nhỏ — video mẫu

Bản mẫu 62,3 giây · 1920×1080 · 30 fps · H.264.

- [Tải video MP4](./sample-silent.mp4?raw=true)
- [Tải mã nguồn Remotion ZIP](./source.zip?raw=true)
- [Xem bảng cảnh](./storyboard.jpg)
- [Phụ đề SRT](./sample.srt)

**Video hiện chưa có âm thanh.** MP3 đầu vào vượt giới hạn tải 32 MiB của công cụ. Hình và phụ đề được dựng theo SRT từ 00:00 đến 01:02,3, chưa xác minh đồng bộ với giọng gốc. Cần ghép đoạn giọng gốc tương ứng để hoàn tất.

Minh họa vector người que, 12 cảnh. Các nhân vật là hình giản lược, không phải chân dung chính xác. Nội dung theo SRT cung cấp, chưa kiểm chứng dữ kiện độc lập.

Giải nén source.zip, chạy `npm ci`, sau đó `npm run dev -- src/index.tsx`. Đọc README trong ZIP để ghép giọng và render; lệnh render dùng Chromium tại `/usr/bin/chromium`.
