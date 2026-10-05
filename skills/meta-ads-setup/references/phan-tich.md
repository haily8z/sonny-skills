# Phân tích số liệu

## Mục lục
1. Năm chỉ số cần nhìn
2. Outbound CTR — chỉ số đáng tin nhất
3. Tần suất
4. Số Meta khác số thật
5. Learning phase
6. Lịch tối ưu
7. Mẫu báo cáo

---

## 1. Năm chỉ số cần nhìn

Ads Manager có hơn 40 cột. Năm chỉ số này đủ để ra quyết định:

| Chỉ số | Nghĩa | Ngưỡng |
|---|---|---|
| Chi phí | Đã tiêu bao nhiêu | — |
| Kết quả | Được bao nhiêu khách | — |
| Chi phí mỗi kết quả | Mỗi khách tốn bao nhiêu | Tuỳ ngành |
| **Tần suất** | Mỗi người thấy mấy lần | Dưới 2,5 |
| **Outbound CTR** | Bao nhiêu người thật sự sang trang | Trên 1% |

---

## 2. Outbound CTR — chỉ số đáng tin nhất

**Khác với CTR thông thường.** CTR tính cả người bấm vào ảnh để phóng to, bấm tên page, bấm "xem thêm". Những cái đó không phải ý định thật.

Outbound clicks = số người rời Facebook sang trang của bạn. Đây mới là ý định thật.

**Vì sao quan trọng:** khi tracking có vấn đề, số "kết quả" không đáng tin. Nhưng outbound clicks vẫn đúng vì Meta đo ngay trên nền tảng nó.

**Trường hợp thật:** một mẫu có CTR 3,57% trông tốt, nhưng outbound CTR chỉ 0,51%. Người ta bấm rồi không đi tiếp — bấm nhầm hoặc tò mò. Mẫu đó đã bị tắt.

**Cách dùng khi đánh giá:** khi chưa có đủ conversion để so, dùng outbound CTR làm proxy. Mẫu nào đưa nhiều người sang trang nhất với chi phí thấp nhất là mẫu đang thắng.

---

## 3. Tần suất

| Mức | Nghĩa |
|---|---|
| Dưới 1,5 | Tốt, tệp còn rộng |
| 1,5 – 2,5 | Bình thường |
| 2,5 – 3,5 | Bắt đầu bão hoà, chuẩn bị mẫu mới |
| Trên 3,5 | Tệp đã cạn, phải thay mẫu hoặc mở rộng tệp |

**Tần suất là dấu hiệu sớm nhất báo chi phí sắp tăng.** Thấy vượt 2,5 thì chuẩn bị ngay, đừng chờ đến khi chi phí tăng.

**Cách xử lý:** thay creative mới với góc nội dung khác. Không phải sửa cái cũ — Meta không cho sửa.

---

## 4. Số Meta khác số thật

### Vì sao chênh

Meta chỉ tính conversion mà nó nối được với một lượt bấm quảng cáo. Hệ thống bán hàng tính tất cả đơn, bất kể từ đâu.

Phần chênh gồm: khách từ nguồn tự nhiên, khách được giới thiệu, và khách từ quảng cáo nhưng mất dấu theo dõi.

### Trường hợp đáng nhớ

Meta báo: chi 8,5 triệu, doanh thu ghi nhận 6 triệu → **lỗ 2,5 triệu**.

Đối chiếu hệ thống bán hàng: quảng cáo mang về 333 lead cho workshop. Cuối buổi, những người này nhận link mua bootcamp. Hai tuần sau: 34 người mua, doanh thu 55,9 triệu.

**ROAS thật: 6,6 lần.**

Nếu tin số Meta, doanh nghiệp đó đã tắt chiến dịch sinh lời tốt nhất.

### Cách đối chiếu đúng

**Đừng so chi phí quảng cáo với doanh thu Meta báo.**

So chi phí quảng cáo với **doanh thu thật trong hệ thống của user**, cùng khoảng thời gian.

Nếu bán qua nhiều bước (workshop rồi mới bán khoá) thì phải tính cả doanh thu ở bước sau.

### Cách phân biệt lead từ quảng cáo và lead tự nhiên

So `outbound_clicks` (Meta) với `landing_views` (hệ thống bán hàng).

Ví dụ: outbound 1.261, landing views 2.462 → quảng cáo mang về ~51% traffic, còn lại là tự nhiên.

**Đừng chia toàn bộ chi phí cho toàn bộ lead** — sẽ ra CPL đẹp giả.

---

## 5. Learning phase

### Con số 50

Meta cần khoảng **50 kết quả trong 7 ngày** mỗi adset để thoát learning phase.

**Điểm hay hiểu sai:** con số này tính ở **cấp nhóm**, không phải cấp chiến dịch. Chia 5 nhóm thì mỗi nhóm cần 50, tổng 250.

Đây là lý do chia quá nhiều nhóm là sai lầm.

### Với sản phẩm giá cao

Sản phẩm 2 triệu, 50 đơn/tuần = 100 triệu doanh thu/tuần. Không thực tế.

**Nghĩa là chiến dịch bán hàng giá cao sẽ luôn ở trong learning phase.** Không tránh được.

Cách xử lý: dùng tệp nhỏ và chính xác — chất lượng tệp làm phần việc mà thuật toán không làm được. Hoặc tối ưu theo InitiateCheckout thay vì Purchase.

### Điều gì reset learning

- Đổi ngân sách quá 20%
- Đổi tệp khách hàng
- Đổi sự kiện tối ưu
- Thêm hoặc đổi quảng cáo trong nhóm

**Lỗi phổ biến nhất của người mới:** sốt ruột nên ngày nào cũng vào chỉnh. Mỗi lần chỉnh là bắt đầu lại. Ba tuần trôi qua, chiến dịch vẫn ở ngày đầu.

### Khi nào bỏ qua quy tắc 20%

- Chiến dịch sắp kết thúc (còn 1-2 ngày trước sự kiện)
- Ngày cuối chương trình khuyến mãi

Ngoài hai trường hợp này, giữ nguyên quy tắc.

---

## 6. Lịch tối ưu

| Thời điểm | Việc |
|---|---|
| Ngày 1-3 | **Không động vào.** Chỉ theo dõi |
| Ngày 4-6 | Tắt nhóm chi trên 500k mà không có tín hiệu nào |
| Ngày 7-10 | Tăng ngân sách nhóm thắng, mỗi lần ≤20% |
| Ngày 11+ | Theo dõi tần suất, thay creative khi vượt 2,5 |

### Ba ngày đầu số liệu sẽ xấu

Chi phí mỗi khách cao gấp đôi kỳ vọng. Có nhóm chưa tiêu hết ngân sách. Đó là bình thường.

Nhìn nhưng đừng sửa.

### Tiêu chí tắt nhóm

Nhóm nào chi trên 500k mà **0 tín hiệu chuyển đổi** trong 3 ngày → tắt.

Nhóm có tín hiệu nhưng chưa ra đơn → giữ, vấn đề nằm ở trang bán không phải ở tệp.

---

## 7. Mẫu báo cáo

### Báo cáo hàng ngày

```
HÔM NAY ([ngày])

Chi: [số]đ / [ngân sách]đ
Kết quả: [số] — giá [số]đ

NHÓM TỐT NHẤT
[tên] — [số] kết quả, giá [số]đ

NHÓM CẦN CHÚ Ý
[tên] — [vấn đề cụ thể]

CẦN LÀM
- [hành động 1]
```

### Báo cáo tổng kết chiến dịch

```
TỔNG KẾT [tên chiến dịch]

| Chỉ số | Meta báo | Thực tế |
|---|---|---|
| Chi phí | [số] | — |
| Kết quả | [số] | [số từ hệ thống] |
| Giá mỗi kết quả | [số] | [số] |
| Doanh thu | [số] | [số] |

SO VỚI MỤC TIÊU
[mục tiêu] → [đạt được] — [đạt/không đạt]

BÀI HỌC
1. [rút ra từ dữ liệu]
2. [...]

ĐỀ XUẤT ĐỢT SAU
- [...]
```

### Nguyên tắc viết báo cáo

**Đưa số trước, nhận xét sau.** Đừng nói "hiệu quả tốt" mà không kèm con số.

**Nói rõ độ tin cậy.** Nếu tracking có vấn đề, nói ra trước khi đưa kết luận.

**Chỉ ra hành động cụ thể.** "Cần tối ưu thêm" là vô nghĩa. "Tắt nhóm N3, dồn 150k sang N1" mới dùng được.

**Không giấu tin xấu.** Nếu chiến dịch lỗ, nói thẳng kèm số.
