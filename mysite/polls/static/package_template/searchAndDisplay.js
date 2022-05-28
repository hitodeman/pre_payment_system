//CSRF対策、おまじない------START-----------
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
//CSRF対策、おまじない------END-----------

$(function(){
    $('#begin_date').datepicker({
        minViewMode: 0,
        maxViewMode: 2,
        format: 'yyyy-mm-dd',
        language:'ja',
        startView: 1,
        autoclose: true,
        //daysOfWeekHighlighted: [0,6],
    });

    $('#late_date').datepicker({
        minViewMode: 0,
        maxViewMode: 2,
        format: 'yyyy-mm-dd',
        language:'ja',
        startView: 1,
        autoclose: true,
        //daysOfWeekHighlighted: [0,6],
    });
});

$(function(){
    $('#begin_date').datepicker().on({
        changeDate : function(e) {
            $('#late_date').datepicker('show');
            selected_date = e['date']; //開始日のデータ取得
            yyyy = selected_date.getFullYear();
            mm = selected_date.getMonth() + 1;
            sd = computeDate(yyyy, mm); //0000-00の形で指定日後が返ってくる
            $('#late_date').datepicker('setStartDate', sd);
            
        }
    });
});

$(function(){
    $('#late_date').datepicker().on({
        changeDate : function(e) {
            let id_ajax = document.getElementById('late_date');
            let url_ajax = id_ajax.getAttribute('data-url');
            $.post(
                url_ajax, 
                {
                    begin_date:$('#begin_date').val(),
                    late_date:$('#late_date').val()
                },
                'json')
                .done(function(response){//動的テーブル生成
                    ajax_data = '<tr>'
                    $.each(response.jpay, function(idx, obj) {
                        console.log(obj.bank_name)
                        if (obj.payment_valid_flg) {
                            ajax_data += '<td><div class="form-check"><input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" checked disabled="disabled"><label class="form-check-label" for="flexCheckDefault"></label></div></td>'
                            } 
                        else{
                            ajax_data += '<td><div class="form-check"><input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" disabled="disabled"><label class="form-check-label" for="flexCheckDefault"></label></div></td>'
                            }
                        ajax_data +=  '<td>'+obj.id+'</td>'
                        ajax_data +=  '<td>'+obj.payment_date+'</td>'
                        ajax_data +=  '<td>'+obj.customer_name+'</td>'
                        ajax_data +=  '<td>'+obj.bank_name+'</td>'
                        ajax_data +=  '<td>'+obj.payment_kind_name+'</td>'
                        ajax_data +=  '<td>'+obj.payment_money+'</td>'
                        ajax_data +=  '<td>'+obj.payment_memo+'</td>'
                        ajax_data += '<td><div class="container"><button type="button" class="mb-12 my_button btn btn-sm btn-outline-secondary " data-toggle="modal" data-target="#payment_modal'+obj.id+'">編集</button></div></td></tr>'
                        console.log(obj)
                    });
                    ajax_data += '</tr>'
                    $('#payment_form').empty();
                    $('#payment_totalDisp').empty();
                    $('#payment_form').append(ajax_data);
                    payment_totalDisp = '<p class="total-money text-right">合計金額　　'+response.payment_total+'円</p>'
                    $('#payment_totalDisp').append(payment_totalDisp);
                });
                
        }
    });
});

function computeDate(year, month) {
    var dt = new Date(year, month - 1);
    return dt;
}
$('late-date').attr('autocomplete', 'off');

