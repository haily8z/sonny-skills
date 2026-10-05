# Bước 3 — Giọng đọc, clip Ken Burns, dựng video hoàn chỉnh

Đầu vào: ảnh `images/s01..sNN` đã kiểm, `VO_SCRIPT.md`. Đầu ra: MP4 cuối + `subtitles.srt`.

## Bước 1 — Thu VO từng cảnh (Checkpoint C3)

Thu **từng cảnh một file** để thời lượng cảnh bám theo lời đọc:

```bash
/opt/hatch/bin/tts speak --voice <voice-id> --language <vi|en|…> \
  --output <project>/audio/vo_s03.mp3 --text-stdin <<< "<voiceText của s03>"
```

- Chọn giọng trong `/opt/hatch/skills/voice-selector/voice_source.json`: giọng bản xứ của ngôn ngữ đã khoá, ấm, tự nhiên, kể chuyện. Giọng tiếng Anh đọc tiếng Việt thường không chuẩn.
- Truyền text qua `--text-stdin`, không nhét vào argument.
- Đo thời lượng: `ffprobe -v error -show_entries format=duration -of csv=p=0 audio/vo_s03.mp3`.
- Không có TTS / user muốn tự thu: đưa `VO_SCRIPT.md` + spec WAV 48kHz, mỗi cảnh một file `vo_sNN.wav`.

Chế độ duyệt: **gửi 2–3 file audio đầu** (đính kèm / phát được, kèm tên giọng và thời lượng) để user duyệt giọng + nhịp trước khi thu hết. Sau khi đủ, hiện danh sách tất cả file `audio/vo_sNN.mp3` kèm thời lượng và lời đọc tương ứng:
> *Đã thu đủ VO **n/n** cảnh (tổng XX giây). Gõ **`ok`** để dựng các clip.*

## Bước 2 — Tạo clip Ken Burns từng cảnh (Checkpoint C4)

Thời lượng clip cảnh k: `D_k = thời lượng vo_sk + 0.6` giây (cover không có lời: 2,5 giây).

Kích thước output: 9:16 → `1080x1920`; 16:9 → `1920x1080`. 30fps.

```bash
# Ví dụ 9:16, zoom-in chậm. D = 5.4s → frames = 162
ffmpeg -y -loop 1 -i images/s03-hook-alarm.png -i audio/vo_s03.mp3 \
  -filter_complex "[0:v]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,\
zoompan=z='min(zoom+0.0007,1.10)':d=162:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30,\
format=yuv420p[v];[1:a]apad,aresample=48000[a]" \
  -map "[v]" -map "[a]" -t 5.4 -c:v libx264 -preset medium -crf 18 -c:a aac -ar 48000 -ac 2 \
  clips/s03.mp4
```

- `kenBurns: out` → `z='if(eq(on,0),1.10,max(zoom-0.0007,1.0))'`. `pan-left/right` → giữ `z=1.08`, cho `x` chạy theo `on`.
- Cảnh không có VO (cover): thay input audio bằng `-f lavfi -i anullsrc=r=48000:cl=stereo`.
- **Zoom tối đa 1.10** khi có chữ overlay, và zoom vào tâm, để chữ ở vùng an toàn không bị cắt.
- Mọi clip cùng kích thước, fps, codec, audio 48kHz stereo → nối được bằng `-c copy`.

Chế độ duyệt: nối nhanh các clip thành **bản dựng thô** `rough_cut.mp4` (không nhạc), **gửi file video** cho user xem cùng bảng `clip · thời lượng · lời đọc`:
> *Bản dựng thô **n cảnh, XX giây**. Gõ **`ok`** để render bản cuối · **`lại s05`** để làm lại clip/ảnh cảnh 5 · **`đổi nhịp s07: …`**.*

## Bước 3 — Render bản hoàn chỉnh (Checkpoint C5)

```bash
# list.txt: file 'clips/s01.mp4' … theo thứ tự
ffmpeg -y -f concat -safe 0 -i list.txt -c copy joined.mp4
```

Nhạc nền (tuỳ chọn, user cung cấp hoặc đồng ý): duck dưới VO.
```bash
ffmpeg -y -i joined.mp4 -stream_loop -1 -i music.mp3 \
  -filter_complex "[1:a]volume=0.12[m];[0:a][m]amix=inputs=2:duration=first:normalize=0[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -ar 48000 final.mp4
```
Không có nhạc: `cp joined.mp4 final.mp4`.

### Phụ đề
- Luôn xuất `subtitles.srt` từ `voiceText` + mốc thời gian cộng dồn của các clip.
- **Overlay có:** không burn phụ đề mặc định (chữ trên ảnh + phụ đề sẽ chồng chéo). Chỉ burn khi user yêu cầu, đặt ở 1/4 dưới, tránh vùng chữ overlay.
- **Overlay không:** hỏi một câu khi giao: *"Có muốn burn phụ đề vào video không?"* Có thì:
  ```bash
  ffmpeg -y -i final.mp4 -vf "subtitles=subtitles.srt:force_style='FontName=Be Vietnam Pro,FontSize=14,Outline=2,MarginV=60'" \
    -c:a copy final_sub.mp4
  ```
  Lỗi `No such filter: 'subtitles'` (ffmpeg thiếu libass) → không burn, giao `subtitles.srt` riêng và báo user (đa số nền tảng cho upload phụ đề rời).

### Verify file cuối
```bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate -of default=nw=1 final.mp4
ffprobe -v error -show_entries stream=codec_type -of csv=p=0 final.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 final.mp4
```
- [ ] Đúng 1080×1920 (hoặc 1920×1080), 30fps
- [ ] Có cả video và audio stream
- [ ] Thời lượng ≈ thời lượng mục tiêu (lệch ≤ 15%)
- [ ] Xem lướt đầu–giữa–cuối: chữ overlay không bị zoom cắt, VO khớp ảnh

Giao: đường dẫn `final.mp4`, `subtitles.srt`, `VO_SCRIPT.md` (lời liền mạch), thông số ffprobe. Chế độ chạy luôn: kèm báo cáo các mục đã tự làm lại / dùng phương án dự phòng.
