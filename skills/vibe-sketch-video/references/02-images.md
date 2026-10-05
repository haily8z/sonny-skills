# Bước 2 — Tạo bộ ảnh doodle theo thứ tự #1..#n

Đầu vào: `PROMPTS.md` đã duyệt (hoặc vừa ghi, ở chế độ chạy luôn). Đầu ra: `images/s01-<slug>.png` … `images/sNN-<slug>.png`.

## Lệnh tạo ảnh

```bash
/opt/hatch/bin/media-generation --media-subagent-output-type image \
  --orientation <vertical | landscape> \
  --output-dir <project>/images \
  "<prompt EN đầy đủ của cảnh #k>"
```

- `--orientation`: `vertical` khi khoá 9:16, `landscape` khi khoá 16:9. Không để mặc định.
- Từ ảnh #2 trở đi, nếu có nhân vật lặp lại hoặc muốn khoá nét vẽ: thêm `--image-file <project>/images/s01-*.png` (cover) làm ref phong cách. Ref cover có chữ → thêm vào prompt: `Use the reference only for drawing style and palette; do not copy its text.`
- Đổi tên file ra ngay sau khi tạo: `s03-hook-alarm.png`.
- Không có công cụ tạo ảnh: in prompt sẵn-copy từng cái và hướng dẫn user dán vào công cụ ngoài, rồi lưu về đúng tên file.

## Kiểm tra từng ảnh (cả hai chế độ)

1. **Tỷ lệ:** `ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 <ảnh>` → 9:16 hoặc 16:9 đúng khoá. Sai → tạo lại.
2. **Chữ:**
   - Overlay **có** → chạy checklist "Kiểm tra chữ" trong `00-prompt-locks.md`. Sai chữ/sai dấu/thiếu chữ → quy trình sửa 2 lần, rồi phương án dự phòng chèn chữ bằng `scripts/text_overlay.py`. **Không bao giờ để ảnh thiếu chữ hoặc sai chữ đi tiếp.**
   - Overlay **không** → không có chữ lạc nào.
3. **Nội dung:** đúng ý cảnh, một tiêu điểm rõ, nét vẽ cùng phong cách với cover.

## Chế độ duyệt (Checkpoint C2)

Tạo theo **lô 4 ảnh** theo thứ tự (ảnh chưa làm có số nhỏ nhất đi trước), kiểm tra xong mới trình bày.

**Hiện từng ảnh** (inline / đính kèm; không hiển thị được thì in đường dẫn tuyệt đối), mỗi ảnh một khối:
```
#6 · body · images/s06-coffee-cups.png
Chữ overlay: "Ngủ trước 23 giờ" ✓ khớp      (hoặc ⚠ chèn bằng script)
```
Cuối lô:

> *Đã tạo **#5–#8 / 12**.*
> *Gõ **`tiếp`** để tạo #9–#12 · **`lại #6`** để vẽ lại #6 · **`sửa #7: …`** để đổi ý cảnh/chữ của #7 rồi vẽ lại.*

`sửa #k: …` có đổi chữ overlay → cập nhật đồng thời `PLAN.md`, `PROMPTS.md` để chuỗi luôn khớp.

Khi đủ #n:
> *Đã đủ **n/n** ảnh. Gõ **`ok`** để sang làm giọng đọc (VO).*

## Chế độ chạy luôn

Tạo #1 → #n liền một mạch, mỗi ảnh vẫn qua đủ 3 bước kiểm tra và tự sửa trong giới hạn. Có thể chạy song song nhiều ảnh nếu không dùng cover làm ref. Ghi lại ảnh nào đã làm lại hoặc dùng chữ chèn ffmpeg để báo cáo cuối.

## Checklist trước khi sang VO
- [ ] Đủ s01..sNN, đúng thứ tự, tên file có nghĩa
- [ ] Tất cả đúng tỷ lệ khoá
- [ ] Overlay có: mọi ảnh có chữ đúng từng ký tự với `PLAN.md`
- [ ] Overlay không: không ảnh nào có chữ
- [ ] Phong cách đồng nhất với cover
