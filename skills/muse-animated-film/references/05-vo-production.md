# Bước 5 — Làm VO (thuyết minh)

Thứ tự trong chế độ duyệt: **lời VO đã được duyệt dạng chữ ở C1**, giai đoạn này thu thành âm thanh (C3) **trước** khi generate video. Chế độ chạy luôn: thu VO rồi đi tiếp không dừng.

## Triết lý
VO là **người kể chuyện**, không phải máy đọc. Mỗi cảnh 1–2 câu đặt ở **đầu cảnh**, rồi để khoảng lặng cho hình, tiếng động, nhạc. Tổng VO phủ ~50–60% thời lượng phim. Cảnh cao trào có thể **không cần VO**.

## Bước 1 — VO_SCRIPT.md
Mỗi cảnh:
- **Timecode:** cảnh N bắt đầu ở giây (N-1)×D. VO vào sau ~1 giây đầu cảnh, dứt trước khi hết cảnh ~2 giây.
- **Lời** bằng **ngôn ngữ đã khoá**. Tiếng Việt: số viết bằng chữ. Nếu user cần thêm bản dịch (VD: làm phụ đề song ngữ), thêm dòng thứ hai.
- **Direction:** ghi chú giọng ("trầm xuống cuối câu", "bật cười nhẹ").
- `...` = nghỉ một nhịp (~0,5 giây).

```markdown
## CẢNH N — "<Tên>" (start–end)
*VO vào lúc X, dứt trước Y.*
**<LANG>:** <câu VO>
*Direction: <chỉ dẫn giọng>*
```

## Bước 2 — Thu VO
**Option A: TTS**
```bash
/opt/hatch/bin/tts speak --voice <voice-id> --language <vi|en|…> \
  --output <project>/audio/vo_canhN.mp3 --text-stdin <<< "<câu VO>"
```
- Chọn giọng trong `/opt/hatch/skills/voice-selector/voice_source.json`: narrator ấm, **bản xứ của ngôn ngữ đã khoá**.
- Truyền text qua `--text-stdin`.
- `ffprobe -show_entries format=duration` — mỗi file VO phải ngắn hơn cảnh chứa nó.

**Option B: User thu ngoài** — đưa `VO_SCRIPT.md` + spec WAV 48kHz, không nhạc nền, 2–3 take/câu, kèm file TTS mẫu để tham khảo nhịp.

## Trình bày (Checkpoint C3, chế độ duyệt)
Gửi 2 file đầu để duyệt giọng trước, rồi thu hết:
> *Đã thu VO **8/8** cảnh. Gõ **`ok`** để generate video · **`đổi giọng`** · **`thu lại cảnh 4: …`**.*

## Checklist
- [ ] VO_SCRIPT.md đúng ngôn ngữ khoá, có timecode + direction
- [ ] Mỗi file VO ngắn hơn cảnh
- [ ] Đã nghe thử, không câu nào bị ngắt cụt
