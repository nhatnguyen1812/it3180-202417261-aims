# Câu hỏi thảo luận - Lab 04

### 1. Vì sao chuẩn bị phát hành trên `master` trước thay vì sửa trực tiếp trên nhánh `release/*`?
- **Nguyên tắc "Thượng nguồn trước" (Upstream First):** Nhánh `master` đại diện cho dòng phát triển chính. Việc cập nhật phiên bản, CHANGELOG và kiểm thử toàn diện trên `master` trước khi rẽ nhánh `release` đảm bảo mã nguồn đã được hội đồng duyệt (CCB) chấp thuận trọn vẹn và không làm phân kỳ lịch sử.
- **Tính đóng băng của Release:** Nhánh `release/*` khi sinh ra là để đóng băng đường cơ sở (Baseline). Nếu sửa trực tiếp trên `release`, những thay đổi đó có nguy cơ bị "bỏ quên" và không được đưa ngược về `master`, dẫn đến mất mát mã nguồn trong các phiên bản tương lai.

---

### 2. So sánh mô hình Release Flow (trong học phần) với GitFlow. Vì sao không merge `release/*` ngược lại vào `master`?
- **Khác biệt cốt lõi:**
  - Trong **GitFlow**, nhánh release được tách từ `develop`, sau khi hoàn thiện sẽ được merge đồng thời vào `master` (để gắn tag) VÀ merge ngược lại `develop`. Mô hình này phức tạp, có 2 nhánh sống dài song song và dễ xung đột.
  - Trong **Release Flow**, chỉ có duy nhất một nhánh chính là `master`. Nhánh `release/*` được tách trực tiếp từ `master` tại thời điểm sẵn sàng phát hành.
- **Vì sao không merge `release/*` ngược vào `master`:**
  - Nhánh `release/*` được tạo từ `master` nên `master` đã chứa toàn bộ mã nguồn của release đó.
  - Mọi bản sửa lỗi phát sinh sau này trên release (hotfix) sẽ được áp dụng trực tiếp bằng `git cherry-pick -x` thay vì merge cả nhánh release vào `master`, nhằm tránh xung đột phiên bản và tránh kéo ngược các cấu hình cũ vào dòng phát triển mới.

---

### 3. Vì sao phiên bản này tăng lên `1.0.0` mà không phải `0.4.0`?
- Theo chuẩn **Semantic Versioning (SemVer - semver.org)**:
  - Dải `0.y.z` là giai đoạn thử nghiệm ban đầu (initial development), API chưa ổn định và có thể thay đổi bất kỳ lúc nào.
  - Phiên bản `1.0.0` đánh dấu mốc sản phẩm đã hoàn thiện bộ tính năng cốt lõi ban đầu (Production Ready), có giao diện/hàm ổn định, đầy đủ kiểm thử và tài liệu sẵn sàng bàn giao cho người dùng hoặc nộp nghiệm thu.
