# Sonny Skills

**Tác giả:** Đặng Hữu Sơn ([sonlovinbot](https://github.com/sonlovinbot))

Bộ skill AI dùng trong khoá đào tạo. Mỗi skill là một thư mục trong `skills/`, cài riêng được, gọi bằng tên hoặc bằng câu nói tự nhiên.

## Danh mục skill

| Skill | Gọi khi bạn muốn | Câu gọi mẫu | Bạn nhận được |
|---|---|---|---|
| [`muse-animated-film`](skills/muse-animated-film) | Làm **phim hoạt hình ngắn** có nhân vật, cốt truyện, chuyển động thật (chạy trên Muse AI) | *"Làm phim hoạt hình 60 giây về cô bé giữ đèn hải đăng"* | Story bible, character sheet, keyframe, video từng cảnh, VO, phim MP4 |
| [`vibe-sketch-video`](skills/vibe-sketch-video) | Làm **video doodle vẽ tay / người que** giải thích một ý tưởng, tóm tắt sách; hoặc chỉ **bộ ảnh doodle** | *"Làm video doodle 60 giây về thói quen thức khuya"* | Kịch bản, lời đọc, bộ prompt, bộ ảnh (có chữ đúng dấu nếu muốn), giọng đọc, video MP4 + phụ đề |
| [`content-ads`](skills/content-ads) | **Lịch content** nhiều tuần, hoặc **một bài quảng cáo** theo khung AIDA / PAS / BAB | *"Lên lịch content 4 tuần cho tiệm bánh"* · *"Viết bài PAS cho khoá học Excel"* | Bảng lịch đăng bài 7 cột, hoặc bài quảng cáo 150–350 từ theo 1 trong 9 giọng văn |
| [`facebook-content-viral`](skills/facebook-content-viral) | **Bài Facebook cá nhân / fanpage** kể trải nghiệm, case study, giới thiệu sản phẩm | *"Viết post Facebook kể trải nghiệm dùng AI làm video"* | Bài đăng theo 3 phong cách, giọng thực chiến |
| [`meta-ads-setup`](skills/meta-ads-setup) | **Dựng, kiểm tra, tối ưu chiến dịch** Facebook/Instagram Ads qua MCP | *"Chạy quảng cáo cho landing page này, ngân sách 300k/ngày"* | Báo cáo tài khoản, chiến dịch dựng sẵn ở trạng thái PAUSED, lịch theo dõi |

### Chọn nhanh khi phân vân

- Video có **nhân vật chuyển động** → `muse-animated-film`. Video **hình vẽ tay tĩnh + giọng đọc** → `vibe-sketch-video`.
- **Một bài bán hàng có khung** → `content-ads`. **Bài chia sẻ cá nhân** → `facebook-content-viral`.
- **Viết chữ cho quảng cáo** → `content-ads`. **Đưa quảng cáo lên chạy** → `meta-ads-setup`.

## Điểm chung của mọi skill

- **Luôn hỏi trước khi làm.** Câu nào bạn đã trả lời thì skill bỏ qua.
- **Văn người viết, không phải văn máy.** Mọi chữ người xem nhìn thấy đều được rà theo [`shared/anti-ai-writing.md`](shared/anti-ai-writing.md): bỏ từ sáo và cấu trúc kiểu AI, nhịp câu so le, chi tiết cụ thể, nhưng vẫn cuốn và thuyết phục.
- **Hai skill video** có 2 chế độ: **duyệt từng phần** (xem và duyệt kịch bản → ảnh → giọng → từng clip → bản cuối) hoặc **chạy luôn** (nhận thẳng MP4). Prompt tạo hình viết bằng tiếng Anh; chữ trên hình, lời thoại, VO giữ nguyên văn theo ngôn ngữ bạn chọn, đủ dấu tiếng Việt.

## Cài đặt

**Claude Code**
```
/plugin marketplace add sonlovinbot-team/sonny-skills
/plugin install sonny-skills@sonny-skills
```
Hoặc copy thư mục skill cần dùng vào `~/.claude/skills/`.

**Claude.ai (web / desktop)** — nén **một thư mục skill** (VD: `skills/content-ads/`) thành `.zip`, vào *Settings → Capabilities → Skills* và upload.

**Muse AI** — copy thư mục skill vào thư mục skills của Muse (VD: `~/workspace/skills/vibe-sketch-video/`), hoặc dán link repo vào chat để Muse tự cài.

**ChatGPT (Custom GPT)** — dán nội dung `SKILL.md` vào ô *Instructions*, upload các file trong `references/` vào *Knowledge*.

## Cấu trúc

```
sonny-skills/
├── .claude-plugin/          # cài như plugin Claude Code
├── shared/
│   └── anti-ai-writing.md   # bản gốc luật chống văn AI
└── skills/
    ├── muse-animated-film/
    ├── vibe-sketch-video/
    ├── content-ads/
    ├── facebook-content-viral/
    └── meta-ads-setup/
```

Mỗi skill tự đủ: `SKILL.md` (agent đọc đầu tiên) + `references/` (đọc khi tới bước cần) + `scripts/` (nếu có).

## Đóng góp / bảo trì

- `shared/anti-ai-writing.md` là bản gốc. Mỗi skill có một bản sao trong `references/` để cài riêng vẫn chạy. Sửa bản gốc xong thì đồng bộ:
  ```bash
  for s in skills/*/; do [ -f "$s/references/anti-ai-writing.md" ] && cp shared/anti-ai-writing.md "$s/references/"; done
  ```
- `scripts/text_overlay.py` có hai bản giống nhau trong `muse-animated-film` và `vibe-sketch-video`; sửa thì sửa cả hai.
- Tên skill viết thường, nối bằng gạch ngang, trùng tên thư mục và trường `name` trong `SKILL.md`.

## Giấy phép

MIT — dùng tự do, ghi credit tác giả khi chia sẻ lại.
