# Prompt Locks — các khối ràng buộc dán vào prompt

Đây là nguồn duy nhất cho các khối ràng buộc. File pipeline nào cũng trỏ về đây; không chép lại phiên bản khác ở chỗ khác.

Các khối viết bằng tiếng Anh và dán **nguyên văn** vào prompt. Chỉ thay phần trong `<…>`.

## Thứ tự trong một prompt

```
1. Style lock            (từ STORY.md / PLAN.md)
2. ASPECT RATIO LOCK
3. Character lock        (FILM, nếu cảnh có nhân vật)
4. Nội dung cảnh         (mô tả hình / FIRST FRAME / MOTION …)
5. LANGUAGE LOCK         (khi prompt chứa bất kỳ chuỗi nội dung nào: chữ, thoại, VO)
6. TEXT OVERLAY LOCK     (text_overlay: yes và ảnh này có chữ)
   hoặc NO-TEXT LOCK     (text_overlay: no, hoặc ảnh dùng làm keyframe/ref)
```

---

## 1. ASPECT RATIO LOCK (mọi prompt ảnh và video)

```
STRICT ASPECT RATIO LOCK: The output MUST be exactly <16:9 landscape | 9:16 vertical>.
All reference images — character sheets, keyframes, first-frame and last-frame images —
share this exact ratio and directly condition framing and composition. Never introduce
another ratio. Keep every important element inside the central safe area.
```

## 2. LANGUAGE LOCK (khi prompt chứa chuỗi nội dung)

Thay `<LANGUAGE>` bằng tên ngôn ngữ đầy đủ bằng tiếng Anh: `Vietnamese`, `English`, `Japanese`…

```
LANGUAGE LOCK: This prompt is written in English, but every quoted string ("…") is final
<LANGUAGE> content. Reproduce quoted strings exactly as written, character by character,
including every diacritic, accent and punctuation mark. Never translate, paraphrase,
shorten, romanize or correct them. Do not add any words in any other language.
```

## 3. TEXT OVERLAY LOCK (khi `text_overlay: yes`)

```
TEXT OVERLAY LOCK: This image MUST display exactly this text, once, in <LANGUAGE>:
"<EXACT TEXT>"
- Spell it exactly as quoted, letter by letter. <VIETNAMESE ONLY: Every Vietnamese
  diacritic (ă â ê ô ơ ư đ and tone marks ́ ̀ ̉ ̃ ̣) must be present, correctly shaped, and
  sitting on the correct letter.>
- Typography: <TYPE STYLE>, large, bold, high contrast against the background,
  legible at phone size. One or two lines maximum, balanced line break.
- Placement: <ZONE>, inside the safe area (at least 8% margin from every edge),
  never covering faces or the main subject.
- This is the ONLY text in the image: no other letters, numbers, labels, signs,
  logos, captions or watermarks anywhere.
```

Giá trị gợi ý:

| Biến | SKETCH | FILM (cover / title card) |
|---|---|---|
| `<TYPE STYLE>` | `hand-lettered marker style matching the doodle ink, dark ink with one accent color` | `clean bold rounded sans-serif, cinematic title treatment` |
| `<ZONE>` | `top third` (9:16) hoặc `left third` (16:9) | `lower third` hoặc `centered over empty sky` |

Luật viết chuỗi `<EXACT TEXT>`:
- **Tối đa 6 từ** (cứng: 8). Càng ngắn model vẽ càng đúng, nhất là tiếng Việt có dấu.
- Một ảnh **một chuỗi**. Cần kicker + headline thì gộp thành một chuỗi hai dòng, ngăn bằng ` / ` và ghi rõ `line break at "/"`.
- Không emoji, không ký tự đặc biệt, không dấu ngoặc kép bên trong chuỗi.
- Viết đúng chính tả, đúng hoa/thường như muốn hiển thị. Chuỗi trong prompt phải **giống hệt** chuỗi trong cột "Chữ overlay" của bảng cảnh.

## 4. NO-TEXT LOCK

Dùng khi `text_overlay: no`, và **luôn dùng** cho character sheet, keyframe FILM (ảnh làm ref cho video — chữ sẽ biến dạng khi chuyển động).

```
NO-TEXT LOCK: No text, letters, numbers, captions, signs, labels, logos or watermarks
anywhere in the image.
```

---

## Kiểm tra chữ sau khi tạo ảnh (bắt buộc khi `text_overlay: yes`)

Mở ảnh xem trực tiếp, so **từng ký tự** với chuỗi trong bảng cảnh:

- [ ] Chữ có xuất hiện, đúng một lần
- [ ] Đúng chính tả từng chữ cái, không thiếu/thừa chữ
- [ ] Đủ dấu và dấu nằm đúng chữ (tiếng Việt: kiểm riêng ư/ơ/ă/â/ê/ô/đ và 5 dấu thanh)
- [ ] Không có chữ nào khác trong ảnh (biển hiệu, nhãn, chữ ký giả…)
- [ ] Đọc được ở kích thước điện thoại, không đè lên mặt/tiêu điểm

Không đạt → quy trình sửa:

1. **Lần 1:** tạo lại với cùng prompt, thêm vào cuối: `The previous attempt misspelled the text. Render "<EXACT TEXT>" with extra care, larger and simpler letterforms.`
2. **Lần 2:** rút ngắn chuỗi (nếu user đã duyệt bản ngắn hơn) hoặc tách 2 dòng; tạo lại.
3. **Vẫn sai → phương án dự phòng (bắt buộc, không giao ảnh sai chữ):** tạo lại ảnh với NO-TEXT LOCK và `leave the <ZONE> as calm empty space for a title`, rồi chèn chữ bằng script đi kèm skill (Pillow, đã kiểm với dấu tiếng Việt, không cần ffmpeg có `drawtext`):

```bash
python3 <skill>/scripts/text_overlay.py --in s05_clean.png --out s05.png \
  --text "<EXACT TEXT>" --zone <top|center|bottom> --style dark
# --style dark  = chữ mực đậm viền trắng (nền giấy doodle)
# --style light = chữ trắng viền đậm (nền tối / video)
# " / " trong chuỗi = xuống dòng; --font <file.ttf> nếu muốn font riêng (Be Vietnam Pro, Noto Sans)
```

Không có Pillow (`pip install pillow` thất bại) mà ffmpeg có `drawtext` (`ffmpeg -filters | grep drawtext`):

```bash
printf '%s' "<EXACT TEXT>" > /tmp/overlay_s05.txt     # textfile: không phải escape dấu
ffmpeg -y -i s05_clean.png -vf "drawtext=fontfile=<font hỗ trợ tiếng Việt>.ttf:textfile=/tmp/overlay_s05.txt:\
fontsize=<96 cho 1080×1920 | 80 cho 1920×1080>:fontcolor=0x1E1E1E:borderw=6:bordercolor=white:\
x=(w-text_w)/2:y=h*0.10" s05.png
```

Sau khi chèn, mở ảnh kiểm lại một lần theo checklist trên.

Ghi lại cảnh nào dùng phương án dự phòng để báo user (chế độ duyệt: báo ngay; chế độ chạy luôn: báo trong báo cáo cuối).

## Kiểm tra NO-TEXT

Ảnh có chữ lạc (chữ giả, chữ nguệch ngoạc trên biển, nhãn) → tạo lại với NO-TEXT LOCK đặt lên **đầu** prompt. Chữ lạc trên keyframe FILM là lỗi nặng: nó sẽ trôi và méo trong video.
