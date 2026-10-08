# Cách đăng bài cho báo Sân Cỏ

Trang báo chạy miễn phí trên GitHub Pages. Bài viết được lưu thành tệp Markdown trong repo; khi cập nhật lên nhánh main, GitHub Actions dựng lại website và xuất bản.

## Tạo bài mới bằng GitHub

1. Mở thư mục [site/_posts](https://github.com/haily8z/sonny-skills/tree/main/site/_posts).
2. Chọn **Add file → Create new file**.
3. Đặt tên theo mẫu **YYYY-MM-DD-ten-bai-viet.md**, ví dụ **2026-10-09-ten-bai-viet.md**.
4. Dán phần đầu bài mẫu bên dưới, rồi thay nội dung.
5. Chọn **Commit changes** trên nhánh main.
6. Mở tab **Actions** và chờ quy trình **Build and deploy Sân Cỏ + Muse Animated Film** hoàn tất. Bài sẽ hiện tại [trang báo](https://haily8z.github.io/sonny-skills/the-thao/).

~~~yaml
---
title: "Tiêu đề bài viết"
date: 2026-10-09 09:00:00 +0700
category: "Bóng đá"
sport: football
author: "Tên tác giả"
reading_time: "4 phút đọc"
excerpt: "Một câu giới thiệu ngắn hiển thị trên trang chủ."
---
~~~

## Viết nội dung

Sau dấu --- cuối phần thông tin, viết bài bằng Markdown:

- ## Tiêu đề phụ để chia phần.
- **chữ đậm** để nhấn ý.
- > đoạn trích để tạo câu dẫn.
- Dòng trắng để bắt đầu đoạn mới.

Chọn sport để bài vào đúng bộ lọc: **football** (Bóng đá), **basketball** (Bóng rổ), hoặc **tennis**. Trường category là nhãn bài hiển thị, có thể ghi như **Bóng đá**, **Chiến thuật**, **Bóng rổ** hoặc **Tennis**. Để bài xuất hiện đúng thứ tự, ngày trong tên tệp và trường date nên trùng nhau.

## Sửa hoặc gỡ bài

- **Sửa:** mở tệp bài viết trong GitHub, bấm biểu tượng cây bút, chỉnh nội dung rồi commit.
- **Gỡ:** xóa tệp bài viết trong GitHub. Thay đổi sẽ xuất bản sau khi Actions chạy xong.

Tất cả nội dung trong repo này là công khai. Chỉ commit bài đã sẵn sàng xuất bản. Nếu đang chuẩn bị bài, hãy soạn trên máy trước rồi mới commit lên main.

## Bài mẫu

Các bài đang có trên trang được đánh dấu **Bài mẫu**. Khi thay một bài mẫu bằng bài thật, bỏ dòng demo: true trong phần thông tin đầu bài. Bài mẫu là nội dung minh họa, không phải tin thời sự.

## Ảnh

Bản đầu tiên dùng hình minh họa chung trên trang chủ. Muốn thêm ảnh bài, tải ảnh lên thư mục site/assets/articles/ trong repo rồi thêm đường dẫn vào phần thông tin:

~~~yaml
image: "/assets/articles/ten-anh.jpg"
image_alt: "Mô tả ngắn nội dung ảnh"
~~~

Tránh tải ảnh không có quyền sử dụng.
