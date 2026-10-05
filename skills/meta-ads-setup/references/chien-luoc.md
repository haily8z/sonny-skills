# Chiến lược quảng cáo

## Mục lục
1. Chọn mục tiêu chiến dịch
2. Chọn sự kiện tối ưu theo giá sản phẩm
3. Chọn tệp khách hàng
4. Ngân sách tối thiểu
5. Cấu trúc chiến dịch
6. Tư duy phễu
7. Chạy nhiều chiến dịch cùng lúc

---

## 1. Chọn mục tiêu chiến dịch

| Mục tiêu | Chọn khi | Tránh khi |
|---|---|---|
| OUTCOME_LEADS | Muốn số điện thoại, email, đăng ký | Sản phẩm bán thẳng giá cao |
| OUTCOME_SALES | Muốn người trả tiền trên web | Trang chưa có giao dịch nào |
| OUTCOME_TRAFFIC | Chỉ muốn người vào xem | Có mục tiêu chuyển đổi rõ ràng |
| OUTCOME_ENGAGEMENT | Tích luỹ tương tác cho bài đăng | Cần lead hoặc đơn hàng |

**Sai lầm tốn kém nhất:** chọn OUTCOME_SALES cho sản phẩm miễn phí. Không có giao dịch nào để Meta học, nó tìm mãi người "sắp mua" trong khi trang chỉ có nút đăng ký.

Trường hợp thật: chiến dịch OUTCOME_SALES chi 11,9 triệu ra 3 lead. Đổi sang OUTCOME_LEADS, giá mỗi lead xuống 12.206đ.

**Lưu ý kỹ thuật:** OUTCOME_SALES bắt buộc phải có pixel trên trang đích. Nếu trang chưa gắn pixel, dùng OUTCOME_TRAFFIC với `LINK_CLICKS` tạm thời.

---

## 2. Chọn sự kiện tối ưu theo giá sản phẩm

| Giá sản phẩm | Mục tiêu | Sự kiện tối ưu | Lý do |
|---|---|---|---|
| Miễn phí | LEADS | `LEAD` | Nhiều dữ liệu, Meta học nhanh |
| Dưới 500k | LEADS | `LEAD` | Vẫn đủ volume |
| 500k – 2tr | SALES | `PURCHASE` | Có đủ giao dịch để học |
| Trên 2tr | SALES | `INITIATE_CHECKOUT` | Purchase quá hiếm |

**Vì sao sản phẩm trên 2 triệu nên tối ưu InitiateCheckout:**

Meta cần ~50 conversion/tuần mỗi adset để thoát learning phase. Với sản phẩm 2 triệu, 50 đơn/tuần = 100 triệu doanh thu/tuần. Không thực tế với phần lớn doanh nghiệp nhỏ.

InitiateCheckout thường nhiều gấp 20-30 lần Purchase. Đủ volume để Meta học, và vẫn gần với hành vi mua.

**Trường hợp sản phẩm chưa bán được đơn nào:**

Vòng luẩn quẩn — không có traffic thì không có đơn, không có đơn thì custom conversion không hoạt động.

Cách thoát: chạy tạm bằng sự kiện chuẩn (`PURCHASE` chung), tích đủ 15-20 giao dịch, rồi tạo campaign mới tối ưu theo custom conversion riêng.

Không sửa campaign cũ — Meta khoá `promoted_object` sau khi publish.

---

## 3. Chọn tệp khách hàng

### Dữ liệu thực chiến

Từ tài khoản chạy liên tục 5 tháng:

| Loại tệp | Giá mỗi lead |
|---|---|
| **Broad + Advantage+ Audience** | **13.442đ** |
| Lookalike 1% | 32.575đ |
| Tệp tương tác (Page, Video) | 38.936đ |

**Broad rẻ hơn Lookalike 2,4 lần.** Lặp lại ở nhiều chiến dịch, không phải ngẫu nhiên.

Lý do: nhắm hẹp = bảo Meta "chỉ tìm trong nhóm này" = cạnh tranh cao = giá đấu tăng. Để rộng = Meta có trăm triệu người để chọn = tìm được người rẻ nhất.

**Điều kiện:** dataset phải đầy đủ. Meta chỉ tự tìm giỏi khi biết khách hàng trông như thế nào.

### Khi nào Broad không phù hợp

- Sản phẩm giá cao (người lạ không trả 5 triệu cho brand mới thấy lần đầu)
- Ngân sách dưới 200k/ngày (không đủ dữ liệu)
- Sản phẩm rất ngách

### Tỷ trọng theo giá

| Giá sản phẩm | Broad | Lookalike | Retarget |
|---|---|---|---|
| Miễn phí | 70% | 30% | — |
| Dưới 1tr | 50% | 30% | 20% |
| 1 – 2tr | 30% | 30% | 40% |
| Trên 2tr | 10% (chỉ để test) | 20% | 70% |

---

## 4. Ngân sách tối thiểu

| Mục đích | Tối thiểu/ngày | Khuyến nghị |
|---|---|---|
| Test một tệp mới | 100k | 150-200k |
| Chạy nghiêm túc thu lead | 300k | 500k-1tr |
| Bán sản phẩm giá cao | 200k | 400-600k |

**Quy tắc chia nhóm:** mỗi nhóm tối thiểu 100k/ngày. Dưới mức đó Meta không đủ dữ liệu.

Có 500k/ngày → tối đa 3-4 nhóm. Đừng chia 8 nhóm mỗi cái 60k.

---

## 5. Cấu trúc chiến dịch

### CBO hay ABO

**ABO (ngân sách cấp nhóm)** — người mới nên dùng.
- Mỗi nhóm có ngân sách riêng
- Mỗi tệp có cơ hội công bằng
- Học được tệp nào tốt

**CBO (ngân sách cấp chiến dịch)** — dùng khi đã biết tệp nào thắng.
- Meta tự phân bổ
- Thường dồn hết vào một nhóm, bỏ quên nhóm khác

### Số lượng

| Cấp | Số lượng khuyến nghị |
|---|---|
| Nhóm mỗi chiến dịch | 3-5 |
| Ads mỗi nhóm | 3-5 |

Ít hơn 3 ads: không có gì để Meta so sánh, mẫu bão hoà là cả nhóm chết.
Nhiều hơn 5: chia loãng, mỗi mẫu không đủ dữ liệu.

### Quy ước đặt tên

```
Chiến dịch:  [Ngày] [Sản phẩm] [Mục tiêu]
             25.08 Khoá AI LEADS ABO

Nhóm:        [Số] [Loại tệp] [Chi tiết]
             N1 Broad AA
             N2 LAL 1pct Purchase
             N3 Retarget Lead 180d

Ads:         [Nhóm] [Góc nội dung]
             N1 tiet kiem chi phi
             N1 nguoi moi bat dau
```

---

## 6. Tư duy phễu

### Vì sao bán thẳng sản phẩm giá cao thường lỗ

| | Bán thẳng cho người lạ | Qua bước miễn phí |
|---|---|---|
| Tỷ lệ mua | ~0,5% | 9,5% |
| Chi phí mỗi đơn | ~3.000.000đ | 590.000đ |
| ROAS | ~1,7 lần | 6,5 lần |

Chênh gần 4 lần. Cùng sản phẩm, cùng ngân sách, khác cách tiếp cận.

### Cấu trúc phễu

```
Quảng cáo tệp rộng  →  Lead magnet miễn phí  →  Sản phẩm chính
   (rẻ, nhiều)          (workshop, ebook)        (giá cao)
```

**Bước 1 — thứ cho không phải có giá trị thật.** Tài liệu ba trang chung chung không làm ai tin bạn hơn.

**Bước 2 — thời điểm mời mua mạnh nhất là ngay cuối buổi học.** Dữ liệu thật: ngày diễn ra workshop mang về gần một nửa doanh thu cả đợt.

**Bước 3 — retarget người dự mà chưa mua.** Tệp nóng nhất, chạy 7-14 ngày sau sự kiện.

### Bài toán đo lường

**Meta không thấy đường đi này.** Người dự workshop nhận link qua Zoom chat hoặc email, mở trực tiếp. Không có dấu vết quảng cáo.

Hệ quả: Meta báo chiến dịch workshop lỗ, trong khi nó chính là nguồn doanh thu lớn nhất.

Trường hợp thật: Meta báo chi 200tr thu 150tr → lỗ 50tr. Đối chiếu hệ thống bán hàng: 1.500 lead từ workshop, 340 người mua khoá chính, doanh thu 1,3 tỷ. ROAS thật 6,5 lần.

**Cách khắc phục:** tạo funnel riêng cho mỗi nguồn, hoặc lưu tham số UTM vào hệ thống bán hàng.

---

## 7. Chạy nhiều chiến dịch cùng lúc

### Đừng tách tài khoản quảng cáo

Nhiều người nghĩ tách tài khoản để hai sản phẩm không đụng nhau. **Ngược lại.**

**Cùng tài khoản:** khi hai nhóm cùng nhắm một người, Meta chỉ đưa MỘT quảng cáo vào phiên đấu giá, tự chọn cái tốt hơn. Không tự đẩy giá.

**Khác tài khoản:** cơ chế đó không áp dụng. Hai tài khoản = hai nhà quảng cáo độc lập = cả hai cùng đấu giá = tự đấu với chính mình.

Cộng thêm: mất lịch sử chi tiêu, learning lại từ đầu, phải share lại pixel và audience.

Chỉ tách khi có lý do vận hành (báo cáo riêng, giao người khác quản lý, cách ly rủi ro).

### Bốn lớp tách

**Lớp 1 — Tách theo phễu, không theo sản phẩm**

| Mức độ | Tệp | Sản phẩm |
|---|---|---|
| Chưa biết | Broad, Lookalike | Miễn phí, giá thấp |
| Đã biết | Lead 180d | Giá trung bình |
| Đã mua | Purchase 180d | Giá cao |

**Lớp 2 — Loại trừ chéo.** Mỗi chiến dịch exclude tệp mà chiến dịch khác đang dùng.

**Lớp 3 — Loại trừ người đã mua.**

**Lớp 4 — Custom conversion riêng cho từng sản phẩm.**

### Số chiến dịch tối đa

**Hai chiến dịch chạy đồng thời** với ngân sách vừa phải.

Ba trở lên: mỗi cái nhận quá ít dữ liệu, không cái nào thoát learning phase.

Mô hình tốt: một chiến dịch thu lead chạy liên tục, một chiến dịch bán hàng chạy theo đợt.
