# Câu hỏi thảo luận - Lab 02

### 1. Vì sao phải đồng bộ `master` trước khi gửi Pull Request?
- **Phát hiện và xử lý sớm xung đột (Conflict Resolution):** Trong môi trường làm việc song song, các thành viên khác có thể đã merge code của họ vào `master`. Nếu không kéo `master` mới về trước, PR có thể bị conflict trên GitHub và không thể tự động merge.
- **Ngăn ngừa lỗi tích hợp âm thầm (Semantic Conflict):** Dù Git không báo xung đột dòng lệnh (syntactic conflict), việc chạy code tính năng mới trên nền tảng `master` đã cũ có thể gây lỗi logic khi tích hợp chung. Đồng bộ trước giúp lập trình viên kiểm thử toàn bộ hệ thống (`python main.py`) ngay trên môi trường cục bộ để đảm bảo tính ổn định trước khi đưa lên CCB duyệt.

---

### 2. Khi nào không được phép dùng `rebase`?
- **Nguyên tắc vàng của Rebase (The Golden Rule of Rebase):** Tuyệt đối không rebase trên các nhánh công khai/đã chia sẻ (public branches) như `master`, `main`, `release/*` hoặc nhánh mà nhiều người đang cùng làm việc.
- **Lý do:** Lệnh rebase sẽ viết lại lịch sử commit (tạo các mã băm SHA mới và thay đổi commit cha). Nếu rebase trên nhánh đã đẩy lên remote mà người khác đã kéo về, lịch sử của họ sẽ bị phân kỳ (diverged), gây ra xung đột dây chuyền và phá vỡ tính toàn vẹn của lịch sử SCM.
- Rebase chỉ nên dùng trên các nhánh tính năng cục bộ (local private feature branch) của cá nhân trước khi mở PR để làm sạch và tuyến tính hóa commit history.

---

### 3. Nhánh `feature/*` khác nhánh `topic/*` ra sao?
- **`feature/*` (Feature branch):** Dùng để phát triển một tính năng nghiệp vụ cụ thể của phần mềm trực tiếp phục vụ người dùng cuối (ví dụ: `feature/cart-print`, `feature/search-by-title`). Nhánh này tác động trực tiếp đến mã nguồn logic của sản phẩm.
- **`topic/*` (Topic branch):** Thường dùng cho các chủ đề ngắn hạn, công việc phụ trợ, kỹ thuật hoặc tài liệu mà không phải là một tính năng nghiệp vụ người dùng (ví dụ: `topic/pr-template`, `topic/use-case-diagram`, `topic/ci-pipeline`).
