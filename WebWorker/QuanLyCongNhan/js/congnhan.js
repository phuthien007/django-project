$(document).ready(function () {



    loadData();



    $("#ho-ten").click(function (e) {
        $(".menu-ca-nhan").removeClass("d-none");
        e.stopPropagation();
    });
   

    $("#doi-mat-khau").click(function (e) {
        $(".doi-mat-khau").removeClass("d-none");
        e.stopPropagation();
    });
    $(".doi-mat-khau").click(function(e){
        e.stopPropagation();
    })
    $("body").click(function () {
        $(".menu-ca-nhan").addClass("d-none");
        $(".doi-mat-khau").addClass("d-none");

    });


    $("#dangxuat").click(function () {

        window.localStorage.removeItem('authorization');
        window.sessionStorage.removeItem('tencongnhan')
        duong_dan_hien_tai = window.location.href;
        duong_dan = duong_dan_hien_tai.replace("congnhan", "dangnhap");
        window.location = duong_dan

    });

    $("btn-bao-cao").click(function () {
        $(".tien-do-cong-viec").addClass("d-none");
    })

    doimatkhau();








});

function loadData() {
    $.ajax({
        type: "GET",
        url: URL_API + "/api/ds_cong_viec",
        data: {
            authorization: window.localStorage.getItem('authorization')
        },
        headers: {
            "Authorization": "token " + localStorage.getItem('authorization')
        },
        dataType: "JSON",
        success: function (response) {
            $("#ho-ten").html(window.sessionStorage.getItem('tencongnhan'));
            console.log(response);
            response.forEach(element => {
                let text = "<tr><td>" + element.tencongviec + "</td><td>" + element.noilamviec + "</td> <td>" + element.tengiong + "</td> <td>" + element.tenphanbon + "</td><td>" + element.tenthuoc + "</td><td>" + element.soluongthuoc + "</td><td>" + element.thoigian + '</td> <td class ="congviec" data_id=' + element.id_congviec + '><button class ="btn btn-success btn-bao-cao-main">Báo cáo</button></td> </tr>';
                $("#tbody").append(text);



            });
            $(".btn-bao-cao-main").click(function (e) {
                var id_congviec = $(this).closest("tr").find(".congviec").attr("data_id");;
                $(".tien-do-cong-viec").removeClass("d-none");
                guibaocao(id_congviec);

            });


        }
    });
}

function guibaocao(id_congviec) {
    $(".btn-bao-cao").click(function () {
        var mo_ta = $(".mo-ta-trang-thai").val();
        var trangthai;
        if (document.getElementById("defaultUnchecked").checked == true) {
            trang_thai = "Hoàn thành";
        } else if (document.getElementById("defaultChecked").checked == true) {
            trang_thai = "Chưa hoàn thành";
        }
        var hinh;

        var file_name = $("#file-up").val().replace(/C:\\fakepath\\/i, "");
        fileSelect = document.getElementById("file-up").files;



        var fileSelect = fileSelect[0];
        var fileReader = new FileReader();
        fileReader.onload = function (FileLoadEvent) {
            hinh = FileLoadEvent.target.result.replace("data:image/jpeg;base64,", "");
            console.log(hinh);
            $.ajax({

                type: "POST",
                url: URL_API + "/api/gui_bao_cao",
                data: {
                    trangthai: trang_thai,
                    mota: mo_ta,
                    hinhanh: hinh,
                    file_name: file_name,
                    id_congviec: id_congviec

                },
                headers: {
                    "Authorization": "token " + localStorage.getItem('authorization')
                },
                dataType: "dataType",
                success: function (response) {
                    duong_dan_hien_tai = window.location.href;
                    window.location = duong_dan_hien_tai
                }
            });
        }

        fileReader.readAsDataURL(fileSelect)


        $(".tien-do-cong-viec").addClass("d-none");


    });


}

function encodeImageFileURL() {
    fileSelect = document.getElementById("file-up").files;
    if (fileSelect.length > 0) {
        var fileSelect = fileSelect[0];
        var fileReader = new FileReader();
        fileReader.onload = function (FileLoadEvent) {
            var srcData = FileLoadEvent.target.result;
            document.getElementById("imageFile").src = srcData

        }
        fileReader.readAsDataURL(fileSelect)
    }
}

function doimatkhau() {
    $("#btn-doi-mat-khau").click(function () {
        var mat_khau_cu = $("#mat-khau-cu").val();
        var mat_khau_moi = $("#mat-khau-moi").val();
        var nhap_lai_mat_khau_moi = $("#nhap-lai-mat-khau").val();
        if (mat_khau_cu === mat_khau_moi) {
            swal("", "Bạn đã nhập mật khẩu cũ vui lòng nhập lại", "error");
        } else if (mat_khau_moi != nhap_lai_mat_khau_moi) {
            swal("", "Mật khẩu mới không trùng khớp", "error");
        } else {
            $.ajax({
                type: "PUT",
                url: URL_API + "/api/doimk",
                data: {
                    old_password: mat_khau_cu,
                    new_password: mat_khau_moi
                },
                headers: {
                    "Authorization": "token " + localStorage.getItem('authorization')
                },
                success: function (response) {
                    window.localStorage.removeItem('authorization');
                    window.sessionStorage.removeItem('tencongnhan')
                    duong_dan_hien_tai = window.location.href;
                    duong_dan = duong_dan_hien_tai.replace("congnhan", "dangnhap");
                    window.location = duong_dan
                   
                }
            });
        }
       

    })

}



function encodeImgtoBase64(element) {

    var file = element.files[0];

    var reader = new FileReader();

    reader.onloadend = function () {

        $("#convertImg").attr("href", reader.result);

        $("#convertImg").text(reader.result);

        $("#base64Img").attr("src", reader.result);

    }

    reader.readAsDataURL(file);

}