# Bước 3 — Character Sheets (Khoá nhân vật)

## Mục đích
Tạo "chứng minh thư" hình ảnh cho từng nhân vật. Từ đây về sau, mọi ảnh/video đều phải nạp sheet này để nhân vật không bị lệch (on-model).

Giai đoạn này chạy ở **cả hai chế độ**: chế độ chạy luôn vẫn cần sheet vì đây là khoá nhân vật, chỉ khác là không dừng để duyệt.

## Tỷ lệ khung hình và chữ
- Sheet PHẢI vẽ đúng tỷ lệ đã khoá ở Bước 0. Sheet không chỉ là tham chiếu style/nhân vật, nó còn định hình trực tiếp output video.
- Sheet **luôn dùng NO-TEXT LOCK**, kể cả khi `text_overlay: yes`. Sheet là ảnh ref; chữ trên ref sẽ lọt vào video.
- Các khối lock lấy từ `00-prompt-locks.md`.

## Prompt mẫu (từng nhân vật)
```
Character reference sheet, soft 2D Disney/Pixar animation style, clean rounded shapes,
warm cinematic lighting.
<ASPECT RATIO LOCK>
Character: <MÔ TẢ CHI TIẾT bằng tiếng Anh: tuổi, giới tính, tóc, mắt, trang phục từng món,
màu sắc chính xác, phụ kiện, đặc điểm nhận dạng>
Show: front view, side view, back view, 3/4 view, plus 3 expression close-ups
(happy, sad, determined). Same outfit and colors in every view, consistent proportions.
Plain soft neutral background.
<NO-TEXT LOCK>
```

## Quy trình
1. Viết mô tả nhân vật thật cụ thể (màu áo, kiểu tóc, phụ kiện). Càng chi tiết càng khó lệch về sau.
   - Chế độ duyệt: đưa user mô tả (kèm bản dịch một dòng bằng ngôn ngữ user) để chốt trước khi vẽ.
   - Chế độ chạy luôn: tự chốt mô tả từ chủ đề, ghi vào `STORY.md`.
2. Generate:
   ```
   /opt/hatch/bin/media-generation --media-subagent-output-type image \
     --orientation <landscape | vertical> --output-dir <project>/character_sheets \
     "<prompt trên>"
   ```
3. Kiểm tra: đúng tỷ lệ (ffprobe), các góc đồng nhất trang phục/màu sắc, không có chữ. Chưa đạt → sửa prompt, vẽ lại.
4. Lưu tên rõ ràng: `milo-sheet-16x9.webp`, `lyra-sheet-9x16.webp`…

## Checklist
- [ ] Mỗi nhân vật chính có sheet riêng, đúng tỷ lệ khoá
- [ ] Mô tả nhân vật đã chốt (không đổi giữa chừng)
- [ ] Đủ góc nhìn + biểu cảm, nền trơn, không chữ
- [ ] Chế độ duyệt: user đã duyệt sheet (thuộc Checkpoint C2)
