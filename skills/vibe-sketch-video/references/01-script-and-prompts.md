# Bước 1 — Kịch bản, lời đọc, chữ overlay, bộ prompt

Vai trò: đạo diễn kiêm biên kịch video doodle vẽ tay (người que có hồn + element đa dạng, có màu). Mọi cảnh là **một ảnh doodle tĩnh** chạy Ken Burns, không có motion graphics.

Đầu vào: khối PROJECT LOCK từ Bước 0 (`SKILL.md`). Đầu ra của file này: `PLAN.md`, `PROMPTS.md`, `VO_SCRIPT.md`.

## 1. Số cảnh theo thời lượng

| Thời lượng | Số cảnh (kể cả cover) | Số từ lời đọc / cảnh | Thời lượng / cảnh |
|---|---|---|---|
| ≤ 60s | 10–13 | 11–16 | ~4–6s |
| ~3 phút | 16–22 | 14–18 | ~8–11s |
| 5–10 phút | 22–24 | 16–20 | ~12–25s |

Vai trò cảnh: `cover` · `hook` · `body` · `outro`. **Cảnh #1 luôn là cover/thumbnail. Cảnh cuối là outro/CTA.** Mỗi bộ có **đúng một** cover.

Kiểm tổng: tổng số từ lời đọc ÷ 2,5 từ/giây ≈ thời lượng mục tiêu (tiếng Việt). Lệch quá 15% thì thêm/bớt cảnh.

## 2. Viết kịch bản

- **Bám nguồn.** Có nguồn → mọi cảnh xây trên ý, số liệu, ví dụ trong nguồn. Không nguồn → dùng kiến thức nền nhưng cụ thể, không chung chung.
- **Giọng:** đời, street-smart, góc nhìn người bản xứ của ngôn ngữ đã khoá. Đọc số bằng chữ.
- **Cấm sáo rỗng:** "BẠN SẼ KHÔNG TIN", "BÍ MẬT KHÔNG AI NÓI", "99% người bỏ lỡ" và các biến thể.
- **Một cảnh một ý.** Ý đó phải vẽ được thành một hình.
- **Tiêu đề video:** ≤ 12 từ, hấp dẫn, không sáo rỗng.
- **Rà văn AI:** viết xong lời đọc và chữ overlay, rà theo `anti-ai-writing.md`. Giữ hook và nhịp cuốn, bỏ từ/cấu trúc cấm. Lời đọc phải nghe như người thật đang kể.

## 3. Lời đọc ≠ chữ overlay

| Trường | Là gì | Luật |
|---|---|---|
| `voiceText` | Lời voice-over đầy đủ của cảnh | Ngôn ngữ đã khoá, số viết bằng chữ, đúng số từ/cảnh ở bảng trên |
| `onscreen` | Chữ hiển thị trên ảnh | Chỉ khi `text_overlay: yes`. **≤ 6 từ** (cứng: 8). Là ý chốt của cảnh, không chép lại lời đọc |

Gợi ý `onscreen` theo vai trò:
- `cover`: tiêu đề video (rút gọn ≤ 6 từ nếu tiêu đề dài).
- `hook`: câu chốt gây tò mò ("Sáng nào cũng thua"…).
- `body`: từ khoá / con số / khẩu hiệu của ý ("Ngủ trước 23 giờ").
- `outro`: CTA ngắn ("Bắt đầu từ tối nay").

Con số trong `onscreen` **được** viết bằng chữ số (vì là chữ đọc bằng mắt); trong `voiceText` thì viết bằng chữ.

## 4. Prompt ảnh (tiếng Anh)

Lắp prompt theo thứ tự trong `00-prompt-locks.md`. Style lock của SKETCH:

```
Hand-drawn doodle illustration, expressive lively ink linework with character, tasteful
color accents on a warm paper background, varied elements (people, objects, scenery,
symbols — not just a stick figure), one clear focal idea, generous empty space.
```

### Cover (#1)

```
<STYLE LOCK>, COVER/thumbnail composition: the richest, most detailed doodle of the set,
a bold central focal scene that captures the whole topic: <chủ đề, tả bằng tiếng Anh>.
Rich but uncluttered.
<ASPECT RATIO LOCK>
<text_overlay: yes → LANGUAGE LOCK + TEXT OVERLAY LOCK với "<tiêu đề>", ZONE = top third>
<text_overlay: no  → NO-TEXT LOCK + "Leave the top third as calm empty space.">
```

### Cảnh #2..#n

```
<STYLE LOCK>, illustrating: <ý của cảnh, tả cụ thể: ai, làm gì, ở đâu, vật gì, cảm xúc gì>.
<ASPECT RATIO LOCK>
<text_overlay: yes → LANGUAGE LOCK + TEXT OVERLAY LOCK với "<onscreen của cảnh>">
<text_overlay: no  → NO-TEXT LOCK>
```

Ví dụ hoàn chỉnh (tiếng Việt, 9:16, overlay có):

```
Hand-drawn doodle illustration, expressive lively ink linework with character, tasteful
color accents on a warm paper background, varied elements (people, objects, scenery,
symbols — not just a stick figure), one clear focal idea, generous empty space,
illustrating: a tired stick-figure man slumped at a desk at 2 a.m., a glowing phone in
his hand, an alarm clock showing late night, empty coffee cups piling up.
STRICT ASPECT RATIO LOCK: The output MUST be exactly 9:16 vertical. […nguyên khối…]
LANGUAGE LOCK: This prompt is written in English, but every quoted string ("…") is final
Vietnamese content. […nguyên khối…]
TEXT OVERLAY LOCK: This image MUST display exactly this text, once, in Vietnamese:
"Thức khuya là vay nợ"
[…nguyên khối, TYPE STYLE = hand-lettered marker…, ZONE = top third…]
```

Luật phong cách nhất quán: giữ **cùng style lock, cùng bảng màu nhấn, cùng kiểu chữ overlay** cho mọi cảnh. Nếu có nhân vật lặp lại (VD: "Nam"), viết một dòng mô tả cố định (`a stick figure with messy black hair and a red scarf`) và chép nguyên văn vào mọi cảnh có Nam.

## 5. Xuất bộ kịch bản (Checkpoint C1)

### `PLAN.md`
```
<PROJECT LOCK>

# <Tiêu đề video>
Thời lượng · Ngôn ngữ · Tỷ lệ · Số cảnh (kể cả cover) · Overlay: có/không

| # | Vai trò | Lời đọc (voiceText) | Chữ overlay | Ý cảnh (ngôn ngữ user) |
|---|---|---|---|---|
| 1 | cover | … | … | … |
```

### `PROMPTS.md`
```
#1 (cover)
Ý cảnh: <mô tả bằng ngôn ngữ user>
Chữ overlay: "<…>"            ← chỉ khi overlay có
Prompt: <prompt EN đầy đủ, đã lắp các khối lock>
```

### `VO_SCRIPT.md`
Từng cảnh (`## s01 — cover`, lời đọc, ghi chú giọng) + một đoạn **lời đọc liền mạch** toàn bộ, ngắt cảnh bằng `↵`.

### JSON (tuỳ chọn, để nạp máy)
```json
[
  {
    "id": "s01",
    "type": "cover|hook|body|outro",
    "voiceText": "lời đọc, số viết bằng chữ",
    "onscreen": "chữ overlay hoặc rỗng nếu overlay = không",
    "imagePrompt": "English prompt, đã gồm đủ lock",
    "kenBurns": "in|out|pan-left|pan-right"
  }
]
```

### Trình bày ở C1 (chế độ duyệt) — hiện đủ, không tóm tắt
Gửi cho user **ngay trong chat**, theo thứ tự:
1. Tiêu đề + dòng thông số (thời lượng · ngôn ngữ · tỷ lệ · số cảnh · overlay).
2. **Bảng cảnh đầy đủ** như `PLAN.md`.
3. **Toàn bộ prompt** như `PROMPTS.md` — mỗi prompt nguyên văn, kèm "Ý cảnh" và "Chữ overlay". Không rút gọn, không ghi "…tương tự".
4. **Lời đọc liền mạch** (đoạn `↵`).
5. Dòng lệnh: *Gõ **`ok`** để tạo bộ ảnh · **`sửa cảnh 5: …`** · **`đổi tiêu đề: …`***

### Chia lô khi dài
Tổng prompt > 12 → trình bày theo lô ~8 cảnh. Cuối mỗi lô:
> *Xong lô 1/3 (cảnh 1–8). Gõ **`tiếp`** để xem lô kế · **`sửa cảnh 5: …`** để chỉnh · **`đủ rồi`** để chốt sớm.*

Chế độ chạy luôn: ghi đủ các file, không trình bày theo lô, không dừng.

### Tự kiểm trước khi trình bày
- [ ] Đúng 1 cover ở #1, cảnh cuối là outro, đánh số liên tục 1..n
- [ ] Số từ/cảnh và tổng thời lượng khớp bảng
- [ ] Lời đọc: số viết bằng chữ, không sáo rỗng, bám nguồn (nếu có)
- [ ] Overlay **có**: mọi prompt có LANGUAGE LOCK + TEXT OVERLAY LOCK; chuỗi trong prompt giống hệt cột "Chữ overlay"; mỗi chuỗi ≤ 6 từ (cứng 8)
- [ ] Overlay **không**: mọi prompt có NO-TEXT LOCK, cột "Chữ overlay" bỏ trống
- [ ] Mọi prompt có ASPECT RATIO LOCK đúng tỷ lệ đã khoá
- [ ] Mỗi prompt có dòng "Ý cảnh" bằng ngôn ngữ user

Chế độ duyệt: dừng ở đây, chờ user `ok` rồi mới sang `02-images.md`.
