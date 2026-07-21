> Đây là bản dịch tham khảo. Phiên bản tiếng Nhật là văn bản chính thức.

# Chính sách Quyền riêng tư của KUU

Cập nhật lần cuối: Ngày 21 tháng 7 năm 2026

**Tóm tắt:** Những gì bạn nói là của bạn. **Giọng nói của bạn sẽ không được gửi ra bên ngoài**. Việc chuyển thành văn bản được thực hiện ngay trên thiết bị của bạn. Việc sắp xếp (phân loại bằng AI) có sử dụng AI bên ngoài, nhưng chỉ có nội dung văn bản được gửi đi, chỉ dùng để sắp xếp và không được lưu trữ (phiên bản iOS có thể đổi sang chế độ sắp xếp chỉ trên thiết bị trong Cài đặt > "Trên thiết bị". **Phiên bản Android chỉ gửi đến AI bên ngoài, không có tùy chọn sắp xếp trên thiết bị**). Dữ liệu được lưu trên thiết bị của bạn và, đối với phiên bản iOS, trong iCloud (cơ sở dữ liệu riêng tư) (phiên bản Android chỉ lưu trên thiết bị). Nhà phát triển không lưu trữ nội dung và cũng không thể xem nội dung đã nhận. Bạn có thể xóa toàn bộ dữ liệu từ bên trong ứng dụng bất kỳ lúc nào. Ứng dụng chỉ thực hiện **truyền dữ liệu tối thiểu cần thiết** cho việc thanh toán (iOS=StoreKit／Android=RevenueCat) và quảng cáo Google AdMob, và thông tin đó không bao gồm nội dung bạn đã nói (quảng cáo sẽ bị vô hiệu hóa khi bạn đăng ký KUU+). Chúng tôi có đo lường tình hình sử dụng để cải thiện chất lượng, nhưng việc này cũng không bao gồm nội dung bạn đã nói (iOS yêu cầu người dùng đồng ý (opt-in), Android mặc định thực hiện đo lường không chứa nội dung (content-free). Chi tiết tại Điều 14).

---

## Điều 1 (Chính sách cơ bản)

Ứng dụng "KUU" (sau đây gọi là "Ứng dụng này") là một ứng dụng hỗ trợ bạn giải tỏa những suy nghĩ trong đầu bằng cách nói ra và sắp xếp chúng. Ứng dụng có **phiên bản iOS và Android**, và chính sách này áp dụng cho cả hai. Ứng dụng này chỉ xử lý thông tin trong phạm vi tối thiểu cần thiết để cung cấp các tính năng, và ưu tiên hàng đầu là bảo vệ quyền riêng tư của người dùng.

## Điều 2 (Thông tin thu thập và lưu trữ)

Thông tin mà Ứng dụng này xử lý chỉ giới hạn trong những mục sau:

1.  **Nội dung người dùng nói (dữ liệu âm thanh)** — Âm thanh đã ghi âm chỉ được lưu tạm thời trong khu vực tạm của thiết bị trong quá trình chuyển thành văn bản, và sẽ bị xóa ngay lập tức sau khi xử lý xong. Dữ liệu này không được gửi đến máy chủ.
2.  **Kết quả chuyển thành văn bản và kết quả sắp xếp (văn bản)** — Được lưu trữ để bạn có thể xem lại (phiên bản iOS: trên thiết bị và trong cơ sở dữ liệu riêng tư iCloud; phiên bản Android: chỉ trên thiết bị. Chi tiết tại Điều 4).
3.  **Cài đặt trong ứng dụng** — Các giá trị cài đặt cần thiết cho hoạt động của ứng dụng như chủ đề, cỡ chữ, trạng thái mực nước trong đầu.

Ứng dụng này không thu thập các thông tin cá nhân như họ tên, địa chỉ email, số điện thoại, thông tin vị trí, danh bạ, lịch, ảnh, hay mã nhận dạng thiết bị.

## Điều 3 (Về nhận dạng giọng nói và phân loại bằng AI)

**Nhận dạng giọng nói (Chuyển thành văn bản)** hoàn toàn được thực hiện trên thiết bị iOS của bạn.

-   Nhận dạng giọng nói: Sử dụng Speech framework của Apple (trên thiết bị). Bản thân giọng nói không được gửi ra khỏi thiết bị.

**Phân loại bằng AI (Phân loại danh mục)** sử dụng AI bên ngoài.

-   Chỉ có **nội dung đã được chuyển thành văn bản (transcript)** được gửi đi. Giọng nói không được gửi đi.
-   Dữ liệu được gửi đến một AI bên ngoài, thông qua máy chủ của nhà phát triển (qua backend đến Gemini của Google).
-   Nội dung được gửi **chỉ được sử dụng để phân loại và không được lưu trữ**. Nó cũng không được sử dụng để huấn luyện AI.
-   **Đối với phiên bản iOS**, bạn có thể chuyển sang **chế độ phân loại chỉ trên thiết bị** (FoundationModels của Apple / các quy tắc trên thiết bị) bất kỳ lúc nào thông qua mục "Trên thiết bị" trong Cài đặt. Trong trường hợp này, văn bản cũng sẽ không được gửi ra khỏi thiết bị.

**Về phiên bản Android:** Phiên bản Android không cung cấp phương thức sắp xếp (phân loại) hoàn toàn trên thiết bị. Khi bạn thực hiện sắp xếp, văn bản đã được chuyển đổi **bắt buộc** được gửi đến AI bên ngoài (Gemini của Google thông qua backend của chúng tôi). Không có tùy chọn chuyển đổi sang "Trên thiết bị" như phiên bản iOS. Chỉ có nội dung văn bản được gửi đi, bản thân giọng nói không được gửi đi, và văn bản được gửi chỉ được sử dụng để phân loại, không được lưu trữ và cũng không được dùng để huấn luyện AI. Quá trình chuyển thành văn bản (nhận dạng giọng nói) được thực hiện hoàn toàn trên thiết bị.

## Điều 4 (Lưu trữ và đồng bộ hóa)

**Phiên bản iOS:** Kết quả chuyển thành văn bản và kết quả sắp xếp chỉ được lưu trong **cơ sở dữ liệu riêng tư iCloud của bạn** (CloudKit Private Database). Đây là không gian lưu trữ do Apple cung cấp, và chỉ có bạn mới có thể truy cập nội dung đã lưu. Nhà phát triển của Ứng dụng này không thể xem hay lấy được nội dung đã lưu. Việc sử dụng iCloud tuân theo chính sách quyền riêng tư của Apple.

**Phiên bản Android:** Kết quả chuyển thành văn bản và kết quả sắp xếp chỉ được lưu **trên thiết bị này**. Ứng dụng không thực hiện đồng bộ hóa đám mây tự động. Khi đổi thiết bị, bạn có thể xuất dữ liệu ra tệp từ mục "Giọng nói & Dữ liệu" trong ứng dụng và nhập vào thiết bị mới. Người dùng tự chọn nơi lưu tệp (trong thiết bị, ứng dụng lưu trữ đám mây của bạn, v.v.). Nhà phát triển không thể truy cập vào tệp này.

## Điều 5 (Mục đích sử dụng)

Thông tin được xử lý chỉ được sử dụng cho các mục đích sau:

1.  Tạo văn bản từ giọng nói và hiển thị cho người dùng
2.  Phân loại văn bản thành "Xem ngay / Để sau / Gác lại / Buông bỏ" và hiển thị cho người dùng
3.  Lưu trữ và hiển thị những nội dung người dùng đã nói để họ có thể tự xem lại
4.  Duy trì các giá trị cài đặt cần thiết cho hoạt động của ứng dụng

## Điều 6 (Sử dụng các dịch vụ bên ngoài)

Ứng dụng này sử dụng các dịch vụ bên ngoài sau đây để cung cấp tính năng. **Bản thân giọng nói không được gửi đến bất kỳ dịch vụ nào trong số này**.

-   **iCloud / CloudKit** (Chỉ phiên bản iOS. Do Apple cung cấp. Chỉ lưu trữ và đồng bộ hóa vào cơ sở dữ liệu riêng tư của bạn)
-   **Nhận dạng giọng nói** (Phiên bản iOS: Speech framework của Apple, phiên bản Android: công cụ nhận dạng giọng nói trên thiết bị. Cả hai đều chạy trên thiết bị, giọng nói không được gửi ra bên ngoài)
-   **AI bên ngoài (đám mây)** (Phân loại bằng AI. Chỉ gửi nội dung văn bản. Chỉ được sử dụng để phân loại, không được lưu trữ, không được dùng để huấn luyện AI. Phiên bản iOS có thể tắt tính năng này qua Cài đặt > "Trên thiết bị", nhưng **phiên bản Android chỉ gửi đến AI bên ngoài**. Chi tiết tại Điều 3)
-   **FoundationModels** (Chỉ phiên bản iOS. Do Apple cung cấp. Hoàn toàn chạy trên thiết bị. Được sử dụng khi cài đặt "Trên thiết bị" được bật, hoặc làm phương án dự phòng khi không thể sử dụng AI bên ngoài)
-   **Dịch vụ thanh toán** (Phiên bản iOS: **Apple StoreKit**, phiên bản Android: **RevenueCat**. Quản lý việc mua, gia hạn, hủy và trạng thái quyền của gói đăng ký KUU+. Nội dung đã nói không được gửi đi. Về RevenueCat, xem Điều 7 và [Chính sách Quyền riêng tư của RevenueCat](https://www.revenuecat.com/privacy))
-   **Play Integrity API (qua Firebase App Check. Chỉ phiên bản Android)** (Chứng thực tính toàn vẹn của thiết bị/ứng dụng để xác nhận rằng yêu cầu đến API phân loại được gửi từ một ứng dụng hợp lệ. Không chứa nội dung đã nói hay thông tin nhận dạng người dùng)
-   **Google AdMob (Google Mobile Ads SDK)** (Chỉ khi chưa đăng ký KUU+, hiển thị một khung quảng cáo tự nhiên giữa các phần trong màn hình "Những điều đã nói". Nội dung đã nói không được gửi đi. Chi tiết tại Điều 13)
-   **Firebase Analytics** (Do Google cung cấp. Để cải thiện chất lượng ứng dụng. Phiên bản iOS: **chỉ khi người dùng đồng ý (opt-in) một cách rõ ràng trong Cài đặt**, phiên bản Android: **mặc định** gửi các sự kiện sử dụng không chứa nội dung (content-free) (cả hai trường hợp đều không gửi nội dung đã nói). Phiên bản iOS cũng sử dụng **Crashlytics** khi người dùng đồng ý, nhưng **phiên bản Android không tích hợp Crashlytics**. Chi tiết tại Điều 14)

Máy chủ của Ứng dụng này chỉ là một máy chủ tối giản, không lưu trữ trạng thái (stateless), chỉ làm nhiệm vụ trung chuyển cho việc phân loại bằng AI và hoàn toàn không lưu trữ nội dung. Ứng dụng không sử dụng các dịch vụ xác thực yêu cầu tài khoản cá nhân.

## Điều 7 (Cung cấp cho bên thứ ba)

Nhà phát triển của Ứng dụng này không có phương tiện nào để truy cập nội dung bạn đã nói, kết quả chuyển thành văn bản, hay kết quả sắp xếp, và không cung cấp những thông tin này cho bất kỳ bên thứ ba nào.

Với mục đích phân phối quảng cáo cho người dùng chưa đăng ký KUU+, các thông tin mà Google AdMob yêu cầu để phân phối quảng cáo như mã nhận dạng thiết bị, ID quảng cáo, ngôn ngữ và khu vực của thiết bị, thông tin vị trí ước chừng, thông tin về lượt nhấp vào quảng cáo, v.v., sẽ được gửi đến Google (chi tiết tại Điều 13, chính sách quyền riêng tư AdMob của Google sẽ được áp dụng). Khi bạn đã đăng ký KUU+, việc truyền thông tin này sẽ không xảy ra.

Khi bạn đăng ký KUU+ trên **phiên bản Android**, thông tin mua hàng (ID sản phẩm, giá, ngày giờ mua, v.v.) sẽ được gửi đến RevenueCat, Inc. để quản lý quá trình xử lý mua hàng và quyền lợi (xác định trạng thái hợp lệ/không hợp lệ). Nội dung đã nói không được gửi đi. Vui lòng xem [Chính sách Quyền riêng tư của RevenueCat](https://www.revenuecat.com/privacy) để biết chi tiết về cách xử lý dữ liệu của RevenueCat.

Chúng tôi chỉ tuân thủ việc tiết lộ thông tin khi có yêu cầu bắt buộc theo pháp luật và sẽ thực hiện theo các thủ tục quy định.

## Điều 8 (Xóa dữ liệu)

Người dùng có thể xóa toàn bộ dữ liệu bất kỳ lúc nào từ "Cài đặt → Giọng nói & Dữ liệu → Xóa những gì đã lưu" bên trong ứng dụng. Việc xóa sẽ loại bỏ hoàn toàn dữ liệu trên thiết bị (và, đối với phiên bản iOS, cả dữ liệu trên cơ sở dữ liệu riêng tư iCloud). Dữ liệu đã xóa không thể được khôi phục.

Khi gỡ cài đặt Ứng dụng này, dữ liệu trên thiết bị sẽ bị xóa. Dữ liệu trên iCloud của phiên bản iOS có thể được xóa từ Cài đặt của Apple (Cài đặt → Apple ID → iCloud → Quản lý dung lượng). Phiên bản Android chỉ lưu dữ liệu trên thiết bị, nên dữ liệu sẽ bị xóa khi gỡ cài đặt.

## Điều 9 (Biện pháp quản lý an toàn)

-   **Phiên bản iOS**: Các tệp âm thanh tạm thời trong quá trình ghi âm được mã hóa bằng tính năng bảo vệ tệp của iOS (`FileProtectionType.complete`) và không thể truy cập khi thiết bị bị khóa. Giao tiếp với iCloud được Apple mã hóa bằng SSL/TLS.
-   **Phiên bản Android**: Âm thanh đã ghi âm không được ghi ra đĩa ngay cả dưới dạng tệp tạm thời; nó chỉ được xử lý trong bộ nhớ và bị hủy ngay lập tức sau khi nhận dạng. Kết quả chuyển thành văn bản và sắp xếp được lưu trong khu vực riêng của ứng dụng trên Android, không thể truy cập bởi các ứng dụng khác, và cũng được loại trừ khỏi tính năng sao lưu đám mây tự động của Android.
-   Tất cả giao tiếp với AI bên ngoài đều được mã hóa (HTTPS/TLS). Máy chủ của nhà phát triển chỉ làm nhiệm vụ trung chuyển cho việc phân loại và không lưu trữ nội dung (stateless).

## Điều 10 (Sử dụng bởi người vị thành niên)

Ứng dụng này được xếp hạng 4+, nhưng do tính chất sắp xếp suy nghĩ, chúng tôi giả định người dùng ở độ tuổi có thể đọc và viết. Nếu người vị thành niên sử dụng ứng dụng, vui lòng sử dụng sau khi có sự đồng ý của người giám hộ.

## Điều 11 (Thay đổi chính sách quyền riêng tư)

Chính sách này có thể được sửa đổi do thay đổi pháp luật, bổ sung tính năng, hoặc thay đổi trong đặc tả của các framework hay chính sách của các nền tảng (Apple / Google). Trong trường hợp có những thay đổi quan trọng, chúng tôi sẽ thông báo khi cập nhật ứng dụng hoặc trên trang công khai của chính sách này.

## Điều 12 (Liên hệ)

Mọi thắc mắc liên quan đến chính sách này, vui lòng liên hệ qua mục "Nhà phát triển" trên trang ứng dụng tại App Store hoặc Google Play, hoặc qua "Cài đặt → Liên hệ" bên trong ứng dụng.

## Điều 13 (Về quảng cáo và App Tracking Transparency)

Trong thời gian bạn chưa đăng ký gói KUU+, Ứng dụng này sẽ hiển thị một khung quảng cáo tự nhiên duy nhất do Google AdMob cung cấp trên màn hình "Những điều đã nói". Bản thân quảng cáo được hiển thị một cách kín đáo giữa các phần của màn hình để duy trì không gian của KUU.

-   **Nội dung bạn nói sẽ không bao giờ được sử dụng cho mục đích quảng cáo** (quảng cáo không tham chiếu đến kết quả chuyển văn bản, kết quả phân loại, hay chủ đề của bạn).
-   Để phân phối quảng cáo, Google AdMob có thể thu thập các mã nhận dạng thiết bị (bao gồm IDFA), ID quảng cáo, Vị trí ước chừng (Coarse Location), Chẩn đoán, và Tương tác sản phẩm (thông tin tương tác với quảng cáo trong ứng dụng).
-   **Phiên bản iOS**: Lời nhắc **App Tracking Transparency** (ATT) sẽ được hiển thị một lần duy nhất, ngay trước khi quảng cáo đầu tiên xuất hiện. Quảng cáo vẫn sẽ được hiển thị ngay cả khi bạn không cho phép, nhưng thông tin gửi đến Google sẽ bị giới hạn (không được cá nhân hóa). Bạn có thể thay đổi trạng thái cho phép ATT bất kỳ lúc nào trong "Cài đặt" → "Quyền riêng tư & Bảo mật" → "Theo dõi" của iOS.
-   **Phiên bản Android**: ATT là cơ chế độc quyền của iOS và không có trên Android. Thay vào đó, **ID quảng cáo (Advertising ID)** của Google được sử dụng để phân phối quảng cáo. Bạn có thể từ chối cá nhân hóa quảng cáo hoặc đặt lại ID quảng cáo của mình từ "Cài đặt → Quyền riêng tư → Quảng cáo" trên thiết bị của bạn (cách diễn đạt có thể khác nhau tùy theo thiết bị và phiên bản Android). Đồng thời, phiên bản Android sẽ tuân thủ cơ chế quản lý sự đồng ý (UMP) được hiển thị ở các khu vực áp dụng như EU.
-   **Đăng ký KUU+ sẽ dừng tất cả quảng cáo và việc truyền dữ liệu liên quan.**
-   Để biết chi tiết về cách xử lý dữ liệu của Google AdMob, vui lòng xem [Chính sách Quyền riêng tư của Google AdMob](https://support.google.com/admob/answer/6128543).

## Điều 14 (Về việc sử dụng Firebase Analytics / Crashlytics)

**Phương thức yêu cầu sự đồng ý (opt-in) trong Điều này áp dụng cho phiên bản iOS. Đối với phiên bản Android, vui lòng xem mục "Về phiên bản Android" ở cuối Điều này.**

**Phiên bản iOS**, để cải thiện chất lượng ứng dụng và nhận biết ngay lập tức các sự cố trên thực tế, có thể sử dụng Firebase Analytics của Google (tổng hợp tình hình sử dụng) và Firebase Crashlytics (báo cáo sự cố). **Tính năng này mặc định là TẮT (không gửi dữ liệu) và chỉ hoạt động khi người dùng đồng ý (opt-in) một cách rõ ràng qua "Cài đặt → Dữ liệu & Chẩn đoán".**

-   **Thông tin được gửi**:
    -   ID cài đặt ẩn danh do Firebase tự động cấp (dựa trên IDFV; không phải là mã nhận dạng trực tiếp cá nhân).
    -   Tín hiệu tổng hợp về các sự kiện thao tác trong ứng dụng (sự kiện tổng hợp như hoàn thành phiên ghi âm, hiển thị/chuyển đổi Paywall, hoàn thành Onboarding. Các giá trị số được gửi ở dạng phân loại theo nhóm (bucket) với độ chi tiết thấp).
    -   Dấu vết ngăn xếp (stack trace) của sự cố (đã được symbol hóa) khi ứng dụng bị đóng đột ngột.
-   **Thông tin không được gửi**: Nội dung bạn nói (âm thanh), kết quả chuyển thành văn bản, văn bản kết quả phân loại AI, và tên chủ đề bạn đặt đều **được thiết kế ở cấp độ loại (type-level) để không thể gửi đi** (về mặt triển khai, API được thiết kế để không thể truyền giá trị chuỗi cho SDK đo lường).
-   **Trong thời gian bạn chưa đồng ý (opt-in), hoàn toàn không có bất kỳ giao tiếp nào với Firebase xảy ra**, bao gồm tất cả các thông tin nêu trên.
-   **Cách ngừng gửi**: Bạn có thể TẮT nút gạt trong "Cài đặt → Dữ liệu & Chẩn đoán" bất kỳ lúc nào. Khi TẮT, các ID cài đặt trước đó sẽ bị hủy, và các nhật ký sự cố chưa gửi được lưu trữ trên thiết bị cũng sẽ bị xóa.
-   Bên nhận là Google LLC (Hoa Kỳ). [Thông tin Quyền riêng tư của Firebase](https://firebase.google.com/support/privacy) của Google sẽ được áp dụng.

**Về phiên bản Android:** Phiên bản Android sử dụng Firebase Analytics và gửi các **sự kiện sử dụng không chứa nội dung (content-free)** để cải thiện sản phẩm (các giá trị được phân nhóm như số lần chuyển màn hình và số lần sử dụng tính năng) cùng với một ID phiên bản ứng dụng (App Instance ID) ẩn danh do Firebase cấp. **Khác với phiên bản iOS, tính năng này được bật theo mặc định.** Nội dung bạn nói (âm thanh), kết quả chuyển thành văn bản, kết quả sắp xếp và tên chủ đề **không thể được gửi đi** do thiết kế của SDK đo lường không cho phép truyền giá trị chuỗi. **Phiên bản Android không tích hợp Crashlytics và không gửi báo cáo sự cố.** Bên nhận là Google LLC (Hoa Kỳ); [Thông tin Quyền riêng tư của Firebase](https://firebase.google.com/support/privacy) của Google sẽ được áp dụng.
