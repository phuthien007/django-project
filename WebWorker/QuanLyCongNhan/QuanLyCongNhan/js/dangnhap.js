$(document).ready(function () {
  
    $("#btn-dang-nhap").click(function () {
        var ten_dang_nhap = $("#ten-dang-nhap").val();
        var mat_khau = $("#mat-khau").val();

            $.ajax({
                type: "POST",
                url: URL_API+"/api/dangnhap",
                data: {
                    username: ten_dang_nhap,
                    password: mat_khau
                },
                dataType: "JSON",
                success: function (response) {
                    window.sessionStorage.setItem('tencongnhan', ten_dang_nhap);
                    window.localStorage.setItem('authorization', response.token);
                    console.log(window.localStorage.getItem('authorization'));
                    duong_dan_hien_tai = window.location.href;
                    duong_dan = duong_dan_hien_tai.replace("dangnhap", "congnhan");
                    window.location = duong_dan
                },
                error: function (e) {
                    swal("", "Tài khoản bị sai mật khẩu hoặc tên đăng nhập", "error");
                }
            });
    })

});