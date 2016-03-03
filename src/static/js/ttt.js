var onReady = function () {

    $('#letterSelection').click(function () {
        var userLetter = $('#letter').find(":selected").val();
        $.post('letter' ,{letter : userLetter} , function(res){
            $('.chooseLetter').toggleClass('hidden');
            $('h3').html('you have choose "'+res+'"');
            $('.notification').removeClass('hidden');
        })
    })


    $('input[value="play"]').click(function () {
        $('.chooseLetter').remove();
        $('.notification').remove();
        $('.board').removeClass('hidden')
    })

}


$(document).ready(onReady);