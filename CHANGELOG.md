# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [1.1.0] - 2026-11-02
### Added
- Chức năng tìm kiếm theo thể loại search_by_category().
- Chức năng sắp xếp giỏ hàng sort_by_title() và sort_by_cost().


## [1.0.0] - 2026-11-02
### Added
- Cấu trúc gói mã nguồn `aims/` gồm `DigitalVideoDisc` và `Cart`.
- Chức năng in giỏ hàng `Cart.print_cart()`.
- Chức năng tìm kiếm đĩa theo tiêu đề `search_by_title()`.
- Tính năng tính tổng tiền có chiết khấu `total_cost_with_discount()`.
- Kiểm thử tự động với `unittest` trong `tests/test_cart.py`.
- Tài liệu ca sử dụng `docs/use-case.md`.

### Fixed
- Sửa lỗi giỏ hàng nhận đĩa thứ 21 vượt quá giới hạn 20 đĩa (#6).
