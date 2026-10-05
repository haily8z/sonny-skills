# Dataset, Audience và Custom Conversion

## Mục lục
1. Phân biệt ba khái niệm
2. Kiểm tra sức khoẻ dataset
3. Custom conversion — tạo và dùng
4. Audience — các loại và cách dựng
5. Lookalike — điều kiện và chất lượng
6. Checklist kiểm tra

---

## 1. Phân biệt ba khái niệm

| | Dataset (Pixel) | Audience | Custom Conversion |
|---|---|---|---|
| Trả lời | Chuyện gì đã xảy ra | Ai sẽ thấy quảng cáo | Cái gì tính là thành công |
| Ví dụ | Cuốn sổ ghi chép | Danh sách khách mời | Bút màu đánh dấu |
| Nằm ở | Events Manager | Audiences | Events Manager |
| Cần mấy cái | **Một là đủ** | Càng nhiều càng linh hoạt | Mỗi sản phẩm một cái |

**Không tách dataset theo sản phẩm.** Đây là sai lầm tốn kém.

Tách dataset làm: chia đôi dữ liệu, mất toàn bộ tệp retarget, mất lookalike, cắt đứt đường đi của khách qua nhiều sản phẩm, giảm điểm chất lượng khớp.

Cách đúng: **một dataset, nhiều custom conversion**.

---

## 2. Kiểm tra sức khoẻ dataset

### Bốn thứ cần kiểm tra

**a) Sự kiện có về không**

Kéo dataset stats, xem có dữ liệu trong 24h qua không. Trống = chưa gắn được pixel.

**b) Sự kiện nào đang fire**

Sáu loại quan trọng:

| Sự kiện | Dùng để |
|---|---|
| PageView | Biết ai quan tâm |
| ViewContent | Biết ai quan tâm sâu |
| **Lead** | **Bắt buộc** — tối ưu thu khách |
| InitiateCheckout | Tối ưu sản phẩm giá cao |
| AddToCart | Với bán lẻ |
| **Purchase** | **Bắt buộc** — kèm giá trị |

Thiếu Lead hoặc Purchase = Meta không biết thành công là gì.

**c) Điểm chất lượng khớp (Event Match Quality)**

| Điểm | Nghĩa |
|---|---|
| Dưới 5 | Kém — Meta đoán mò nhiều |
| 5 – 7 | Tạm được |
| Trên 7 | Tốt |
| Trên 9 | Rất tốt |

Điểm thấp thường vì gửi thiếu thông tin. Gửi thêm email và số điện thoại (đã hash) là cách nhanh nhất để tăng.

Sự kiện qua Conversions API thường đạt 9+. Sự kiện browser-side thường 6-7.

**d) Có bị đếm đôi không**

Đặt một đơn thử. Xem Events Manager có một hay hai sự kiện Purchase. Hai = phần khử trùng lặp (`event_id`) chưa đúng.

### Lỗi âm thầm: mất tham số fbclid

**Triệu chứng:** Meta báo rất ít conversion, hệ thống bán hàng báo nhiều gấp nhiều lần.

**Cách kiểm tra:** mở trang đích với `?fbclid=test123` ở cuối URL. Sau khi trang tải xong, nhìn thanh địa chỉ. Nếu tham số biến mất → đúng lỗi này.

**Cách sửa:** báo người làm web giữ nguyên query string khi chuyển hướng.

### Lưu ý khi đọc tracking_config qua API

`tracking_config: null` **không** có nghĩa là chưa gắn pixel. Nó có nghĩa là "không có cấu hình riêng cho funnel này, dùng dataset mặc định toàn hệ thống".

Nhiều nền tảng tự gắn pixel mặc định cho mọi trang. Kiểm tra bằng dataset stats thay vì đọc config.

---

## 3. Custom conversion

### Khi nào cần

Khi một dataset nhận nhiều loại giao dịch với giá trị khác nhau.

Ví dụ: bán workshop 99k, ebook 990k, khoá học 5tr. Meta nhìn vào thấy "100 lần Purchase" nhưng không biết cái nào là cái nào. Chạy quảng cáo khoá 5tr thì nó đi tìm người giống... người mua 99k, vì nhóm đó đông hơn.

### Cách tạo

Events Manager → Custom Conversions → Create.

| Trường | Giá trị |
|---|---|
| Data source | Dataset đang dùng |
| Action Source | Website |
| Event | Purchase hoặc Lead |
| Name | `[Loại sự kiện] [Tên sản phẩm]` |
| Rule | **URL contains `<slug-sản-phẩm>`** |
| Conversion value | **Bỏ tick** |

### Vì sao lọc theo URL, không lọc theo giá trị

| | Lọc theo Value | Lọc theo URL |
|---|---|---|
| Đổi giá sản phẩm | ❌ rule chết | ✅ vẫn chạy |
| Chạy khuyến mãi | ❌ đơn giảm giá rơi sai nhóm | ✅ đúng |
| Một funnel nhiều gói giá | ❌ lẫn lộn | ✅ gom đúng funnel |

### Vì sao bỏ tick Conversion value

Trường này **ghi đè** giá trị pixel gửi lên. Nhập 990000 thì mọi conversion khớp rule đều tính 990.000đ, bất kể thực tế thu bao nhiêu.

Chỉ nhập khi pixel **không** gửi giá trị.

### Cạm bẫy: rule mâu thuẫn AND

Mỗi lần bấm **Add Rule** tạo một điều kiện nối bằng **AND**.

Thêm hai dòng URL:
```
Lead
AND URL chứa "workshop-a"
AND URL chứa "workshop-b"
```
Một URL không thể vừa là A vừa là B → không bao giờ đúng → custom conversion vĩnh viễn trống.

Muốn OR: bấm dấu **+** trong cùng một dòng. Nhưng thường tách hai custom conversion riêng còn tốt hơn.

### Custom conversion không hồi tố

Chỉ tính từ lúc tạo trở đi. Mới tạo thì "Never received event" là bình thường.

Cần vài giờ đến một ngày tích dữ liệu trước khi dùng làm mục tiêu tối ưu.

### Đặt tên có hệ thống

```
Purchase Workshop AI Marketing
Purchase Ebook Vibe Code
Purchase Bootcamp
Lead Workshop AI Marketing
Lead Ebook Vibe Code
```

Meta cho 100 custom conversion mỗi tài khoản.

---

## 4. Audience

### Bốn loại

**Website Custom Audience** — từ dữ liệu pixel. Tự cập nhật hàng ngày.

**Customer List** — tải file email/SĐT lên. Đứng yên, phải cập nhật thủ công, tỷ lệ khớp 60-80%.

**Engagement** — người tương tác Page, xem video, follow.

**Lookalike** — người giống một nguồn có sẵn.

### Ba tệp nên có sẵn

| Tệp | Quy tắc | Dùng để |
|---|---|---|
| Đã để lại thông tin | event = Lead, 180 ngày | Retarget chính |
| Đã mua | event = Purchase, 180 ngày | Loại trừ + nguồn lookalike |
| Đã xem trang bán chưa mua | URL contains `<slug>`, exclude Purchase, 30 ngày | Tệp nóng nhất |

Ba tệp này Meta tự cập nhật, không cần làm gì thêm.

### Đọc quy mô tệp

Meta đã đổi cách hiển thị: **lookalike không còn báo quy mô trong danh sách Audiences**, chỉ hiện khi tạo adset.

Con số 1.000 mà API trả về là giá trị mặc định, **không phải dấu hiệu thất bại**. Đừng kết luận tệp hỏng chỉ vì thấy số này.

Cách kiểm tra thật: tạo thử một adset và chọn tệp đó, Meta sẽ hiện ước tính.

### Tệp quá nhỏ

Dưới vài nghìn người thì adset gần như không phân phối. Gộp với tệp khác hoặc chuyển sang Broad.

---

## 5. Lookalike

### Điều kiện

| | Yêu cầu |
|---|---|
| Nguồn tối thiểu | 100 người |
| Nguồn khuyến nghị | 1.000 – 50.000 |
| Thời gian dựng | 2-6 giờ, có khi lâu hơn |

Nguồn 20-50 người thì Meta không dựng được, tệp đứng yên vĩnh viễn.

### Chất lượng nguồn

Xếp từ tốt đến kém:

1. **Người đã trả tiền** — đã chứng minh chịu mở ví
2. **Người đã để lại thông tin** — đã hành động
3. **Người xem video 50%+** — đã xem nội dung sâu
4. **Người tương tác Page** — chỉ bấm like, ý định thấp

### Không tạo lookalike từ lookalike

Meta từ chối. Cần nguồn gốc là custom audience thật.

### Độ rộng

1% hẹp nhất và giống nhất. Bắt đầu từ 1%. 3% và 5% rộng hơn nhưng loãng hơn.

---

## 6. Checklist kiểm tra

```
DATASET
□ Có dữ liệu trong 24h qua
□ Sự kiện Lead đang fire
□ Sự kiện Purchase đang fire (nếu bán hàng)
□ Điểm chất lượng khớp trên 7
□ Không bị đếm đôi
□ Trang đích giữ được tham số fbclid

CUSTOM CONVERSION
□ Sản phẩm này đã có nhãn riêng
□ Rule lọc theo URL, không theo value
□ Đã bỏ tick Conversion value
□ Nhãn đã nhận được dữ liệu (nếu dùng làm mục tiêu tối ưu)
□ Rule không có hai điều kiện URL nối AND

AUDIENCE
□ Có tệp Lead 180 ngày
□ Có tệp Purchase 180 ngày (để loại trừ)
□ Có tệp người xem trang bán chưa mua
□ Không tệp nào dưới 1.000 người

LOOKALIKE
□ Nguồn có ít nhất 1.000 người
□ Nguồn là người đã hành động, không phải người like
□ Đã dựng xong (kiểm tra bằng cách tạo thử adset)
```
