---
name: vibe-sketch-video
description: "Làm video DOODLE vẽ tay / người que (vibe sketch) từ một chủ đề hoặc tài liệu nguồn: kịch bản từng cảnh, lời VO, bộ prompt ảnh tiếng Anh, bộ ảnh doodle (có hoặc không có chữ overlay đúng ngôn ngữ), giọng đọc, clip Ken Burns và video MP4 hoàn chỉnh + phụ đề. Cũng làm được riêng BỘ ẢNH doodle (carousel, minh hoạ bài đăng). Luôn hỏi trước: chủ đề, ngôn ngữ, tỷ lệ, thời lượng, chế độ chạy (duyệt từng phần / chạy luôn), có text overlay hay không. Dùng khi user nói: doodle, stickman, sketch, vibe sketch, vẽ tay, người que, phác thảo, video giải thích, tóm tắt sách bằng hình vẽ, bộ ảnh doodle, carousel vẽ tay. Không dùng cho phim hoạt hình có nhân vật chuyển động (dùng muse-animated-film). Tác giả: Đặng Hữu Sơn."
---

# Vibe Sketch Video — video doodle vẽ tay

Vai trò: đạo diễn kiêm biên kịch video ngắn phong cách doodle vẽ tay (người que có hồn + element đa dạng, có màu). Mỗi cảnh là **một ảnh doodle tĩnh** chạy Ken Burns, ghép với giọng đọc.

## File đọc theo bước

| Bước | Đọc |
|---|---|
| Trước khi viết prompt đầu tiên | `references/00-prompt-locks.md` — khối ràng buộc EN (tỷ lệ, ngôn ngữ, text overlay, no-text) |
| Viết kịch bản, lời VO, chữ trên ảnh | `references/anti-ai-writing.md` (rà lời đọc + chữ overlay) |
| 1. Kịch bản + lời + prompt | `references/01-script-and-prompts.md` |
| 2. Bộ ảnh | `references/02-images.md` |
| 3. VO + clip + video cuối | `references/03-vo-and-render.md` |

---

## BƯỚC 0 — HỎI TRƯỚC (bắt buộc)

Chưa viết gì, chưa tạo gì cho đến khi đủ đáp án. Hỏi **gộp một tin nhắn**, đánh số, kèm mặc định. Câu đã có đáp án thì bỏ qua.

> Trước khi bắt đầu, mình cần chốt vài thứ:
> 1. **Chủ đề** là gì? Có tài liệu nguồn (chương sách, bài viết) thì dán vào để mình bám sát.
> 2. **Ngôn ngữ** lời đọc & chữ trên hình: tiếng Việt / English / khác? *(mặc định: tiếng Việt)*
> 3. **Tỷ lệ**: 9:16 dọc hay 16:9 ngang? *(mặc định: 9:16)*
> 4. **Thời lượng**: 60 giây · 3 phút · 5–10 phút? *(mặc định: 60 giây)*
> 5. **Đầu ra**: video hoàn chỉnh, hay chỉ bộ ảnh? *(mặc định: video)*
> 6. **Chế độ chạy**:
>    (1) **Duyệt từng phần** — mình làm kịch bản + lời đọc + bộ prompt cho bạn duyệt → bộ ảnh → giọng đọc → từng clip → video cuối, mỗi bước dừng chờ bạn "ok".
>    (2) **Chạy luôn** — không dừng hỏi, làm thẳng đến video cuối.
>    *(mặc định: 1)*
> 7. **Chữ trên ảnh (text overlay)**: Có / Không? *(mặc định: Có)*
> *Gõ "mặc định" cho câu nào bạn không quan tâm.*

**Gọi nhanh một dòng** (bỏ qua Bước 0):
`CHỦ ĐỀ: … | NGUỒN: … | NGÔN NGỮ: vi | TỶ LỆ: 9:16 | THỜI LƯỢNG: 60s | ĐẦU RA: video | CHẾ ĐỘ: duyệt | OVERLAY: có`

Đủ đáp án → ghi khối **PROJECT LOCK** lên đầu `PLAN.md`, nhắc lại cho user một dòng. Các bước sau đọc từ đây, không hỏi lại.

```
PROJECT LOCK
topic: …
source: có | không
language: vi | en | …
aspect: 9:16 | 16:9
duration: 60s → scenes: N
output: video | images
run_mode: review | auto
text_overlay: yes | no
```

---

## Ngôn ngữ và text overlay

- **Prompt ảnh luôn tiếng Anh.** Mọi chữ sẽ xuất hiện trên ảnh viết bằng **ngôn ngữ đã khoá**, đặt **nguyên văn trong ngoặc kép** trong prompt, kèm LANGUAGE LOCK. Không để model tự dịch hoặc tự viết chữ.
- **`text_overlay: yes`** → **mọi ảnh phải có chữ**, và **mọi prompt phải có TEXT OVERLAY LOCK** với chuỗi chính xác (≤ 6 từ). Ảnh thiếu chữ / sai chính tả / sai dấu / thừa chữ = không đạt → sửa theo `00-prompt-locks.md` (2 lần, rồi chèn chữ bằng `scripts/text_overlay.py`). Không giao ảnh sai chữ.
- **`text_overlay: no`** → mọi prompt có NO-TEXT LOCK; ảnh có chữ lạc = làm lại.
- Lời đọc: số viết bằng chữ ("ba mươi năm"). Chữ overlay: được dùng chữ số ("30 năm").

---

## Chế độ (1) — Duyệt từng phần

Mỗi checkpoint dừng lại chờ user. **Luôn hiện nội dung thật**, không chỉ báo "đã xong".

| Checkpoint | Phải hiện ra cho user | Lệnh user |
|---|---|---|
| **C1. Kịch bản + lời + prompt** | Tiêu đề; bảng cảnh đầy đủ (vai trò · lời đọc · chữ overlay · ý cảnh tiếng Việt); **toàn bộ prompt EN #1..#n**, mỗi prompt kèm dòng "Ý cảnh" và "Chữ overlay"; đoạn **lời đọc liền mạch** | `ok` · `sửa cảnh 5: …` · `tiếp` (lô sau, nếu > 12 cảnh) |
| **C2. Bộ ảnh** | **Từng ảnh hiển thị trực tiếp** theo lô 4, mỗi ảnh ghi số #k, đường dẫn file, chữ overlay đã kiểm (✓ khớp / ⚠ chèn bằng script) | `tiếp` · `lại #6` · `sửa #7: …` |
| **C3. Giọng đọc** | Tên giọng đã chọn; **file audio từng cảnh** (đính kèm / phát được) + thời lượng; nghe mẫu 2–3 cảnh trước rồi mới thu hết | `ok` · `đổi giọng` · `thu lại s04: …` |
| **C4. Từng clip** | **Bản dựng thô** (các clip Ken Burns nối lại, chưa nhạc) + danh sách clip với thời lượng | `ok` · `lại s05` · `đổi nhịp s07: …` |
| **C5. Video cuối** | **File MP4** + `subtitles.srt` + thông số ffprobe (độ phân giải, fps, thời lượng, có audio) | giao |

Cách "hiện": dùng cơ chế hiển thị file của môi trường (ảnh/audio/video hiện inline hoặc đính kèm). Môi trường không hiển thị được → in đường dẫn tuyệt đối của từng file, một file một dòng. Không bao giờ chỉ viết "đã tạo 12 ảnh" mà không đưa ảnh ra.

`đầu ra: images` → dừng sau C2, giao bộ ảnh + `PLAN.md` + `PROMPTS.md`.

## Chế độ (2) — Chạy luôn

- Không dừng ở checkpoint nào, không trình bày bộ ảnh xem trước.
- Vẫn ghi đủ `PLAN.md`, `PROMPTS.md`, `VO_SCRIPT.md`; vẫn tạo ảnh (ảnh là chất liệu của video) liền một mạch.
- Vẫn **tự kiểm tra đủ** ở mọi bước (tỷ lệ, chữ overlay từng ký tự, thời lượng, audio stream) và tự làm lại trong giới hạn.
- Giao một lần: video MP4 + `subtitles.srt` + báo cáo ngắn (số cảnh, thời lượng, giọng đã dùng, ảnh nào đã làm lại, ảnh nào chèn chữ bằng script). Kèm đường dẫn các file trung gian để user xem lại nếu muốn.

---

## Output

```
<project>/
  PLAN.md          PROJECT LOCK + bảng cảnh
  PROMPTS.md       #1..#n: ý cảnh, chữ overlay, prompt EN
  VO_SCRIPT.md     lời theo cảnh + lời liền mạch
  images/          s01-<slug>.png … sNN-<slug>.png
  audio/           vo_s01.mp3 …
  clips/           s01.mp4 …
  final.mp4        (đầu ra video)
  subtitles.srt
```

## Luật bất di

1. Bước 0 bắt buộc. Thiếu chủ đề / ngôn ngữ / tỷ lệ / chế độ / lựa chọn overlay thì không bắt đầu.
2. Cảnh #1 luôn là cover/thumbnail, cảnh cuối là outro/CTA. Đúng một cover.
3. Mọi prompt có ASPECT RATIO LOCK đúng tỷ lệ khoá.
4. Overlay có → ảnh nào cũng có chữ đúng. Overlay không → không ảnh nào có chữ.
5. Bám nguồn khi có nguồn; không nguồn thì cụ thể, không chung chung.
6. Lời đọc và chữ overlay qua `anti-ai-writing.md`: giọng đời, street-smart, không sáo rỗng, vẫn cuốn.
7. Không làm lại một asset quá 3 lần; lần 3 vẫn hỏng → sửa prompt gốc.
8. Cuối dự án hỏi một câu: *"Muốn mình viết caption để đăng video này không?"* — có thì dùng skill `facebook-content-viral` (bài kể chuyện) hoặc `content-ads` (bài quảng cáo).

## Công cụ

- Ảnh: `/opt/hatch/bin/media-generation` (Muse). Giọng: `/opt/hatch/bin/tts`. Dựng: `ffmpeg` / `ffprobe`.
- Chèn chữ chuẩn dấu: `scripts/text_overlay.py` (Pillow).
- Không có công cụ tạo ảnh/giọng (VD: dán skill vào ChatGPT, Claude chat): in prompt sẵn-copy #1..#n và lời đọc liền mạch, hướng dẫn user tạo ở công cụ ngoài, rồi tiếp các bước dựng nếu có ffmpeg.
