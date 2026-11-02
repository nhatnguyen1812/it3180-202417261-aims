# Câu hỏi thảo luận - Lab 03

### 1. Merge base là gì? Vai trò của nó trong quá trình giải quyết xung đột?
- **Định nghĩa:** **Merge base** là commit tổ tiên chung gần nhất (lowest common ancestor) của hai nhánh đang được sáp nhập trong đồ thị lịch sử Git (Directed Acyclic Graph - DAG). Bạn có thể tìm commit này bằng lệnh `git merge-base branchA branchB`.
- **Vai trò:**
  - Git sử dụng merge base làm mốc đối chiếu trong thuật toán gộp 3 chiều (3-way merge).
  - Thuật toán so sánh phiên bản commit của nhánh A với merge base, và nhánh B với merge base. Nếu một dòng mã chỉ bị thay đổi ở một nhánh so với merge base, Git sẽ tự động chấp nhận thay đổi đó. Chỉ khi cả hai nhánh cùng sửa một dòng mã khác với merge base thì xung đột (Merge Conflict) mới xảy ra để lập trình viên tự kết hợp.

---

### 2. Vì sao trên các nhánh chung như `master`, `main` và `release/*` bắt buộc phải dùng `git revert` thay vì `git reset`?
- **Nguyên lý của `git reset`:** Lệnh này dời con trỏ nhánh lùi về quá khứ và viết lại lịch sử commit. Nếu áp dụng trên nhánh công khai đã chia sẻ (public branch), lập trình viên bắt buộc phải dùng `git push --force` để ghi đè remote. Điều này làm cho bản sao chép của tất cả các thành viên khác bị phân kỳ lịch sử (diverged), gây ra xung đột nghiêm trọng và làm hỏng luồng làm việc nhóm.
- **Nguyên lý của `git revert`:** Thay vì xóa commit cũ, `git revert` tạo ra một **commit mới** có nội dung đảo ngược hoàn toàn thay đổi của commit cần hủy.
- **Lý do bắt buộc:** Nhánh `master` và `release/*` đóng vai trò là đường cơ sở (Baseline) của dự án. Dùng `revert` giúp lịch sử luôn tiến về phía trước một cách tuyến tính và minh bạch, lưu lại bằng chứng đầy đủ cho việc kiểm toán cấu hình phần mềm (Audit Trail), đồng thời an toàn cho toàn bộ hệ thống CI/CD và các thành viên khác trong nhóm.
