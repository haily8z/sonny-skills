# Template 1 — Social Content Calendar (Lịch content social)

## Khi nào dùng
User muốn **lập kế hoạch nhiều bài đăng theo thời gian**: "lên lịch content", "lịch đăng bài", "content calendar", "kế hoạch content tháng", "content plan 4 tuần", "mỗi tuần đăng gì". Không dùng khi user chỉ cần **một** bài (→ AIDA / PAS / BAB).

## Khảo sát trước (2–3 câu, gộp một tin nhắn)
Chỉ hỏi câu còn thiếu. Không hỏi quá 3 câu.

1. **Brand + sản phẩm:** tên thương hiệu, sản phẩm/dịch vụ, mô tả ngắn chủ đề cần truyền thông.
2. **Vấn đề + lợi ích:** khách hàng đang gặp vấn đề gì, sản phẩm giúp được gì (lợi ích chính, điểm khác biệt).
3. **Khối lượng + kênh:** bao nhiêu bài trong bao lâu (X bài / X tuần hoặc tháng), đăng trên nền tảng nào — *mặc định: 3 bài/tuần, 4 tuần, Facebook + Instagram + TikTok.* Ngôn ngữ đầu ra nếu khác tiếng Việt.

Nếu có công cụ tìm kiếm web: **research** nhanh trước khi lập lịch (xu hướng của ngành, ngày lễ / sự kiện trong khoảng thời gian, đối thủ đang nói gì). Ghi 2–3 dòng "Căn cứ" phía trên bảng. Không có công cụ tìm kiếm thì bỏ dòng căn cứ, không bịa xu hướng.

## Câu lệnh gốc

```
Research và lên lịch content social media trong {X ngày/tuần}. Sử dụng định dạng
bảng/danh sách dễ theo dõi với {X tuần/ngày} về {BrandName}. Bảng phải bao gồm các cột
sau: Thời gian, Nền tảng, Loại nội dung, Mục tiêu đối tượng, Dòng tiêu đề, Sao chép
quảng cáo có biểu tượng cảm xúc và Hình ảnh. Tham khảo {Description}.
Hãy đảm bảo rằng bảng được sắp xếp hợp lý và dễ hiểu, với thông tin rõ ràng và ngắn gọn
cho mỗi bài đăng. Viết bằng {ngôn ngữ user yêu cầu}.
```

Biến: `{BrandName}` = câu 1 · `{Description}` = câu 1 + câu 2 · `{X…}` = câu 3.

## Định dạng bảng

| Thời gian | Nền tảng | Loại nội dung | Mục tiêu đối tượng | Dòng tiêu đề | Nội dung (có emoji) | Hình ảnh |
|---|---|---|---|---|---|---|
| T2 · 06/10 · 19:30 | Facebook | Carousel kiến thức | Chủ shop mới bán online | … | … | Mô tả ảnh cụ thể để designer/AI làm được |

- **Thời gian:** thứ + ngày + giờ đăng đề xuất. Nhóm theo tuần, mỗi tuần một tiêu đề nhỏ `Tuần 1 — <chủ đề tuần>`.
- **Loại nội dung:** xoay vòng (giáo dục, câu chuyện khách hàng, hậu trường, bán hàng, tương tác, trend). Bài bán hàng không quá 1/3 tổng số bài.
- **Dòng tiêu đề:** ≤ 12 từ, cụ thể.
- **Nội dung (có emoji):** 1–3 câu sẵn để đăng hoặc làm khung viết bài dài, có 1–2 emoji.
- **Hình ảnh:** mô tả đủ để làm ra (bố cục, chủ thể, chữ trên ảnh nếu có). Bài cần ảnh doodle/AI → gợi ý gọi skill `vibe-sketch-video` (chỉ bộ ảnh).

Bảng dài hơn ~12 dòng: chia mỗi tuần một bảng.

## Sau bảng
Một dòng hỏi tiếp: *"Muốn mình viết đầy đủ bài nào trong lịch không? Gõ số dòng hoặc ngày."* Bài được chọn viết bằng AIDA / PAS / BAB tuỳ mục tiêu của dòng đó.

## Tự kiểm
- [ ] Đủ 7 cột, đủ số bài user yêu cầu, đúng khoảng thời gian
- [ ] Không có hai bài liền nhau cùng loại nội dung
- [ ] Mỗi dòng tiêu đề và nội dung đã qua `anti-ai-writing.md`
- [ ] Đúng ngôn ngữ user yêu cầu
