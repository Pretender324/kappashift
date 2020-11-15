$(function () {
    var frm_cnt = $("#form-table").data("length") - 1;

    $(document).on('click', 'span.add', function () {
        var original = $('tr')[frm_cnt + 1];


        var originCnt = frm_cnt;
        frm_cnt++;


        var cloneCode = $(original).clone();
        console.log(cloneCode)
        cloneCode.attr('id', 'form-row[' + frm_cnt + ']') // クローンのid属性を変更。
        cloneCode.find('.sex')
            .attr('name', 'sex[' + frm_cnt + ']')
            .removeAttr('placeholder')
        cloneCode.find('.distance')
            .attr('name', 'distance[' + frm_cnt + ']')
            .removeAttr('placeholder')
        cloneCode.find('.style')
            .attr('name', 'style[' + frm_cnt + ']')
            .removeAttr('placeholder')
        cloneCode.find('.start_time')
            .attr('name', 'start_time[' + frm_cnt + ']')
            .removeAttr('placeholder')
        cloneCode.insertAfter(original)

    })
})

$(function () {
    var frm_cnt = $("#form-table-entry").data("length") - 1;

    $(document).on('click', 'span.add', function () {
        var original = $('tr')[frm_cnt + 1];


        var originCnt = frm_cnt;
        frm_cnt++;


        var cloneCode = $(original).clone();
        console.log(cloneCode)
        cloneCode.attr('id', 'form-row[' + frm_cnt + ']') // クローンのid属性を変更。
        cloneCode.find('.sex')
            .attr('name', 'sex[' + frm_cnt + ']')
            .removeAttr('placeholder')
        cloneCode.find('.distance')
            .attr('name', 'distance[' + frm_cnt + ']')
            .removeAttr('placeholder')
        cloneCode.find('.style')
            .attr('name', 'style[' + frm_cnt + ']')
            .removeAttr('placeholder')
        cloneCode.find('.start_time')
            .attr('name', 'start_time[' + frm_cnt + ']')
            .removeAttr('placeholder')
        cloneCode.insertAfter(original)

    })
})