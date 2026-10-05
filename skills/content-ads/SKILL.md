---
name: content-ads
description: "Viết content quảng cáo và lập lịch content social theo template: (1) Social Content Calendar — lịch đăng bài X tuần/tháng dạng bảng; (2) AIDA; (3) PAS; (4) BAB. 9 giọng văn tuỳ chọn, văn người viết (không giống AI) nhưng vẫn hấp dẫn, thuyết phục. Dùng BẤT CỨ KHI NÀO user nói: lên lịch content, content calendar, kế hoạch content, lịch đăng bài, content ads, AIDA, PAS, BAB, content quảng cáo, bài viết bán hàng, viết ads, ad copy, copy quảng cáo, content chạy quảng cáo, content theo khung. Không dùng cho bài Facebook cá nhân kể trải nghiệm (dùng facebook-content-viral) hay dựng chiến dịch trên trình quản lý quảng cáo (dùng meta-ads-setup). Luôn hỏi input trước khi viết. Tác giả: Đặng Hữu Sơn."
---

# Content Ads — Lịch content & framework quảng cáo

Bốn template, mỗi template một file trong `references/`. Chọn đúng template, hỏi đủ input, viết, rà văn AI, giao.

## Chọn template

| User muốn | Template | File |
|---|---|---|
| Kế hoạch **nhiều bài** theo tuần/tháng | **1. Social Content Calendar** | `references/social-calendar.md` |
| Giới thiệu sản phẩm mới, kể chuyện thương hiệu, khách **chưa biết** mình | **2. AIDA** | `references/aida.md` |
| Khách **đang đau rõ ràng**, cần đẩy quyết định, ads chuyển đổi | **3. PAS** | `references/pas.md` |
| Kết quả **thấy được**, có case trước/sau, muốn tạo khao khát | **4. BAB** | `references/bab.md` |

User gọi tên template → dùng luôn. User nói chung chung ("viết content ads") → hỏi kèm gợi ý theo bảng trên. Chỉ đọc file của template đang dùng.

## Bước 1 — Hỏi input

**Template 1 (lịch content):** hỏi 2–3 câu khảo sát trong `social-calendar.md`. Không hỏi giọng văn.

**Template 2–4 (một bài):** hỏi gộp một tin nhắn, chỉ câu còn thiếu. User dán ảnh/tài liệu/bài mẫu → đọc trước, trích những gì đã có.

| # | Câu hỏi | Dùng cho biến |
|---|---|---|
| 1 | Tên thương hiệu / sản phẩm / dịch vụ? | `{Brandname}` |
| 2 | Mô tả ngắn: lợi ích chính, điểm khác biệt? | `{benefits}` / `<Solution>` |
| 3 | Khách hàng mục tiêu là ai (tuổi, nghề, mối quan tâm)? | persona |
| 4 | Nỗi đau / vấn đề lớn nhất của khách mà sản phẩm giải quyết? | `{pain}` / `<Problems>` |
| 5 | Framework: AIDA / PAS / BAB, hay để mình gợi ý? | chọn file |
| 6 | Giọng văn (bảng dưới), hay để mình gợi ý? | style |
| 7 | Ngôn ngữ đầu ra? *mặc định tiếng Việt* | dòng cuối câu lệnh |

**Giọng văn — chỉ hiện bảng này cho user, không hiện prompt style:**

| # | Giọng văn | Phù hợp |
|---|---|---|
| 1 | Triết gia | Sản phẩm cao cấp, nghệ thuật, chiều sâu cảm xúc |
| 2 | Thân thiện & Trò chuyện | Đại chúng, B2C |
| 3 | Chuyên nghiệp & Uy tín | B2B, tư vấn, tài chính, BĐS cao cấp |
| 4 | Truyền cảm hứng | Khoá học, coaching, phát triển bản thân, fitness |
| 5 | Giáo dục & Thông tin | Sản phẩm kỹ thuật, phần mềm, dịch vụ chuyên ngành |
| 6 | Hài hước & Dí dỏm | Lifestyle, F&B, giải trí, thương hiệu trẻ |
| 7 | Cảm xúc & Gợi mở | Gia đình, sức khoẻ, kỷ niệm |
| 8 | Thuyết phục & Bán hàng | Ads trực tiếp, flash sale, chuyển đổi nhanh |
| 9 | Suy tư & Triết lý | Thương hiệu cao cấp, khác biệt bằng tư duy |

Không chọn → gợi ý theo sản phẩm. Mặc định: **2** cho B2C, **3** cho B2B.

## Bước 2 — Viết

1. Mở file template, lấy **câu lệnh gốc**, thay biến bằng input.
2. Template 2–4: nạp prompt giọng văn tương ứng từ `references/styles.md` vào cuối câu lệnh (nội bộ, không hiện cho user). Giọng Triết gia: tham khảo thêm `references/example-philosopher.md`.
3. Viết bản nháp.
4. **Rà bằng `references/anti-ai-writing.md`** — bắt buộc, kể cả khi user không nhắc. Giữ hook, cảm xúc và lực thuyết phục; bỏ dấu vết AI.
5. Giao bản đã rà.

## Quy tắc chung (template 2–4)

- **Không ghi nhãn** framework (A.I.D.A, P.A.S, B.A.B, VẤN ĐỀ, TRƯỚC/SAU…) trong bài. Bài liền mạch.
- Emoji: **1–2**, ở mở bài hoặc chỗ cần nhấn. Không rải.
- Đoạn 2–4 câu, xuống dòng thoáng, độ dài các đoạn so le.
- 150–350 từ.
- Liệt kê lợi ích: dùng 1/, 2/, 3/ hoặc viết thành đoạn, không dùng bullet.
- Chi tiết cụ thể thay cho nói chung. Không bịa số liệu, lời khách, giải thưởng — user không cung cấp thì không viết.
- Ngôn ngữ khác tiếng Việt: viết hoàn toàn bằng ngôn ngữ đó. Thuật ngữ marketing phổ biến (CTA, target…) được giữ tiếng Anh.

## Giao bài

- Chỉ giao nội dung. Không mở đầu "Đây là bài viết…", không ghi chú framework, không tóm tắt cuối.
- Sau bài, **một dòng** gợi ý bước tiếp: viết thêm phiên bản góc khác / đổi giọng văn / rút gọn thành bản ads 60–100 từ.
- User muốn đổi giọng → viết lại toàn bài với style mới, không vá từng câu.

## Liên kết skill khác
- Bài cần ảnh minh hoạ doodle hoặc bộ ảnh có chữ → `vibe-sketch-video`.
- Đưa bài lên chạy quảng cáo Meta → `meta-ads-setup` (bản ads ngắn 60–100 từ theo công thức bốn nhịp của skill đó).
