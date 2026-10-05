# Bước 7 — Dựng phim bằng ffmpeg (Checkpoint C5)

## Mục đích
Nối các clip thành phim hoàn chỉnh, chèn chữ dự phòng (nếu có), mix VO đúng timecode, xuất file cuối đạt chuẩn.

Độ phân giải chuẩn theo tỷ lệ khoá: 16:9 → **1280×720**; 9:16 → **720×1280**. 24fps.

## Bước 1 — Kiểm tra audio gốc của clip
```bash
ffprobe -v error -show_entries stream=index,codec_type -of csv <clip.mp4>
```
- Có audio nền → **giữ**, duck dưới VO.
- Im lặng → thêm track câm khi normalize để mọi clip đều có audio (concat cần đồng nhất stream).

## Bước 2 — Normalize
```bash
# 16:9 (clip có audio)
ffmpeg -i <clip>.mp4 -vf "scale=1280:720,fps=24" \
  -c:v libx264 -pix_fmt yuv420p -c:a aac -ar 48000 -ac 2 <clip>_norm.mp4
# 9:16: đổi scale=720:1280
# Clip im lặng: thêm  -f lavfi -i anullsrc=r=48000:cl=stereo -shortest  và map 0:v + 1:a
```

## Bước 3 — Chèn chữ dự phòng (chỉ cảnh bị ghi chú ở bước 6)
Cách chính — lớp chữ trong suốt bằng script của skill, rồi overlay (không cần `drawtext`):
```bash
python3 <skill>/scripts/text_overlay.py --size <1280x720 | 720x1280> --out scene3_text.png \
  --text "<EXACT TEXT>" --zone bottom --style light
ffmpeg -y -i scene3_norm.mp4 -loop 1 -i scene3_text.png -filter_complex \
  "[1:v]format=rgba,fade=in:st=<start>:d=0.4:alpha=1,fade=out:st=<end-0.4>:d=0.4:alpha=1[t];\
[0:v][t]overlay=0:0:shortest=1:enable='between(t,<start>,<end>)'" \
  -c:a copy scene3_norm_text.mp4
```

Cách thay thế — ffmpeg có `drawtext` (`ffmpeg -filters | grep drawtext`):
```bash
printf '%s' "<EXACT TEXT>" > /tmp/scene3_text.txt
ffmpeg -y -i scene3_norm.mp4 -vf "drawtext=fontfile=<font hỗ trợ tiếng Việt>.ttf:\
textfile=/tmp/scene3_text.txt:fontsize=<44 cho 1280×720 | 48 cho 720×1280>:fontcolor=white:borderw=4:bordercolor=black@0.6:\
x=(w-text_w)/2:y=h*0.78:enable='between(t,<start>,<end>)':\
alpha='if(lt(t,<start>+0.4),(t-<start>)/0.4,if(gt(t,<end>-0.4),(<end>-t)/0.4,1))'" \
  -c:a copy scene3_norm_text.mp4
```
Font: `fc-list | grep -iE "be vietnam|noto sans|montserrat"`. Dùng `textfile=` để không phải escape dấu tiếng Việt.

## Bước 4 — Nối
```bash
# list.txt: file '<clip>_norm.mp4' theo thứ tự 1→N
ffmpeg -f concat -safe 0 -i list.txt -c copy joined.mp4
```
Frame trùng ở mối nối quá lâu → trim bằng `-ss`/`-t` trước khi nối.

## Bước 5 — Mix VO đúng timecode
Cảnh N (mỗi cảnh D giây) → offset = (N-1)×D + 1 giây:
```bash
ffmpeg -i joined.mp4 -i vo_canh1.mp3 -i vo_canh2.mp3 \
 -filter_complex "[1:a]adelay=1000|1000[a1];[2:a]adelay=11000|11000[a2]; \
 [0:a]volume=0.35[bg];[bg][a1][a2]amix=inputs=3:duration=first:normalize=0[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac final.mp4
```
`adelay` tính bằng mili-giây. `volume=0.35` = duck audio gốc dưới VO.

## Bước 6 — Verify file cuối
```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height,r_frame_rate -of default=noprint_wrappers=1 final.mp4
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 final.mp4
```
- [ ] Đúng độ phân giải của tỷ lệ khoá, 24fps
- [ ] Có cả video + audio stream
- [ ] Tổng thời lượng ≈ N×D
- [ ] Overlay có: chữ ở các cảnh đã định hiển thị đúng, đọc được
- [ ] Xem lại một lượt trước khi giao

Giao: `final.mp4` + thông số ffprobe (+ `cover.webp` nếu có). Chế độ chạy luôn: kèm báo cáo cảnh nào đã generate lại, cảnh nào chữ chèn bằng ffmpeg.
