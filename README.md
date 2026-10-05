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

### Chọn nhanh

| Bạn dùng | Cách nhanh nhất | Cài hết 5 skill một lần? |
|---|---|---|
| **Claude Code** (terminal, VS Code, desktop) | Plugin marketplace | ✅ |
| **Codex** (CLI / app) | Plugin marketplace | ✅ |
| **Nhiều agent cùng lúc** (Claude Code, Codex, Cursor, OpenCode…) | `npx skills` | ✅ |
| **ChatGPT** (web / desktop / mobile) | Upload file zip từng skill | ❌ mỗi skill một lần upload (workspace Business/Enterprise: admin đồng bộ cả repo, xem bên dưới) |
| **Claude.ai** (web / desktop / mobile) | Upload file zip từng skill | ❌ mỗi skill một lần upload |
| **Muse AI** | Copy thư mục / dán link repo | Tuỳ cách |

### Claude Code — cài hết bằng plugin

Gõ trong Claude Code:
```
/plugin marketplace add sonlovinbot-team/sonny-skills
/plugin install sonny-skills@sonny-skills
```
Cả 5 skill được cài cùng lúc. Gọi bằng câu nói tự nhiên, hoặc gọi tên: `/sonny-skills:content-ads`, `/sonny-skills:vibe-sketch-video`…

Cập nhật bản mới: `/plugin marketplace update sonny-skills`.

### Codex (CLI / app) — cài hết bằng plugin

```bash
codex plugin marketplace add sonlovinbot-team/sonny-skills
```
Rồi mở Codex, gõ `/plugins`, chọn tab **Sonny Skills** → cài **sonny-skills**. Khởi động lại Codex nếu skill chưa hiện. Gọi bằng câu nói tự nhiên hoặc `@sonny-skills`.

### Mọi agent — cài hết bằng `npx skills`

Cần Node.js. Một lệnh cài cả 5 skill vào các agent trên máy (Claude Code, Codex, Cursor, OpenCode…):
```bash
npx skills add sonlovinbot-team/sonny-skills --all -g
```
- Chỉ cài cho một agent: thêm `-a claude-code` hoặc `-a codex`.
- Chỉ cài vài skill: `npx skills add sonlovinbot-team/sonny-skills -s content-ads -s vibe-sketch-video -g`
- Xem danh sách trước khi cài: `npx skills add sonlovinbot-team/sonny-skills --list`
- Bỏ `-g` để cài vào dự án đang mở thay vì toàn máy.

### ChatGPT (web / desktop / mobile)

**Tài khoản cá nhân** — upload từng skill:
1. Tải file zip của skill cần dùng:
   [muse-animated-film.zip](https://github.com/sonlovinbot-team/sonny-skills/releases/latest/download/muse-animated-film.zip) ·
   [vibe-sketch-video.zip](https://github.com/sonlovinbot-team/sonny-skills/releases/latest/download/vibe-sketch-video.zip) ·
   [content-ads.zip](https://github.com/sonlovinbot-team/sonny-skills/releases/latest/download/content-ads.zip) ·
   [facebook-content-viral.zip](https://github.com/sonlovinbot-team/sonny-skills/releases/latest/download/facebook-content-viral.zip) ·
   [meta-ads-setup.zip](https://github.com/sonlovinbot-team/sonny-skills/releases/latest/download/meta-ads-setup.zip)
2. Trong ChatGPT: **Skills → Create → Upload from your computer** → chọn file zip.
3. Chờ ChatGPT quét xong là dùng được. Lặp lại cho skill khác.

**Workspace Business / Enterprise** — admin có thể nhập và đồng bộ cả repo này như một marketplace plugin cho cả team (repo đã có sẵn `.agents/plugins/marketplace.json`). Sau đó thành viên vào tab **Plugins**, tìm **Sonny Skills**, bấm **+** để cài hết 5 skill một lần.

Gọi skill: gõ `@` rồi chọn skill, hoặc nói tự nhiên ("lên lịch content 4 tuần cho tiệm bánh").

### Claude.ai (web / desktop / mobile)

1. Tải file zip của skill cần dùng (cùng các link ở mục ChatGPT phía trên).
2. Vào **Customize → Skills** → **+** → **Create skill** → **Upload a skill** → chọn file zip.
3. Bật skill trong danh sách. Lặp lại cho skill khác.

Cần bật *Code execution* trong cài đặt. Gói Team / Enterprise: owner có thể upload một lần cho cả tổ chức trong *Organization settings*.

### Muse AI

Dán link repo vào chat và nhờ Muse cài, hoặc copy **từng thư mục** trong `skills/` vào thư mục skills của Muse (VD: `~/workspace/skills/vibe-sketch-video/`). Không copy nguyên repo vào một thư mục, vì skill nằm sâu một tầng trong `skills/` sẽ không được nhận.

### Cài tay (mọi công cụ hỗ trợ SKILL.md)

Copy thư mục skill (nguyên cả `references/`, `scripts/`) vào thư mục skills của công cụ, VD Claude Code: `~/.claude/skills/<tên-skill>/`.

## Cấu trúc

```
sonny-skills/
├── .claude-plugin/          # marketplace + plugin cho Claude Code
├── .agents/plugins/         # marketplace cho Codex / ChatGPT
├── plugin.json              # manifest plugin chuẩn Agent Plugins (Codex / ChatGPT)
├── tools/build-zips.sh      # đóng gói mỗi skill thành zip để upload
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
- Phát hành bản mới: tăng `version` trong `plugin.json` và `.claude-plugin/plugin.json`, chạy `bash tools/build-zips.sh`, rồi tạo GitHub Release đính kèm các file trong `dist/` (link tải ở README luôn trỏ tới release mới nhất):
  ```bash
  gh release create v1.0.1 dist/*.zip --title "v1.0.1" --notes "..."
  ```
- Tên skill viết thường, nối bằng gạch ngang, trùng tên thư mục và trường `name` trong `SKILL.md`.

## Giấy phép

MIT — dùng tự do, ghi credit tác giả khi chia sẻ lại.
