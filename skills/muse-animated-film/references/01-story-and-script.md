# Bước 1 — Thảo luận & chốt kịch bản (Story Bible)

## Mục đích
Biến ý tưởng của user thành một **Story Bible** duy nhất, chốt cứng mọi thứ trước khi vẽ. Đây là "hiến pháp" của phim — mọi prompt sau này đều trích từ đây.

## Đã có từ Bước 0 — không hỏi lại
Chủ đề, ngôn ngữ, tỷ lệ, thời lượng → số cảnh, chế độ chạy, text overlay. Chép nguyên khối PROJECT LOCK lên đầu `STORY.md`.

## Câu hỏi thảo luận (chỉ ở chế độ duyệt)
Hỏi ngắn, gộp những câu còn thiếu:
1. Nhân vật chính là ai? (tuổi, tính cách, ngoại hình)
2. Logline: ai + muốn gì + vật cản + cái giá
3. Thế giới ở đâu? Phong cách hình ảnh? (2D Disney/Pixar, anime, 3D…)
4. VO giọng người kể chuyện hay nhân vật tự thoại?
5. Nhạc có motif chủ đạo không? (VD: bài hát ru → full orchestra ở cao trào)
6. Đỉnh cảm xúc nằm ở cảnh nào?

Chế độ chạy luôn: tự quyết các mục trên từ chủ đề, chọn mặc định an toàn (2D Disney/Pixar, người kể chuyện ấm, đỉnh cảm xúc ở ~2/3 phim), ghi vào `STORY.md`, không hỏi.

## Template STORY.md
```markdown
<PROJECT LOCK>

# <TÊN PHIM> — Story Bible
*Phong cách · số cảnh · ngôn ngữ VO · tỷ lệ*

## Logline
<1 câu>

## Characters (CANONICAL LOCK — tiếng Anh, chép nguyên văn vào mọi prompt)
- **<TÊN> (tuổi, vai):** <ngoại hình chi tiết + tính cách + arc>

## World & Style Lock (tiếng Anh)
<Thế giới, phong cách hình ảnh, tỷ lệ + độ phân giải, âm thanh, nhạc>

## Continuity Rule
**Last frame of Scene N = first frame of Scene N+1 (match cut).**

### Scene N — "<Tên cảnh>"
- Beat: <cảm xúc chủ đạo>
- First frame: <mô tả>
- Last frame: <mô tả> (= first frame cảnh N+1)
- VO: "<câu VO bằng ngôn ngữ đã khoá>"
- Dialogue: "<thoại nhân vật, nếu có, ngôn ngữ đã khoá>"
- On-screen text: "<≤ 6 từ, ngôn ngữ đã khoá>"   ← chỉ khi text_overlay: yes
- Music: <diễn biến nhạc>
```

## Text overlay trong FILM
Khi `text_overlay: yes`, chọn cảnh nào có chữ (không bắt buộc mọi cảnh): thường là **title card cảnh 1**, mốc thời gian/địa điểm ("Mười năm sau"), và **cảnh kết**. Mỗi cảnh có chữ ghi `On-screen text` với chuỗi chính xác. Thêm một ảnh **cover/thumbnail** có chữ là tên phim.

## Quy tắc chốt
- **Characters** và **Style Lock** viết bằng tiếng Anh, đủ chi tiết để paste vào prompt không cần sửa.
- Mỗi cảnh bắt buộc có first frame + last frame mô tả rõ.
- VO mỗi cảnh 1–2 câu, ngôn ngữ đã khoá. Tiếng Việt: số viết bằng chữ. Logline, thoại, VO, chữ trên hình rà theo `anti-ai-writing.md`: giọng người kể, có hình ảnh cụ thể, không sáo rỗng.
- Chế độ duyệt: `STORY.md` thuộc Checkpoint C1, trình bày cùng `MEGA_PROMPTS.md` và `VO_SCRIPT.md` (nháp lời). User duyệt xong mới vẽ. Đổi kịch bản sau khi đã vẽ = làm lại mọi cảnh liên quan.
