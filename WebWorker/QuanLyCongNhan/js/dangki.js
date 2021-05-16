$(document).ready(function () {
    $("#btn-dang-ki").click(function () {

        var ho_va_ten = $("#ho_va_ten").val();
        var dia_chi = $("#dia_chi").val();
        var so_dien_thoai = $("#so_dien_thoai").val();
        var ten_dang_nhap = $("#ten_dang_nhap").val();
        var mat_khau = $("#mat_khau").val();
        var nhap_lai_mat_khau = $("#nhap_lai_mat_khau").val();
        var email = $("#email").val();

        if (nhap_lai_mat_khau != mat_khau) {
            swal("", "Mật khẩu không trùng khớp", "error");
        } else {
            $.ajax({
                type: "POST",
                url: URL_API + "/api/dangki",
                data: {
                    username: ten_dang_nhap,
                    password: mat_khau,
                    email: email,
                    hoten: ho_va_ten,
                    diachi: dia_chi,
                    sdt: so_dien_thoai

                },
                dataType: "JSON",
                success: function (response) {
                    window.localStorage.setItem('authorization', response.token);
                    console.log(window.localStorage.getItem('authorization'));
                    duong_dan_hien_tai = window.location.href;
                    console.log(duong_dan_hien_tai)
                    duong_dan = duong_dan_hien_tai.replace("dangki", "dangnhap");
                    window.location = duong_dan
                },
                error: function (e) {
                    swal("", "Tài khoản đã tồn tại", "error");
                }
            });
        }
    });


});