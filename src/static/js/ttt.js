var winnerTemplate = function (winner) {
    return '<h2>' + winner + ' won!!!!!!</h2>' +
        '<input type="submit" value="play again">';
};

var tieTemplate = function() {
    return '<h2>its a tie</h2>'+
        '<input type="submit" value="play again">';
};
var showWinner = function (status) {
    if(status['tie']){
        $('.board').html(tieTemplate());
    }else{
        $('.board').html(winnerTemplate(status.winner));
    }
    $('input[value="play again"]').click(function(){
        location.reload();
    })
};

var drawBord = function (list) {
    [].forEach.call($("td"), function (ele, i) {
        ele.innerHTML = list[i + 1];
    })
};

var postPlayerMove = function (move) {
    $.post('playerMove', {move: +move}, function (res) {
        console.log(res)
        if (res.over) {
            showWinner(res);
            return;
        }
        drawBord(res['board']);
    })
};

var takePlayerMove = function (id) {
    postPlayerMove(id);
};


var play = function () {
    $.get("play", function (res) {
        drawBord(res['board']);
    })
};

var showBoard = function () {
    $(".chooseLetter").remove();
    $(".notification").remove();
    $(".board").removeClass('hidden');
    play();
};

var postSymbol = function () {
    var userLetter = $("#letter").find(':selected').val();
    $.post("letter", {letter: userLetter}, function (res) {
        $(".chooseLetter").toggleClass("hidden");
        $("h3").html("you have choose \"" + res + "\"");
        $(".notification").removeClass("hidden");
    })
};

var onReady = function () {
    $("#letterSelection").click(postSymbol);
    $('input[value="play"]').click(showBoard);
};


$(document).ready(onReady);