# Bước 2 — Mega Prompt từng cảnh

## Mục đích
Viết một prompt "copy-paste là chạy" cho mỗi cảnh, gom đủ: style lock, character lock, camera, hành động, âm thanh, nhạc, lời thoại/VO, chữ trên hình, first/last frame. Viết kỹ ở đây thì video ít phải sửa. Character lock lấy từ `STORY.md`; character sheet (bước 3) vẽ sau, dựa trên chính lock này.

Chế độ duyệt: viết ngay sau `STORY.md` và trình bày cùng lúc ở Checkpoint C1. Chế độ chạy luôn: viết rồi dùng luôn.

## Global locks (đầu mọi prompt, tiếng Anh)
```
<Style lock từ STORY.md, VD: Soft 2D Disney/Pixar animation, clean rounded shapes,
warm cinematic lighting, painterly rich backgrounds.>
<ASPECT RATIO LOCK>
<Character lock chép nguyên văn từ STORY.md cho nhân vật trong cảnh>
Keep every character exactly on-model with the attached sheets in all frames.
```

## Cấu trúc mega prompt
```
<GLOBAL LOCKS>
FIRST FRAME: <frame đầu = keyframe đầu (duyệt) / frame cuối clip trước (chạy luôn)>
MOTION: <diễn biến hành động theo trình tự thời gian, từng bước>
CAMERA: <push-in, orbit, aerial follow…>
LAST FRAME: <match keyframe cuối (duyệt) / mô tả rõ tư thế + bố cục kết (chạy luôn)>
SOUND: <tiếng động chi tiết: gió, bước chân, lửa crackle…>
MUSIC: <diễn biến nhạc>
DIALOGUE: <tên nhân vật> says "<thoại, ngôn ngữ đã khoá>"        ← nếu có thoại
VO (warm narrator, <LANGUAGE>): "<câu VO, ngôn ngữ đã khoá>"
ON-SCREEN TEXT: "<chuỗi chính xác>" — <placement>, appears at <giây>, stays static and
fully legible until <giây>; letters never morph, warp or animate.   ← chỉ khi cảnh có chữ
<LANGUAGE LOCK>            ← khi có DIALOGUE / VO / ON-SCREEN TEXT
<NO-TEXT LOCK>             ← khi cảnh không có ON-SCREEN TEXT
```

Ghi chú:
- VO và DIALOGUE trong prompt giúp model khớp diễn xuất/khẩu hình. Âm thanh VO cuối cùng vẫn lấy từ file TTS ở `05-vo-production.md`.
- Cảnh có `ON-SCREEN TEXT`: thay NO-TEXT LOCK bằng câu `The quoted ON-SCREEN TEXT is the only text allowed in the video.`

## Thứ tự nạp ref (bắt buộc)
1. Character sheet của nhân vật trong cảnh
2. First frame (keyframe hoặc frame trích từ clip trước)
3. Last frame (chỉ chế độ duyệt)
→ Rồi mới đến prompt text.

## Luật realism (đọc kỹ trước khi viết MOTION)
Mọi hành động vật lý nhỏ phải đúng cơ chế thực tế. Ví dụ từ dự án thật:
- Thắp đèn có khung kính: **mở cửa kính → đưa bấc vào chạm tim đèn → đóng cửa lại**. Không viết "châm lửa xuyên qua kính".
- Bão dập lửa: gió **xé rách đèn giấy**, lửa **chập chờn trong housing kính rung lắc rồi tắt**.
- Đèn lớn: châm qua **miệng mở phía dưới** và **khay lửa sắt**.
Kiểm từng động từ trong MOTION: "ngoài đời nó có xảy ra như vậy không?" Không → viết lại.

## Trình bày cho user (chế độ duyệt)
Mỗi cảnh: prompt EN đầy đủ + 2–3 dòng tóm tắt bằng ngôn ngữ user (chuyện gì xảy ra, camera, lời thoại/VO, chữ trên hình).

## Checklist
- [ ] Mỗi cảnh một mega prompt đủ các mục
- [ ] Global locks (style + ASPECT + character) có trong mọi prompt
- [ ] Thoại/VO/chữ: nguyên văn ngôn ngữ đã khoá, có LANGUAGE LOCK
- [ ] Cảnh có chữ: ON-SCREEN TEXT khớp `STORY.md` từng ký tự; cảnh không chữ: có NO-TEXT LOCK
- [ ] Thứ tự ref đúng
- [ ] MOTION đã rà realism
