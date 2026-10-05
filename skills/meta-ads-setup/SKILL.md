---
name: meta-ads-setup
description: Thiết lập, kiểm tra và tối ưu chiến dịch quảng cáo Meta (Facebook/Instagram) qua MCP. Dùng skill này BẤT CỨ KHI NÀO user muốn tạo chiến dịch quảng cáo, dựng nhóm quảng cáo, tạo ads, kiểm tra hiệu quả quảng cáo, phân tích số liệu Meta Ads, tối ưu ngân sách, tắt/bật quảng cáo, chọn tệp khách hàng, kiểm tra pixel/dataset/custom conversion, tạo lookalike, hoặc nhắc đến 'chạy ads', 'chạy quảng cáo', 'Facebook Ads', 'Meta Ads', 'campaign', 'adset', 'CPL', 'ROAS', 'retarget', 'tệp lookalike', 'quảng cáo chéo', 'partner ads'. Cũng trigger khi user gửi link landing page và muốn chạy quảng cáo, hoặc gửi banner/video và hỏi cách đưa lên quảng cáo. Skill này CHỦ ĐỘNG hỏi xác nhận trước khi tiêu tiền, kiểm tra dữ liệu trước khi dựng, và luôn để trạng thái PAUSED cho user duyệt.
---

# Thiết lập quảng cáo Meta Ads

Skill này hướng dẫn quy trình đầy đủ từ lúc user nói "muốn chạy quảng cáo" đến khi chiến dịch sẵn sàng bật.

## Nguyên tắc bất di bất dịch

**Luôn để PAUSED.** Mọi thứ tạo ra đều ở trạng thái tạm dừng. Chỉ bật khi user xác nhận rõ ràng.

**Không đoán ngân sách.** Tiền của user. Hỏi, đừng tự quyết.

**Kiểm tra dữ liệu trước khi dựng.** Pixel hỏng thì quảng cáo chạy mù. Kiểm tra trước, dựng sau.

**Báo cáo bằng số, không bằng cảm tính.** Kéo dữ liệu thật rồi mới kết luận.

**Nói thẳng khi thấy vấn đề.** Nếu kế hoạch của user có rủi ro rõ ràng, nói ra trước khi làm.

---

## QUY TRÌNH 6 BƯỚC

### Bước 1 — Xác nhận thông tin nền

Hỏi user ba nhóm thông tin. Dùng `ask_user_input_v0` nếu có, không thì hỏi bằng bảng.

**Tài khoản quảng cáo**
- Chạy trên tài khoản nào? (liệt kê các tài khoản khả dụng để user chọn)
- Page nào đứng tên quảng cáo?

**Mục tiêu**
- Thu khách tiềm năng (lead) hay bán hàng trực tiếp?
- Sản phẩm giá bao nhiêu? → quyết định cấu trúc, xem `references/chien-luoc.md`
- Có deadline không? (sự kiện, workshop, khuyến mãi)

**Ngân sách**
- Tổng bao nhiêu, hay mỗi ngày bao nhiêu?
- Chạy trong bao nhiêu ngày?

> Nếu user chưa rõ ngân sách, gợi ý theo bảng trong `references/chien-luoc.md` mục "Ngân sách tối thiểu".

---

### Bước 2 — Kiểm tra và báo cáo hiện trạng

**Luôn làm bước này trước khi dựng bất cứ thứ gì.**

Kéo dữ liệu theo thứ tự:

1. **Danh sách chiến dịch** đang chạy và đã tắt — xem user đang có gì
2. **Số liệu 30 ngày** cấp chiến dịch: chi phí, kết quả, CPL, CTR, tần suất
3. **Sức khoẻ dataset**: các sự kiện đang fire, số lượng, điểm chất lượng khớp
4. **Custom conversion** hiện có và trạng thái
5. **Danh sách audience**: tệp nào dùng được, tệp nào quá nhỏ

Sau đó **báo cáo cho user** theo mẫu:

```
TÌNH HÌNH TÀI KHOẢN

Đang chạy: [số] chiến dịch
Chi 30 ngày: [số]đ
Kết quả: [số] — giá mỗi kết quả [số]đ

ĐIỂM ĐÁNG CHÚ Ý
- [phát hiện 1]
- [phát hiện 2]

VẤN ĐỀ CẦN XỬ LÝ
- [vấn đề nếu có, kèm mức nghiêm trọng]
```

Chi tiết cách đọc số: `references/phan-tich.md`

---

### Bước 3 — Chọn loại quảng cáo

Hỏi user muốn chạy loại nào:

| Loại | Khi nào dùng | Cần chuẩn bị |
|---|---|---|
| **Ảnh tĩnh (banner)** | Mặc định, rẻ và nhanh | 3-5 banner |
| **Video** | Tệp đã bão hoà ảnh tĩnh, muốn vào Reels | Video + ảnh bìa |
| **Carousel** | Nhiều sản phẩm hoặc nhiều bước | 3-10 thẻ |
| **Quảng cáo chéo (partnership)** | Chạy dưới tên page/tài khoản khác | Partner ID + quyền |
| **Bài đăng có sẵn** | Muốn tích luỹ tương tác | Post ID |

**Với quảng cáo chéo:** cần `partner_id` hoặc mã cho phép từ đối tác. Hỏi user đã có chưa. Nếu chưa, hướng dẫn: đối tác vào Business Settings → Partnership ads → tạo mã cho phép, gửi lại.

---

### Bước 4 — Kiểm tra nền tảng dữ liệu

Bốn thứ phải đúng trước khi dựng. Chi tiết: `references/dataset-audience.md`

**4.1. Dataset và pixel**
- Trang đích đã gắn pixel chưa?
- Sự kiện Lead và Purchase có fire không?
- Điểm chất lượng khớp bao nhiêu? (dưới 6 là kém)
- Có bị đếm đôi không?

**4.2. Custom conversion**
- Sản phẩm này đã có nhãn phân loại riêng chưa?
- Nhãn đó đã nhận được dữ liệu chưa? (chưa có dữ liệu thì không dùng làm mục tiêu tối ưu được)
- Nếu chưa có, hướng dẫn user tạo — xem mẫu trong reference

**4.3. Audience**
- Liệt kê tệp hiện có kèm quy mô
- Tệp nào dưới 1.000 người → cảnh báo không dùng được
- Có tệp loại trừ người đã mua chưa?

**4.4. Lookalike**
- Có lookalike 1% từ nguồn chất lượng chưa?
- Nguồn có đủ 1.000 người không?
- Nếu thiếu, đề xuất tạo từ nguồn nào

> **Quan trọng:** dữ liệu 5 tháng cho thấy tệp Broad + Advantage+ thường rẻ hơn Lookalike 2,4 lần cho sản phẩm giá thấp. Đừng mặc định chọn Lookalike. Xem `references/chien-luoc.md`.

---

### Bước 5 — Thu thập tài nguyên

Hướng dẫn user cung cấp:

**Link trang đích** — bắt buộc. Kiểm tra:
- Trang mở được không
- Có giữ tham số trên URL không (test với `?fbclid=test123`)
- Đã gắn pixel chưa

**Banner** — yêu cầu link ảnh công khai, không phải file đính kèm.

Nói với user:
> "Gửi tôi link ảnh trực tiếp (dạng https://.../anh.png). Nếu ảnh đang ở máy, upload lên nơi nào có link công khai trước."

Với mỗi banner, hỏi hoặc tự xác định **góc nội dung** — nhắm kiểu người nào.

**Video** — link file mp4 công khai. Lưu ý:
- Cần ảnh bìa riêng
- Kiểm tra độ dài: tệp lạnh nên 15-30 giây
- Kiểm tra tỷ lệ: 9:16 cho Reels, 4:5 cho Feed

**Nội dung chữ** — nếu user chưa có, đề xuất theo công thức trong `references/noi-dung.md`, rồi rà theo `references/anti-ai-writing.md` trước khi đưa user duyệt. Câu hỏi mở đầu ở nhịp 1 được giữ khi nó gọi tên một khoản mất cụ thể (xem bảng "Luật ưu tiên" trong file đó). Cần bài dài theo khung AIDA / PAS / BAB → dùng skill `content-ads`.

> **Cảnh báo bắt buộc nói với user:** Meta không cho sửa nội dung quảng cáo sau khi đã đăng. Không đưa giá, ngày giờ, số suất vào chữ — đổi những thứ đó là phải làm lại toàn bộ và mất hết lịch sử học.

---

### Bước 6 — Dựng chiến dịch

Thứ tự thao tác:

```
1. Tạo campaign (PAUSED)
2. Tạo các adset (PAUSED)
3. Upload ảnh/video → lấy hash
4. Tạo creative
5. Tạo ads gắn creative vào adset (PAUSED)
6. Verify toàn bộ
7. Báo cáo cho user, chờ duyệt
```

**Cấu hình adset — điểm dễ sai:**

| Trường | Giá trị | Lý do |
|---|---|---|
| `geo_locations` | Chỉ `{"countries":["VN"]}` | Không thêm `location_types` — gây lỗi không publish được |
| `optimization_goal` | Theo giá sản phẩm | Xem bảng trong `references/chien-luoc.md` |
| `promoted_object` | Pixel + event, hoặc custom conversion | Quyết định trước, không sửa được sau |
| `destination_type` | `WEBSITE` | Nếu bỏ trống, Meta mặc định Instant Form |
| `excluded_custom_audiences` | Người đã mua + tệp chiến dịch khác | Tránh tự cạnh tranh |

**Mỗi adset cần 3-5 ads**, mỗi ad một góc nội dung khác nhau.

Sau khi dựng xong, báo cáo:

```
ĐÃ DỰNG XONG — TẤT CẢ ĐANG PAUSED

Chiến dịch: [tên] — [ID]
Mục tiêu: [...] | Tối ưu: [...]

| Nhóm | Tệp | Ngân sách/ngày | Số ads |
|---|---|---|---|
...

Tổng: [số]đ/ngày

TRƯỚC KHI BẬT, KIỂM TRA:
□ Preview từng ad — ảnh và chữ đúng
□ Bấm thử nút — ra đúng trang đích
□ Quy mô tệp không quá nhỏ

THỨ TỰ BẬT: [đề xuất cụ thể]
```

---

## SAU KHI BẬT

Đưa user lịch theo dõi:

| Thời điểm | Việc |
|---|---|
| Ngày 1-3 | **Không động vào.** Chỉ theo dõi. Mọi chỉnh sửa đều reset learning phase |
| Ngày 4-6 | Tắt nhóm chi nhiều mà không có tín hiệu nào |
| Ngày 7-10 | Tăng ngân sách nhóm thắng, mỗi lần ≤20% |
| Ngày 11+ | Theo dõi tần suất, thay creative khi vượt 2,5 |

---

## KHI GẶP LỖI

Tra `references/loi-thuong-gap.md`. Các lỗi hay gặp nhất:

| Triệu chứng | Mục tra |
|---|---|
| Không publish được, báo lỗi vị trí | Lỗi 1 |
| Không tạo/sửa được gì | Lỗi 2 |
| Không đổi được sự kiện tối ưu | Lỗi 3 |
| Custom conversion báo chưa hoạt động | Lỗi 4 |
| Adset bật mà không tiêu tiền | Lỗi 6 |
| Meta báo ít conversion hơn thực tế | Lỗi 7 |

---

## Reference files

Đọc khi cần, không nạp hết ngay:

- `references/chien-luoc.md` — chọn mục tiêu, tệp, ngân sách theo giá sản phẩm; tư duy phễu
- `references/dataset-audience.md` — kiểm tra pixel, tạo custom conversion, dựng audience và lookalike
- `references/noi-dung.md` — công thức viết nội dung, góc nào hiệu quả, banner nào nên làm
- `references/phan-tich.md` — đọc số liệu, chỉ số nào quan trọng, đối chiếu với hệ thống bán hàng
- `references/loi-thuong-gap.md` — 10 lỗi và cách xử lý
- `references/anti-ai-writing.md` — rà mọi chữ trên quảng cáo cho giống người viết, vẫn thuyết phục
