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
            .attr('name', 'sex')
            .removeAttr('placeholder')
        cloneCode.find('.distance')
            .attr('name', 'distance')
            .removeAttr('placeholder')
        cloneCode.find('.style')
            .attr('name', 'style')
            .removeAttr('placeholder')
        cloneCode.find('.start_time')
            .attr('name', 'start_time')
            .removeAttr('placeholder')
        cloneCode.insertAfter(original)

    })
})

//出場人数0の種目のビデオのセレクトボックスを無効化
$(function () {
    const n = $('#form-shift').data["length"];

    for (let i = 1; i <= n; i++) {
        let count = $('#member-count-' + i).data("count");
        if (count == 0) {
            $('#video-select-' + i).remove();
        }

    }
})