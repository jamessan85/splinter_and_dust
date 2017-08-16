/**
 * Created by Administrator on 27/07/2017.
 */

$(document).ready(function () {
     $(".hamburger").click(function () {
        $(".navibar").slideToggle().css('display','flex');
    });

    $("#button1").click(function () {
        $("#dropdown-content1").slideToggle().css('display','block');
         $("#dropdown-content2").slideToggle().css('display','none');
         $("#dropdown-content3").slideToggle().css('display','none');
         $("#dropdown-content4").slideToggle().css('display','none');
    });

    $("#button2").click(function () {
        $("#dropdown-content2").slideToggle().css('display','block');
        $("#dropdown-content1").slideToggle().css('display','none');
        $("#dropdown-content3").slideToggle().css('display','none');
        $("#dropdown-content4").slideToggle().css('display','none');
    });

    $("#button3").click(function () {
        $("#dropdown-content3").slideToggle().css('display','block');
        $("#dropdown-content1").slideToggle().css('display','none');
        $("#dropdown-content2").slideToggle().css('display','none');
        $("#dropdown-content4").slideToggle().css('display','none');
    });

        $("#button4").click(function () {
        $("#dropdown-content4").slideToggle().css('display','block');
        $("#dropdown-content1").slideToggle().css('display','none');
        $("#dropdown-content2").slideToggle().css('display','none');
        $("#dropdown-content3").slideToggle().css('display','none');
    });

});
