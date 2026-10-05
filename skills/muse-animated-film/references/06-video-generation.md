# Bước 6 — Generate video từng cảnh

## Mục đích
Biến mỗi mega prompt thành một clip, rồi kiểm tra chất lượng trước khi dựng.

## Chế độ duyệt — first frame → last frame bằng keyframe
```bash
/opt/hatch/bin/media-generation --media-subagent-output-type video \
  --orientation <landscape | vertical> \
  --image-file <character-sheet-1.webp> \
  --image-file <character-sheet-2.webp> \
  --image-file <K-first-frame.webp> \
  --last-frame-image <K-last-frame.webp> \
  --output-dir <project>/videos \
  --timeout-secs 600 \
  "<mega prompt của cảnh>"
```
Các cảnh độc lập có thể chạy song song (mỗi cảnh một lệnh).

Trình bày từng clip (Checkpoint C4):
> *Xong cảnh **3/8**. Gõ **`ok`** để sang cảnh 4 · **`lại`** để generate lại · **`sửa: …`** để chỉnh prompt rồi generate lại.*

## Chế độ chạy luôn — không keyframe, nối bằng frame cuối
Chạy **tuần tự** cảnh 1 → N:

1. Cảnh 1: chỉ nạp character sheet, FIRST FRAME mô tả bằng chữ.
   ```bash
   /opt/hatch/bin/media-generation --media-subagent-output-type video \
     --orientation <landscape | vertical> \
     --image-file <character-sheet.webp> \
     --output-dir <project>/videos --timeout-secs 600 "<mega prompt cảnh 1>"
   ```
2. Trích frame cuối của clip vừa tạo:
   ```bash
   ffmpeg -y -sseof -0.1 -i videos/scene1.mp4 -frames:v 1 -update 1 frames/scene1-last.png
   ```
3. Cảnh N+1: nạp character sheet **trước**, rồi `--image-file frames/sceneN-last.png` làm first frame.
4. Lặp đến hết. Không chạy song song (cảnh sau phụ thuộc cảnh trước).

## Verify từng clip (bắt buộc, cả hai chế độ)
1. **Kỹ thuật:** `ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,duration -of default=noprint_wrappers=1 <file>` → đúng tỷ lệ khoá, ~10s.
2. **On-model:** xem frame đầu/giữa/cuối so với character sheet. Lệch → generate lại (giữ prompt hoặc siết character lock).
3. **Continuity:** frame cuối clip N đặt cạnh frame đầu clip N+1 phải gần như trùng.
4. **Chữ:**
   - Cảnh có `ON-SCREEN TEXT`: trích 3 frame trong khoảng chữ hiển thị, kiểm từng ký tự theo checklist ở `00-prompt-locks.md`. Sai sau 2 lần → generate lại cảnh với NO-TEXT LOCK và ghi chú cảnh này để **chèn chữ bằng ffmpeg drawtext ở khâu dựng** (`07-assembly.md`).
   - Cảnh không có chữ: không có chữ lạc.
5. **Âm thanh gốc:** `ffprobe -show_streams` xem có audio stream không — ghi lại cho `07-assembly.md`.

## Mẹo
- Đừng sửa một clip quá 2–3 lần; vẫn lệch → quay lại sửa mega prompt (MOTION mơ hồ hoặc thiếu character lock).
- Đặt tên lại ngay: `scene3-storm.mp4`.
