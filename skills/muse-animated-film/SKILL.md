---
name: muse-animated-film
description: "Làm PHIM HOẠT HÌNH ngắn trên Muse AI từ ý tưởng đến MP4: story bible, mega prompt từng cảnh, character sheet khoá nhân vật, keyframes match-cut, generate video từng cảnh, VO kể chuyện, dựng ffmpeg. Luôn hỏi trước: chủ đề, ngôn ngữ, tỷ lệ 16:9/9:16, thời lượng (→ số cảnh), chế độ chạy (duyệt từng phần / chạy luôn), có text overlay hay không. Prompt tiếng Anh, lời thoại/VO/chữ trên hình lồng nguyên văn theo ngôn ngữ đã chọn. Dùng khi user nói: phim hoạt hình, phim ngắn, animated short, hoạt hình 2D/3D, Disney/Pixar, anime, phim có nhân vật, kể chuyện bằng phim. Không dùng cho video doodle / người que (dùng vibe-sketch-video). Tác giả: Đặng Hữu Sơn."
---

# Muse Animated Film — phim hoạt hình ngắn

Pipeline đã kiểm chứng qua dự án thật "The Last Lantern" (8 cảnh, 2D Disney/Pixar, nhân vật on-model, match-cut liền mạch).

## File đọc theo bước

Các file `references/` đánh số **theo đúng thứ tự thực thi**. Chỉ đọc file của bước đang làm.

| Lúc | Đọc |
|---|---|
| Trước khi bắt đầu dự án | `references/08-lessons.md` — 12 bài học xương máu |
| Trước khi viết prompt đầu tiên | `references/00-prompt-locks.md` — khối ràng buộc EN (tỷ lệ, ngôn ngữ, text overlay, no-text) |
| Viết logline, VO, thoại, chữ trên hình | `references/anti-ai-writing.md` |
| 1 → 7 | `01-story-and-script` → `02-mega-prompts` → `03-character-sheets` → `04-keyframes` (chỉ chế độ duyệt) → `05-vo-production` → `06-video-generation` → `07-assembly` |

---

## BƯỚC 0 — HỎI TRƯỚC (bắt buộc)

Chưa viết, chưa generate gì cho đến khi đủ đáp án. Hỏi **gộp một tin nhắn**, chỉ câu còn thiếu.

> Trước khi bắt đầu, mình cần chốt vài thứ:
> 1. **Chủ đề / ý tưởng** phim là gì?
> 2. **Ngôn ngữ** lời thoại, VO, chữ trên hình: tiếng Việt / English / khác? *(mặc định: tiếng Việt)*
> 3. **Tỷ lệ**: 16:9 ngang hay 9:16 dọc? *(bắt buộc chọn — quyết định toàn bộ ảnh tham chiếu)*
> 4. **Thời lượng** mong muốn (giây)? *(mỗi cảnh ~10 giây → số cảnh = làm tròn lên thời lượng ÷ 10)*
> 5. **Chế độ chạy**:
>    (1) **Duyệt từng phần** — kịch bản + lời thoại + bộ prompt → bộ ảnh (character sheet, keyframe) → giọng đọc → từng video → phim cuối, mỗi bước chờ bạn "ok".
>    (2) **Chạy luôn** — không dừng hỏi, không làm bộ ảnh xem trước, làm thẳng đến phim cuối.
>    *(mặc định: 1)*
> 6. **Chữ trên hình (text overlay)**: Có / Không? *(mặc định: Không)*

Gọi nhanh: `CHỦ ĐỀ: … | NGÔN NGỮ: vi | TỶ LỆ: 16:9 | THỜI LƯỢNG: 80s | CHẾ ĐỘ: duyệt | OVERLAY: không`

Ví dụ số cảnh: 60s → 6 cảnh; 80s → 8 cảnh; 45s → 5 cảnh (cắt gọn ở khâu dựng). Chốt số cảnh với user ngay tại đây.

Ghi khối **PROJECT LOCK** lên đầu `STORY.md`:
```
PROJECT LOCK
topic: …
language: vi | en | …
aspect: 16:9 | 9:16
duration: 80s → scenes: 8
run_mode: review | auto
text_overlay: yes | no
```

---

## Ngôn ngữ và text overlay

- **Prompt ảnh/video luôn tiếng Anh.** Thoại, VO, chữ trên hình viết bằng **ngôn ngữ đã khoá**, nguyên văn trong ngoặc kép, kèm LANGUAGE LOCK. Không để model tự dịch.
- **`text_overlay: yes`** → ảnh cover có tên phim; cảnh có chữ ghi `ON-SCREEN TEXT` trong mega prompt với chuỗi chính xác. Chữ sai → sửa theo `00-prompt-locks.md`, cuối cùng chèn bằng `scripts/text_overlay.py` khi dựng. Phim giao đi luôn có chữ đúng ở các cảnh đã định.
- **Character sheet và keyframe luôn không chữ** (kể cả overlay = có): chữ trên ảnh tham chiếu sẽ méo khi thành video.
- Khi trình bày cho user duyệt: mỗi prompt EN kèm 2–3 dòng tóm tắt bằng ngôn ngữ user.

---

## Chế độ (1) — Duyệt từng phần

Mỗi checkpoint **hiện nội dung thật** trong chat, không chỉ báo "đã xong".

| Checkpoint | Phải hiện ra cho user | Lệnh user |
|---|---|---|
| **C1. Kịch bản + lời + prompt** | `STORY.md` đầy đủ (logline, character lock, từng cảnh: beat, first/last frame, thoại, VO, chữ); **toàn bộ mega prompt** từng cảnh nguyên văn + tóm tắt tiếng Việt; `VO_SCRIPT.md` bản chữ | `ok` · `sửa cảnh 3: …` |
| **C2. Bộ ảnh** | **Từng ảnh hiển thị**: character sheets → keyframes K1..K(N+1) → cover (nếu có), kèm đường dẫn và mô tả một dòng | `ok` · `lại K4` · `sửa K6: …` |
| **C3. Giọng đọc** | **File audio từng cảnh** (đính kèm / phát được) + thời lượng + lời | `ok` · `đổi giọng` · `thu lại cảnh 4` |
| **C4. Từng video** | **Từng clip** cảnh 1 → N, gửi file video + thông số ffprobe | `ok` · `lại` · `sửa: …` |
| **C5. Phim cuối** | **File MP4** + thông số ffprobe | giao |

Môi trường không hiển thị được ảnh/audio/video → in đường dẫn tuyệt đối từng file, một file một dòng.

## Chế độ (2) — Chạy luôn

- Không dừng. **Bỏ bước keyframes** (`04-keyframes.md`). Chỉ tạo character sheet (khoá nhân vật bắt buộc, một ảnh/nhân vật).
- Nối cảnh: trích frame cuối clip N làm first frame clip N+1, chạy tuần tự (`06-video-generation.md`).
- Vẫn tự kiểm tra đủ (tỷ lệ, on-model, continuity, chữ, audio stream) và tự làm lại trong giới hạn.
- Giao: MP4 + báo cáo ngắn (số cảnh, thời lượng, cảnh nào làm lại, cảnh nào chữ chèn bằng script) + đường dẫn các file trung gian.

---

## Output

- `STORY.md` (có PROJECT LOCK) · `MEGA_PROMPTS.md` · `VO_SCRIPT.md`
- `character_sheets/` · `keyframes/` (chế độ duyệt) · `cover.webp` (overlay có)
- `audio/` · `videos/`
- MP4 cuối: đúng tỷ lệ khoá (16:9 → 1280×720; 9:16 → 720×1280), 24fps, có audio, thời lượng ≈ yêu cầu, đã verify ffprobe.

## Luật vận hành

1. Bước 0 bắt buộc. Thiếu tỷ lệ, ngôn ngữ, thời lượng, chế độ hoặc lựa chọn overlay thì không bắt đầu.
2. **STRICT ASPECT RATIO LOCK** trong mọi prompt; mọi ảnh tham chiếu cùng tỷ lệ output. Sai tỷ lệ = làm lại.
3. **Khoá nhân vật:** character sheet luôn nạp **đầu tiên** trong mọi lệnh generate.
4. **Continuity:** frame cuối cảnh N = frame đầu cảnh N+1.
5. **Realism:** mọi hành động vật lý trong MOTION phải đúng cơ chế thực tế (mở cửa kính trước khi châm bấc, không "đốt xuyên qua kính").
6. **VO kể chuyện**, 1–2 câu/cảnh ở đầu cảnh, phủ ~50–60% thời lượng; qua `anti-ai-writing.md`.
7. Kiểm tra audio gốc bằng ffprobe trước khi mix; normalize trước khi nối.
8. Không làm lại một asset quá 3 lần; vẫn lỗi → sửa prompt gốc.
9. Mọi con số (số cảnh, thời lượng, độ phân giải) lấy từ output tool hoặc tính toán ở Bước 0, không đoán.
10. Cuối dự án hỏi: *"Muốn mình viết caption để đăng phim không?"* — có thì dùng `facebook-content-viral` hoặc `content-ads`.

## Công cụ trên Muse

- Ảnh/video: `/opt/hatch/bin/media-generation` (`--orientation landscape` cho 16:9, `vertical` cho 9:16).
- Giọng: `/opt/hatch/bin/tts`, catalog `/opt/hatch/skills/voice-selector/voice_source.json`.
- Dựng: `ffmpeg` / `ffprobe`. Chèn chữ chuẩn dấu: `scripts/text_overlay.py` (Pillow).
