# Câu hỏi thảo luận - Lab 05

### 1. So sánh ưu, nhược điểm của cách tiếp cận "Upstream First" (Microsoft Release Flow) so với "Release First" (Học phần)?
- **Cách tiếp cận "Release First" (Sửa trên nhánh Release trước):**
  - *Ưu điểm:* Cho phép tái hiện và kiểm thử bản vá chính xác trên môi trường/đường cơ sở (Baseline) của phiên bản đang gặp lỗi trong thực tế, không bị ảnh hưởng bởi mã nguồn mới chưa ổn định trên `master`.
  - *Nhược điểm:* Đòi hỏi tính kỷ luật cao của đội ngũ phát triển để lan truyền (cherry-pick) bản sửa sang `master` và các nhánh release song song khác; nếu quên, lỗi sẽ tái diễn trong tương lai.
- **Cách tiếp cận "Upstream First" (Sửa trên `master` trước rồi cherry-pick về release):**
  - *Ưu điểm:* Đảm bảo lỗi không bao giờ bị quên trên dòng phát triển chính (`master`), loại bỏ hoàn toàn nguy cơ tái phát lỗi (regression) ở các phiên bản kế tiếp.
  - *Nhược điểm:* Quá trình backport (cherry-pick ngược về release cũ) dễ gặp xung đột nếu `master` đã thay đổi quá nhiều so với bản phát hành cũ.

---

### 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện được?
- **Vòng lặp kiểm thử đa phiên bản (Multi-version behavioral test loop):**
  ```bash
  for ref in v1.0.1 v1.1.0 master; do
    git switch --detach -q $ref; printf "%-8s " $ref
    python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; \
    print(len(search_by_title([D('The Lion King')], 'lion')))"
  done; git switch -q master
  ```
  Nếu quên lan truyền sang `release/lab05` (hoặc `v1.1.0`), tại mốc `v1.1.0` sẽ in ra `0` (thất bại) thay vì `1` (thành công).
- **Lệnh kiểm toán lịch sử commit:**
  - `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"`: Nếu thiếu, chỉ thấy 1 commit cherry-pick thay vì đủ 2 commit trên cả `master` và `release/lab05`.
  - `git cherry -v origin/master origin/release/lab05`: Sẽ hiển thị dấu `+` đối với commit sửa lỗi nếu một trong hai bên chưa có bản vá tương đương.
