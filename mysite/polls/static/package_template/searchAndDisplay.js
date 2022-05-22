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

    $('#input_date').datepicker({
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
            $.post(
                "", 
                {
                    begin_date:$('#begin_date').val(),
                    late_date:$('#late_date').val()
                },
                'json')
                
                .done(function(response){
                    console.log(response);
                    $('#payment_form').empty();
                    $('#payment_totalDisp').empty();

                    $('#payment_form').append(response.payment_form);
                    $('#payment_totalDisp').append(response.payment_totalDisp);
                    //console.log(info_list);
                    /*
                    for (const payment_info of response.jpay_info_list) {
                        const p_info_id = $('<td>', {text: payment_info.fields.customer_id});
                        $('#payment_form').append(p_info_id);
                        const p_info_date = $('<td>', {text: payment_info.updated_at});
                        $('#payment_form').append(p_info_date);
                        //const p_info_name = $('<td>', {text: payment_info.customer_name});
                        //$('#payment_form').prepend(p_info_name);
                        const p_info_bank_name = $('<td>', {text: payment_info.bank_name});
                        $('#payment_form').append(p_info_bank_name);
                        //const p_info_kind_name = $('<td>', {text: payment_info.payment_kind_id.payment_kind_name});
                        //$('#payment_form').prepend(p_info_kind_name);
                        const p_info_money = $('<td>', {text: payment_info.payment_money});
                        $('#payment_form').append(p_info_money);
                        const p_info_memo = $('<td>', "((φ(・ω・´*)ﾒﾓﾒﾓ");
                        $('#payment_form').append(p_info_money);
                    }
                    */
                    $('#payment_totalDisp').append(response.payment_totalDisp);
                    /*
                    $('#payment').prepend('{% if ' + request.payment_info_list + ' %}');
                    $('#payment').prepend('{% for payment_info in ' + request.payment_info_list + ' %}');
                    $('#payment').prepend('<tr><td><div class="form-check"><input class="form-check-input" type="checkbox" value="" id="flexCheckDefault"><label class="form-check-label" for="flexCheckDefault"></label></div></td><td>{{payment_info.id}}</td><td>{{payment_info.updated_at}}</td><td>{{payment_info.customer_id.customer_name}}</td><td>{{payment_info.bank_name}}</td><td>{{payment_info.payment_kind_id.payment_kind_name}}</td>');
                    $('#payment').prepend('<td>￥{{payment_info.payment_money}}</td><td>((φ(・ω・´*)ﾒﾓﾒﾓ</td></tr>{% endfor %}{% endif %}');
                    */
                });
                
        }
    });
});

function computeDate(year, month) {
    var dt = new Date(year, month - 1);
    return dt;
}














/*
$('#begin-date').datepicker({
    minViewMode: 1,
    maxViewMode: 2,
    format: 'yyyy-mm',
    language:'ja',
    startView: 1,
    autoclose: true,
    //daysOfWeekHighlighted: [0,6],
}).on({
    changeDate : function(e) {
        $('#late-date').datepicker('show');
        selected_date = e['date']; //開始日のデータ取得
        yyyy = selected_date.getFullYear();
        mm = selected_date.getMonth() + 1;
        sd = computeDate(yyyy, mm); //0000-00の形で指定日後が返ってくる
        $('#late-date').datepicker('setStartDate', sd);
        
    }
});




('#late-date').datepicker({
    minViewMode: 1,
    maxViewMode: 2,
    format: 'yyyy-mm',
    language:'ja',
    startView: 1,
    autoclose: true,
    //daysOfWeekHighlighted: [0,6],
}).on({
    changeDate : function() {
        $.post("", $('#late-date').val());
    }
}); 
*/

$('late-date').attr('autocomplete', 'off');


/*
$('#datepicker').datepicker().on('changeDate', function(e){
    getSummary($('#datepicker').val());
});


function getSummary(datepicker) {
    $.post("polls/test_okajima", $('#datepicker').val());
}
*/
