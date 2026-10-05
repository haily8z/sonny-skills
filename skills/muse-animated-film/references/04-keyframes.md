# Bước 4 — Keyframes (Khung hình chốt)

> **Chỉ chạy ở chế độ duyệt** (`run_mode: review`). Chế độ chạy luôn bỏ qua giai đoạn này; continuity được nối bằng frame cuối của clip trước (xem `06-video-generation.md`).

## Mục đích
Vẽ trước các mốc hình ảnh của phim: K1..K(N+1) cho N cảnh. Keyframe = first frame và last frame của từng cảnh. Có keyframe rồi thì video chỉ việc "đi từ A đến B".

## Quy trình
1. Từ `STORY.md`, liệt kê K1..K(N+1): K1 = first frame cảnh 1, K2 = last frame cảnh 1 = first frame cảnh 2, …, K(N+1) = last frame cảnh N.
2. Mỗi keyframe: nạp character sheet của nhân vật trong frame làm ref **trước**, rồi mới đến mô tả:
   ```
   /opt/hatch/bin/media-generation --media-subagent-output-type image \
     --orientation <landscape | vertical> \
     --image-file <path/character-sheet.webp> \
     --output-dir <project>/keyframes \
     "<style lock + ASPECT RATIO LOCK + character lock + mô tả keyframe + NO-TEXT LOCK>"
   ```
3. **Keyframe luôn dùng NO-TEXT LOCK**, kể cả khi `text_overlay: yes` — keyframe là frame chuyển cảnh dùng chung giữa hai clip, chữ trên đó sẽ méo khi chuyển động. Chữ của FILM được đưa vào ở mega prompt (`ON-SCREEN TEXT`) và ở cover.
4. **Cover/thumbnail** (khi `text_overlay: yes`): tạo thêm một ảnh riêng `cover.webp` theo prompt cover, có LANGUAGE LOCK + TEXT OVERLAY LOCK với tên phim. Kiểm chữ theo `00-prompt-locks.md`.
5. Kiểm tra từng keyframe: đúng tỷ lệ, nhân vật on-model (so với sheet), ánh sáng đúng beat, không chữ.
6. Đặt tên rõ ràng: `k1-city-dusk.webp`, `k2-spark-falls.webp`…

## Trình bày (Checkpoint C2)
Gửi sheet + keyframe (+ cover) theo thứ tự, mỗi ảnh một dòng mô tả bằng ngôn ngữ user:
> *Đủ K1–K9 + cover. Gõ **`ok`** để làm VO · **`lại K4`** · **`sửa K6: …`**.*

## Checklist
- [ ] Đủ K1..K(N+1)
- [ ] K cuối cảnh N và K đầu cảnh N+1 là CÙNG MỘT FILE (luật match-cut)
- [ ] Nhân vật khớp character sheet
- [ ] Tất cả đúng tỷ lệ khoá, không chữ
- [ ] Overlay có: cover có tên phim đúng từng ký tự
