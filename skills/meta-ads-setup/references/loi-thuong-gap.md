# Lỗi thường gặp

## Bảng tra nhanh

| Triệu chứng | Lỗi số |
|---|---|
| Không publish được, báo lỗi vị trí Việt Nam | 1 |
| Mọi thao tác tạo/sửa đều báo Permission Error | 2 |
| Không đổi được pixel hoặc sự kiện tối ưu | 3 |
| Custom conversion báo chưa hoạt động | 4 |
| Custom conversion mãi không nhận dữ liệu | 5 |
| Adset bật mà không tiêu tiền | 6 |
| Meta báo ít conversion hơn thực tế nhiều | 7 |
| Chi phí tăng dần không rõ lý do | 8 |
| Ads hiện Instant Form thay vì dẫn sang web | 9 |
| Không tải được ảnh lên | 10 |

---

## LỖI 1 — Không publish được vì vị trí Việt Nam

### Triệu chứng

```
Update your location targeting: We have removed the location 
targeting option (people living in, people travelling in or people 
recently in a location). (#1870194)
```

Hoặc: `Invalid Geo Locations for ads (#1487478)`

### Nguyên nhân

Meta đã bỏ `location_types` (living in / travelling in / recently in). Nhưng khi adset tạo qua API, Meta **tự động chèn lại** giá trị mặc định `["frequently_in", "home"]`.

Giao diện web dùng bộ kiểm tra mới, nghiêm hơn API, phát hiện trường cũ này và chặn publish.

**Điểm gây nhầm:** sửa qua API báo thành công nhưng Meta vẫn chèn lại. Nhìn API thấy sạch, mở giao diện lại thấy lỗi.

### Cách sửa — chỉ làm được trong giao diện

Làm từng adset một, **không bulk-edit**:

```
1. Mở adset → Edit
2. Vào phần Location (Vị trí)
3. Chọn chế độ Browse (Duyệt)
4. Country → Asia
5. BỎ TICK Vietnam
6. Gõ lại "Vietnam" vào ô tìm kiếm
7. Chọn Vietnam từ kết quả
8. Publish
```

Bản chất: bỏ chọn rồi chọn lại buộc Meta ghi lại cấu hình theo định dạng mới.

### Phòng tránh

Khi tạo adset qua API, chỉ dùng:
```json
"geo_locations": { "countries": ["VN"] }
```

Không thêm `location_types`. Nhưng vẫn có thể bị chèn lại.

### Lưu ý

**Lỗi này chỉ chặn thao tác sửa, không chặn quảng cáo đang chạy.** Nếu adset đã ACTIVE và phân phối bình thường, không cần vội sửa.

---

## LỖI 2 — Tài khoản bị khoá quyền ghi

### Triệu chứng

```
Permission Error: Either the object you are trying to access is not 
visible to you or the action you are trying to take is restricted 
to certain account types.
```

Mã: `100`, subcode `1487194`

Đọc dữ liệu vẫn bình thường. Upload ảnh vẫn được. Chỉ tạo creative, tạo ad, sửa adset bị chặn.

### Nguyên nhân

Phần lớn là **số dư chưa thanh toán**. Meta khoá quyền ghi cho đến khi trả xong.

Khác: tài khoản chưa vào Business Manager, chưa xác minh danh tính, đang bị xét duyệt chính sách.

### Cách xử lý

```
1. Billing → có nút "Pay now" không
2. Account Quality → có hạn chế nào đang hiệu lực
3. Thanh toán xong thử lại — thường thông trong vài phút
```

### Cách chẩn đoán nhanh

Thử một thao tác đọc (list campaigns). Nếu đọc được mà ghi không được → đúng lỗi này.

---

## LỖI 3 — Không sửa được pixel/sự kiện sau publish

### Triệu chứng

```
Can't Make Edits to Published Ad Set: You can't edit your pixel, 
conversion event, custom conversion or optimization for an ad set 
after the ad set is published.
```

Mã: `100`, subcode `3260011`

### Nguyên nhân

Meta khoá vĩnh viễn bốn thứ sau khi adset publish: pixel, conversion event, custom conversion, optimization goal.

### Cách xử lý

Không có cách sửa. Tạo adset mới với cấu hình đúng, gắn lại creative, tắt adset cũ.

### Phòng tránh

**Quyết định sự kiện tối ưu TRƯỚC khi tạo adset.** Đây là quyết định không đảo ngược.

Nếu chưa chắc, tạo adset nháp với ngân sách tối thiểu để kiểm tra, rồi mới tạo bản chính.

---

## LỖI 4 — Custom conversion báo chưa hoạt động

### Triệu chứng

```
Your custom conversion isn't active. We haven't received activity 
from this custom conversion yet.
```

### Nguyên nhân

Custom conversion mới tạo chưa nhận sự kiện nào. **Không hồi tố** — chỉ tính từ lúc tạo.

### Cách xử lý

**Sản phẩm đã có giao dịch:** chờ vài giờ đến một ngày.

**Sản phẩm chưa bán được đơn nào:** vòng luẩn quẩn. Cách thoát — chạy tạm bằng sự kiện chuẩn, tích 15-20 giao dịch, rồi tạo campaign mới dùng custom conversion.

Không sửa campaign cũ (xem Lỗi 3).

---

## LỖI 5 — Custom conversion mãi không nhận dữ liệu

### Triệu chứng

Tạo xong nhưng vĩnh viễn trống, dù sản phẩm vẫn bán được.

### Nguyên nhân

Mỗi lần bấm **Add Rule** tạo một điều kiện nối bằng **AND**.

Hai dòng URL:
```
Lead
AND URL chứa "workshop-a"
AND URL chứa "workshop-b"
```

Một URL không thể vừa là A vừa là B → không bao giờ đúng.

### Cách sửa

Muốn OR: bấm dấu **+** trong cùng một dòng, không bấm Add Rule.

Thường tách hai custom conversion riêng còn tốt hơn.

---

## LỖI 6 — Adset bật mà không tiêu tiền

### Nguyên nhân thường gặp

| Nguyên nhân | Cách kiểm tra |
|---|---|
| Tệp quá nhỏ | Xem quy mô trong Ads Manager |
| Chỉ còn một ad trong nhóm | Đếm số ads |
| Lookalike chưa dựng xong | Chờ 2-6 giờ |
| Không đủ tín hiệu để tối ưu | Xem dataset có sự kiện không |
| Ngân sách quá thấp so với tệp | So ngân sách với quy mô tệp |

### Cách xử lý

Tệp nhỏ → gộp với tệp khác hoặc chuyển sang Broad.

Một ad → thêm 2-3 cái nữa.

---

## LỖI 7 — Meta báo ít conversion hơn thực tế

### Triệu chứng

Hệ thống bán hàng báo 100 đơn, Meta chỉ báo 20.

### Nguyên nhân

Trang đích làm mất tham số `fbclid` khi tải. Meta không nối được đơn hàng với lượt bấm.

Thường do trang chuyển hướng mà không giữ query string.

### Cách kiểm tra

Mở trang đích với `?fbclid=test123` ở cuối URL. Sau khi trang tải xong, nhìn thanh địa chỉ.

Nếu tham số biến mất → đúng lỗi này.

### Cách sửa

Báo người làm web giữ nguyên toàn bộ query string khi chuyển hướng.

### Lưu ý

Một phần chênh lệch là **bình thường** — traffic tự nhiên cũng tạo đơn. Xem cách phân biệt ở `phan-tich.md` mục 4.

---

## LỖI 8 — Chi phí tăng dần không rõ lý do

### Triệu chứng

Tuần đầu 100k/lead. Tuần thứ ba 200k/lead. Không đổi gì cả.

### Nguyên nhân

Tần suất tăng. Cùng nhóm người thấy đi thấy lại, hết phản ứng.

### Cách kiểm tra

Xem cột tần suất. Trên 2,5 là dấu hiệu rõ.

### Cách xử lý

Thay creative mới với góc nội dung khác. Không phải sửa cái cũ — Meta không cho sửa.

Hoặc mở rộng tệp.

---

## LỖI 9 — Ads hiện Instant Form thay vì dẫn sang web

### Triệu chứng

Preview quảng cáo hiện form Facebook thay vì nút dẫn sang trang.

### Nguyên nhân

Adset không set `destination_type`. Với campaign OUTCOME_LEADS, Meta mặc định Instant Form.

### Cách xử lý

Set `destination_type: "WEBSITE"` khi tạo adset.

Nếu adset đã publish, thử sửa — trường này đôi khi sửa được (khác với pixel và optimization goal).

### Phòng tránh

Luôn set `destination_type` rõ ràng, đừng để mặc định.

---

## LỖI 10 — Không tải được ảnh lên

### Triệu chứng

```
Image Wasn't Downloaded: Your image couldn't be downloaded. 
Please wait a few minutes and try again.
```

Mã: `100`, subcode `2446511`

### Nguyên nhân

CDN chứa ảnh chặn khi Meta tải nhiều lần liên tiếp. Thường xảy ra khi tạo nhiều creative dùng cùng `image_url` trong thời gian ngắn.

### Cách xử lý

**Upload ảnh trước, lấy `image_hash`, rồi dùng hash** thay vì dán `image_url` trực tiếp.

Cách này vừa tránh lỗi, vừa nhanh hơn, vừa để ảnh trong thư viện tài khoản để tái sử dụng.

---

## Nguyên tắc chung khi gặp lỗi

**Đọc kỹ mã lỗi và subcode.** Chúng cho biết chính xác vấn đề, khác với thông báo chung chung.

**Thử một thao tác đọc trước.** Nếu đọc được mà ghi không được → vấn đề ở quyền, không phải tham số.

**Đừng retry mù nhiều lần.** Nếu sai tham số, retry vẫn sai. Đọc lỗi rồi sửa.

**Lỗi timeout khác lỗi validation.** Timeout nghĩa là request đã gửi đi và có thể đã thực hiện — kiểm tra trước khi thử lại, tránh tạo trùng.
