# Câu hỏi thảo luận - Lab 01

### 1. Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
- **Vị trí lưu trữ:**
  - Cấu hình `--global` được lưu trong tệp `.gitconfig` tại thư mục người dùng: `~/.gitconfig` (trên macOS/Linux) hoặc `C:\Users\<username>\.gitconfig` (trên Windows).
  - Cấu hình `--local` được lưu trong tệp `.git/config` nằm ngay bên trong thư mục gốc của repository hiện tại.
- **Sự khác biệt:**
  - **Phạm vi tác động:** `--global` áp dụng cho tất cả các repository của người dùng đó trên máy tính. Trong khi đó, `--local` chỉ có hiệu lực duy nhất đối với repository hiện tại.
  - **Độ ưu tiên:** Khi có sự trùng lặp cấu hình, Git sẽ ưu tiên cấu hình cấp thấp hơn: `--local` (mức repo) sẽ ghi đè lên cấu hình `--global` (mức user), và `--global` ghi đè lên `--system` (mức toàn hệ điều hành). Điều này cho phép một lập trình viên có thể dùng chung cấu hình chung (email, editor) cho mọi dự án, nhưng vẫn có thể dùng email công việc riêng cho từng repo cụ thể bằng cờ `--local`.

---

### 2. Vì sao dùng `git mv` thay vì di chuyển tệp bằng hệ điều hành thông thường?
- Khi dùng lệnh di chuyển của hệ điều hành (như `mv dvd.py aims/`), Git mặc định sẽ coi đó là 2 hành động rời rạc: tệp cũ bị xóa (`deleted`) và một tệp mới chưa được theo dõi xuất hiện (`untracked`). Người dùng phải thực hiện `git add` cả 2 vị trí để Git suy luận lại.
- Khi dùng `git mv dvd.py aims/dvd.py`:
  - Thao tác đổi tên/di chuyển được tự động đưa ngay vào Staging Area (trạng thái `renamed`).
  - Đảm bảo tính liên tục của lịch sử quản lý cấu hình (Configuration Identification).
  - Lệnh `git log --oneline --follow -- <path>` dễ dàng theo dõi trọn vẹn lịch sử chỉnh sửa xuyên suốt của tệp trước và sau khi đổi vị trí.

---

### 3. `release/lab01` có phải là một baseline không? Vì sao?
- **Có, `release/lab01` là một Baseline.**
- **Giải thích theo lý thuyết SCM:**
  - Theo chuẩn SCM, **Baseline** là một trạng thái cấu hình phần mềm tại một mốc thời gian cụ thể (milestone) đã được kiểm tra, đánh giá và chính thức phê duyệt (Approved), dùng làm điểm tựa ổn định cho các giai đoạn phát triển tiếp theo.
  - Nhánh `release/lab01` đóng băng trạng thái của Lab 01 sau khi đã hoàn thành khởi tạo và tái cấu trúc mã nguồn (Refactor). Mọi chỉnh sửa cho các tính năng mới trong tương lai sẽ không được commit thẳng vào đây mà phải đi qua quy trình thay đổi chính thức (Change Control Process).

---

### 4. Vì sao không commit thẳng vào `master` dù chỉ làm việc một mình?
- **Cô lập thay đổi (Isolation):** Mỗi nhánh (refactor, feature, bugfix) đại diện cho một mục đích duy nhất. Nếu quá trình refactor hoặc thử nghiệm gặp lỗi dở dang, nhánh `master` vẫn luôn ở trạng thái "sạch", chạy được và có thể deploy hoặc giao nộp bất kỳ lúc nào.
- **Kiểm soát thay đổi (Change Control):** Việc mở Pull Request (PR) tạo ra một không gian đánh giá (review diff, checklist kiểm thử) trước khi tích hợp vào nhánh chính. Nó giúp chính tác giả nhìn lại toàn cảnh các file bị thay đổi (tránh commit nhầm file rác, file nhạy cảm).
- **Rèn luyện văn hóa chuyên nghiệp:** Trong các dự án thực tế và BTL nhóm, không ai làm việc trực tiếp trên nhánh chính. Việc tuân thủ quy trình này giúp nhóm dễ dàng tích hợp CI/CD tự động, bảo vệ nhánh (Branch Protection) và không bao giờ gặp tình trạng "merge hell".
